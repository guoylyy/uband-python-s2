# -*- coding: utf-8 -*-

import codecs
import os
import csv
import re

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


def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()   #移除首尾空格
        words = line.split(" ") #用空格分割
        words = word_split(words) #用-分割
        word_list.extend(words)
    return word_list

#读取释义txt文件
def read_meaning(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    dict = {}
    for line in lines:
        words = re.split(r'\s+', line)  #多个空格分割
        key = words[0].strip()
        value = words[1].strip()
        dict[key] = value
    return dict


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
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
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

#3. 统计单词数目
# {'aa':4, 'bb':1}
def statictcs_words(words):
    s_word_dict = {}
    for word in words:
        if word in s_word_dict:
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    #排序
    sorted_dict = sorted(s_word_dict.items(), key=lambda d: d[1], reverse=True)
    return sorted_dict   #tuple组成的list

def tup2list(sorted_dict):
    list_words = []
    for tup_word in sorted_dict:  #tuple
        list_word = [tup_word[0], tup_word[1]]
        list_words.append(list_word)
    return list_words   #list组成的list

#获取词频
def get_rate(word_list, total_count):
    current_count = 0
    for val in word_list:
        num = val[1]
        current_count = current_count + num
        word_rate = round((float(current_count)/total_count) * 100, 2)   #保留两位小数
        val.append(word_rate)   #rate加在每一个单词的后面
    return word_list

#添加释义
def add_meaning(word_list, dictionary):
    for word in word_list:
        k = word[0]
        if k in dictionary:
            word.append(dictionary[k])
    return word_list

#截取单词
def cut_words(word_list, ranges):
    start = ranges[0]*100
    end = ranges[1]*100
    cut_list = []
    for val in word_list:
        if((val[2]>= start) and (val[2]<= end)):
            cut_list.append(val)
    return cut_list

#4.输出成csv
def print_to_csv(volcaulay_list, to_file_path):
    nfile = open(to_file_path, 'w+')
    swriter = csv.writer(nfile, dialect='excel')
    for val in volcaulay_list:
        swriter.writerow(val)
    nfile.close()

def main():
    #1. 读取文本
    is_rate = True   #是否算百分比
    words = read_files(get_file_from_folder('data1'))
    print ('获取了未格式化的单词 %d 个' % (len(words)))

    #2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print ('获取了已经格式化的单词 %d 个' %(len(f_words)))
    
    #3. 统计单词和排序
    tup_words = statictcs_words(f_words)

    #tup2list
    list_words = tup2list(tup_words)

    if(is_rate):
    #获取词频
        word_list = get_rate(list_words, total_word_count)

    # read meaning  day5_homework
        dictionary = read_meaning('8000-words.txt')
        word_list = add_meaning(word_list, dictionary)

    # 截取这一部分的单词
        start_and_end = [0.5, 0.7]
        partition_words = cut_words(word_list, start_and_end)
        print(len(partition_words))

    #4. 输出文件
        print_to_csv(word_list, 'output/all.csv')
        print_to_csv(partition_words, 'output/partition.csv')

    else:
        print_to_csv(list_words, 'output/test.csv')

if __name__ == "__main__":
    main()