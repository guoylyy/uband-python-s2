# -*- coding: utf-8 -*-
# author:kudari

import sys
import random
reload(sys)
sys.setdefaultencoding( "utf-8" )
import codecs
import os
import csv



#1. 读取文件
#['aa', 'aaa-bbb-sds'] => ['aa', 'aaa', 'bbb', 'sds']
def word_split(words):
    new_list = []
    for word in words:
        if '-' not in word:
            new_list.append(word)
        else:
            lst = word.split('-')
            new_list.extend(lst)
    return new_list

#读取一份文件
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ") #用空格分割
        words = word_split(words) #用-分割
        word_list.extend(words)
    return word_list

#
def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

#读取多文件里的单词
def read_files(file_paths):
    final_words = []
    for path in file_paths:
        final_words.extend(read_file(path))
    return final_words


#2.获取格式化之后的单词
def format_word(word_list):
	standardList = []
	fmt = 'abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for index, string in enumerate(word_list):
		for char in string:
			if char not in fmt:
				string = string.replace(char, '')
		if string != '':
			standardList.append(string.lower())
	return standardList


#3. 统计单词数目
# {'aa':4, 'bb':1}
def statictcs_words(words):
    s_word_dict = {}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    #排序
    return sort_dict_reverse(s_word_dict,1)

# 4.计算每个词的累计频率
def calculate_rate(vocabulary_list, total_count):
    new_vocabulary_list = {}
    current_count = 0
    for val in vocabulary_list:
        num = val[1]
        current_count =current_count + num
        word_rate = (float(current_count)/total_count) * 100
        new_vocabulary_list[val[0]] = word_rate
    #排序
    return sort_dict_standard(new_vocabulary_list, 1)

# 排序
def sort_dict_standard(vocabulary_list, n):
    sorted_dict = sorted(vocabulary_list.iteritems(), key=lambda d: d[n], reverse=False)
    return sorted_dict

def sort_dict_reverse(vocabulary_list, n):
    sorted_dict = sorted(vocabulary_list.iteritems(), key=lambda d: d[n], reverse=True)
    return sorted_dict

# 筛选特定频率内的单词
def select_vocab(vocabulary_list, range):
    new_vocabulary_list = {}
    for val in vocabulary_list:
        rate = val[1]
        if ((rate >= range[0]) and (rate <= range[1])):
            new_vocabulary_list[val[0]] = val[1]
    # 排序
    return sort_dict_standard(new_vocabulary_list,1)

# 读取字典
def read_dic(file_path):
    dictionary = {}

    f = codecs.open(file_path, 'r', "utf-8")  # 打开文件
    lines = f.readlines()

    for line in lines:
        lineList=[]
        all_words = line.split(" ")
        for val in all_words:
            if val != "":
                lineList.append(val)
        dictionary[lineList[0]] = lineList[1]

    return dictionary

def translate_words(vocabulary_list, dictionary):
    word_list = {}
    for val in vocabulary_list:
        vocab = str(val[0])
        if dictionary.has_key(vocab):
            translation = dictionary[vocab]
            word_list[vocab] = translation
    return sort_dict_standard(word_list,0)

#4.输出成csv
def print_to_csv(vocabulary_list, to_file_path):
    nfile = open(to_file_path,'w+')
    for val in vocabulary_list:
        nfile.write("%s, %s\n" % (val[0], val[1]))
    nfile.close()

def how_many_words_a_day(word_list, plan):
    number_of_words_a_day = len(word_list)/plan
    return number_of_words_a_day

def read_csv(file_path):
    word_list = []
    csv_reader = csv.reader(open(file_path))
    for row in csv_reader:
        word_list.append(row)
    for index, list in enumerate(word_list):
        if list == []:
            del word_list[index]
    return word_list

# 分割单词表
def splist(word_list, number_of_words_a_day,plan,shuffle):
    if shuffle == True:
        random.shuffle(word_list)
    print_form = []
    i = 0
    while i < plan - 1:
        #一个列表
        single_list = word_list[i*number_of_words_a_day:(i+1)*number_of_words_a_day]
        print_form.append(single_list)
        i = i+1
        # 最后一个一天多把多余的单词一起背掉
    single_list = word_list[i * number_of_words_a_day:(len(word_list)-1)]
    print_form.append(single_list)
    return print_form

#输出多个csv
def print_to_csvs(vocabulary_list, to_file_path, plan):
    for i in range(plan):
        print_to_csv(vocabulary_list[i], to_file_path + '/day' + str(i+1) + '.csv')

def main():
    # # day 1
    # #1. 读取文本
    # words = read_files(get_file_from_folder('data1'))
    # print '获取了未格式化的单词 %d 个' % (len(words))
    # print words
    # #2. 清洗文本
    # f_words = format_word(words)
    # total_word_count = len(f_words)
    # print '获取了已经格式化的单词 %d 个' %(len(f_words))
    # print f_words
    # #3. 统计单词和排序
    # word_list = statictcs_words(f_words)
    # print word_list
    # #4. 计算单词累计频率
    # word_rate_list = calculate_rate(word_list, total_word_count)
    # print '获取了带单词累计频率的单词表，共 %d 个' % (len(word_rate_list))
    # print word_rate_list
    # #5. 按频率筛选单词
    # range = [50, 80]
    # selected_vocab = select_vocab(word_rate_list, range)
    # print selected_vocab
    # # 输出文件
    # # print_to_csv(selected_vocab, 'output/test.csv')
    # #day 2
    # dictionary = read_dic('data3/8000-words.txt')
    # recommended_word_list = translate_words(selected_vocab,dictionary)
    # print recommended_word_list
    # print_to_csv(recommended_word_list, 'output/test2.csv')
    # day 3

    #读取csv单词表
    word_list = read_csv('output/test2.csv')

    #计划背50天
    plan = 50
    number_of_words_a_day = how_many_words_a_day(word_list, plan)

    # 顺序分割并输出
    list_for_print = splist(word_list, number_of_words_a_day, plan, shuffle = False)
    print_to_csvs(list_for_print, 'test3', plan)

    # 乱序分割并输出
    list_for_print2 = splist(word_list, number_of_words_a_day, plan, shuffle = True)
    print_to_csvs(list_for_print2, 'test4', plan)


if __name__ == "__main__":
    main()