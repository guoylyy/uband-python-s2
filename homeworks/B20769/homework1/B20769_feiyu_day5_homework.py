# -*- coding: utf-8 -*-

import codecs
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')
#1. 读取文件
#根据“-”再次划分单词：['aa', 'aaa-bbb-sds'] => ['aa', 'aaa', 'bbb', 'sds']
def word_split(words):
    new_list = []
    for word in words:
        if '-' not in word:
            new_list.append(word)
        else:
            lst = word.split('-')
            new_list.extend(lst)
    return new_list
#读取单个文件，输出问由文件中所有单词组成的列表
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()   #按段落（行）读取文件，输出为n行数据
    word_list = []
    for line in lines:
        line = line.strip()#去掉行首尾的空格
        words = line.split(" ") #用空格分割
        words = word_split(words) #用”-“分割
        word_list.extend(words)
    return word_list
#读取文件夹中所有文件的路径，输出为一组文件路径
def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths
#读取多个文件里的单词，输出问所有单词的一个列表
def read_files(file_paths):
    final_words = []
    for path in file_paths:
        final_words.extend(read_file(path))
    return final_words
#2.获取格式化之后的单词
#格式化一个单词，并输出
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()
#格式化一串单词，并输出为一个新的列表
def format_words(words):
    word_list = []
    for word in words:
        wd = format_word(word)
        if wd:#判断该单词是否为空格，若为空格则略过
            word_list.append(wd)
    return word_list
#3. 统计单词数目
# {'aa':4, 'bb':1}
#统计每个单词出现的次数
def statictcs_words(words):
    s_word_dict = {}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1

    #根据单词出现的频次排序，，
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict
#将元组转变为列表，（将字典转化为以小列表为元素的列表）
def tup2list(volcaulay_list_tup):
    volcaulay_list_lst = []
    for val in volcaulay_list_tup:
        volcaulay_list_lst.append(list(val))
    return volcaulay_list_lst
#4.输出成csv
def print_to_csv(volcaulay_list, to_file_path):
    nfile = open(to_file_path, 'w+')
    for val in volcaulay_list:
        nfile.write("%s,%s,%0.2f,%s \n" % (val[0], str(val[1]), val[2], val[3]))
    nfile.close()
#计算单词比例
def word_rate(volcaulay_list,total_count):
    word_rates_dict = []
    current_count = 0
    for val in volcaulay_list:
        current_count = current_count + val[1]
        word_rate = (float(current_count) / total_count) * 100
        val.append(word_rate)
        word_rates_dict.append(val)
    return word_rates_dict
#截取累积频次在一定范围的单词
def select_word(word_percent_list, rate_range):
    word_list_recite = []
    start = rate_range[0] * 100
    end = rate_range[1] * 100
    for val in word_percent_list:
        if val[2] >= start and val[2] <= end:
            word_list_recite.append(val)###列表中的元素就是列表
    return word_list_recite
#读取释义
def read_meaning(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()   #按段落（行）读取文件，输出为n行数据
    words_meaning_list = []
    for line in lines:
        line = line.strip()#去掉行首尾的空格
        word, space, meaning = line.partition(" ")#partition 和 split分割得到的结果不一样
        meaning = meaning.strip()
        word_meaning = [word,meaning]
        words_meaning_list.append(word_meaning)
    return words_meaning_list
#给单词配上解释
def meanging_word(volcaulay_list,words_meaning):
    words_meaning_dict = {}
    meanings2words = []
    for word in words_meaning:
        words_meaning_dict[word[0]] = word[1]
    for val in volcaulay_list:
        if words_meaning_dict.has_key(val[0]):
            val.append(words_meaning_dict[val[0]])
        else:
            val.append('没有该单词的解释')
        meanings2words.append(val)
    return meanings2words
def main():
    #读取文本
    words = read_files(get_file_from_folder('data2'))
    print '获取了未格式化的单词 %d 个' % (len(words))
    #清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' %(len(f_words))
    # 统计单词和排序
    word_list = statictcs_words(f_words)
    #将字典变成以列表为元素的列表
    word_list_lst = tup2list(word_list)
    #计算单词的累积频率并将其加到单词频数列表中
    word_rates_dict = word_rate(word_list_lst,total_word_count)
    #截取单词
    start_and_end = [0.3, 0.7] #截取这一部分的单词
    s_word_list = select_word(word_rates_dict,start_and_end)
    #读取单词解释文件
    words_meaning = read_meaning("8000-words.txt")
    #单词解释和经济学人中抽取的单词配对
    meanings_words = meanging_word(s_word_list, words_meaning)
    # 输出文件
    print_to_csv(meanings_words, 'output/words_meanings.csv')

if __name__ == "__main__":
    main()