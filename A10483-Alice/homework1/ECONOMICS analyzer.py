# -*- coding: utf-8 -*-

import codecs
import os
import random


# 1. 读取文件
# ['aa', 'aaa-bbb-sds'] => ['aa', 'aaa', 'bbb', 'sds']
def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list


def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")  # 打开文件
	lines = f.readlines()
	word_list = []
	for line in lines:
		line = line.strip()
		words = line.split(" ")  # 用空格分割
		words = word_split(words)  # 用-分割
		word_list.extend(words)
	return word_list


def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths


# 读取多文件里的单词
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words


# 2.获取格式化之后的单词
def format_word(word):
	fmt = 'abcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '')
	return word.lower()


def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(wd)
	return word_list


# 3. 统计单词数目
# 将元组的列表转换为列表的列表
def tuple_to_list(t):
	word_list = []
	for item in t:
		word_list.append(list(item))
	return word_list


# {'aa':4, 'bb':1}
def statistics_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word] + 1
		else:
			s_word_dict[word] = 1
	# 排序
	sorted_word_tuples = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
	# 将排序后生成的元组的列表还原为列表的列表
	word_list = tuple_to_list(sorted_word_tuples)
	return word_list


# 4.统计单词出现百分比
def rate_words(vocabulary_list, total_count):
	current_count = 0
	for val in vocabulary_list:
		num = val[1]
		current_count = current_count + num
		word_rate = (float(current_count) / total_count) * 100
		val.append(word_rate)


# 5.截取百分比区间单词
def extract_rate_scale(word_list, scale):
	scale_list = []
	for item in word_list:
		if item[2] >= scale[0]*100 and item[2] <= scale[1]*100:
			scale_list.append(item)
	return scale_list


# 6.查找单词在词典中解释
def read_dict(dict_file_path):
	f = codecs.open(dict_file_path, 'r', "utf-8")  # 打开文件
	lines = f.readlines()
	word_dict = {}
	for line in lines:
		line = line.strip()
		word, space, meaning = line.partition(' ')  # 以空格区分单词与释义
		meaning = meaning.strip()
		if word:
			word_dict[word] = meaning
	return word_dict


def get_words_meaning(dict_file_path, word_list):
	word_dict = read_dict(dict_file_path)
	for item in word_list:
		if word_dict.has_key(item[0]):
			meaning = word_dict[item[0]]
		else:
			meaning = u'未找到释义'
		item.append(meaning)


# 7.生成每日单词表
def generate_tasks(scale_list, num_of_words, choice_random):
	if choice_random:
		random.shuffle(scale_list)
	else:
		scale_list = sorted(scale_list, key=lambda d: d[0], reverse=False)
	task_list = []
	index = 0
	while index < len(scale_list):
		task_list.append(scale_list[index:index+num_of_words])
		index = index + num_of_words
	return task_list


# 7.输出成csv
def print_to_csv(vocabulary_list, to_file_path):
	outfile = codecs.open(to_file_path, 'w+', "utf-8")
	for val in vocabulary_list:
		outfile.write("%s,%s,%0.2f,%s\n" % (val[0], str(val[1]), val[2], val[3]))
	outfile.close()


def print_tasks(task_list, to_file_path):
	day = 1
	for item in task_list:
		print_to_csv(item, to_file_path+"day" + str(day) + '.csv')
		day = day + 1


def main():
	# 1. 读取文本
	words = read_files(get_file_from_folder('data1'))
	print '获取了未格式化的单词 %d 个' % (len(words))

	# 2. 清洗文本
	f_words = format_words(words)
	total_word_count = len(f_words)
	print '获取了已经格式化的单词 %d 个' % (len(f_words))

	# 3. 统计单词和排序
	word_list = statistics_words(f_words)

	# 4.统计单词出现百分比
	rate_words(word_list, total_word_count)

	# 5.为单词查找解释
	get_words_meaning('8000-words.txt', word_list)

	# 输出文件
	if not os.path.exists("output"):
		os.mkdir("output")
	print_to_csv(word_list, 'output/words.csv')

	# 6.询问是否要截取百分比区间的单词
	extract = raw_input('是否要截取百分比区间(50%~70%)单词？ (Y/N) ')
	if extract == 'Y' or extract == 'y':
		start_and_end = [0.5, 0.7]  # 截取这一部分的单词
		scale_list = extract_rate_scale(word_list, start_and_end)
		print "截取了%d个单词" % (len(scale_list))
		print_to_csv(scale_list, 'output/scale.csv')

	# 7.生成背单词表
	task_list = []
	num_of_words = raw_input('将生成每日单词表。每天背几个单词？')
	if num_of_words.isdigit():
		if (type(eval(num_of_words)) == int) and (int(num_of_words) > 0):
			choice_random = raw_input("是否随机生成单词表？(Y/N)")
			if choice_random == 'Y' or choice_random == 'y':
				task_list = generate_tasks(scale_list, int(num_of_words), True)
			else:
				task_list = generate_tasks(scale_list, int(num_of_words), False)
		print_tasks(task_list, "output/")
		print "生成了%d天的单词表" % len(task_list)


if __name__ == "__main__":
	main()