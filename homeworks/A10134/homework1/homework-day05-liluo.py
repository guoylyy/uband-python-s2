#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

import codecs
import os
import sys
import random

reload(sys)
sys.setdefaultencoding('utf8')

if_getpercent = 1
if_select = 1
if_in_order = 1
everyday_amount = 50

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
        line = line.strip()
        words = line.split(" ") #用空格分割
        words = word_split(words) #用-分割
        word_list.extend(words)
    return word_list

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
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    word=word.lower()
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word

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
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    #排序
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict

def tup2list(volcaulay_list_tup):
    volcaulay_list_lst = []
    for val in volcaulay_list_tup:
        volcaulay_list_lst.append(list(val))
    return volcaulay_list_lst

def percent(volcaulay_list, total_count):
    current_count = 0
    for val in volcaulay_list:
        num = val[1]
        current_count = current_count + num
        word_rate = (float(current_count)/total_count) * 100
        val.append(word_rate)
    return volcaulay_list

def select_word(volcaulay_list,start_end):
    lst=[]
    for val in volcaulay_list:
        if (val[2] >= start_end[0] * 100) and (val[2] <= start_end[1] * 100):
            lst.append(val)
    return lst
#4.输出成csv
def print_to_csv(volcaulay_list, to_file_path,if_percent):
    nfile = codecs.open(to_file_path, 'w+', "utf-8")

    for val in volcaulay_list:
        if if_percent:
            nfile.write("%s,%s,%s,%s\n" % (val[0], str(val[1]), str(round(val[2],2)), str(val[3]).encode('utf-8')))
        else:
            nfile.write("%s,%s,%s" % (val[0], str(val[1]),val[2]))
    nfile.close()

#读入字典
def read_dict(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    dict = {}
    for line in lines:
        line = line.strip()
        words = line.split(" ") #用空格分割
        if len(words)==4:
            dict[words[0]]=words[3].replace(",",";")
    return dict

def look_up(dict,word_list):
    for val in word_list:
        if dict.has_key(val[0]):
            val.append(dict[val[0]].encode('utf-8'))
        else:
            val.append(u"not found")
    return word_list


def select_daily(word_list_raw,amount,if_inorder):
    list=[]
    word_list=sorted(word_list_raw)
    if len(word_list)>=amount:
        if if_inorder:
            order=range(0,amount)
        else:
            order=random.sample(range(1,len(word_list)),amount)
        for i in order:
            list.append(word_list[i])
    else:
        list.extend(word_list)
    for word in list:
        word_list.remove(word)

    return list,word_list

def csv_dailys(word_list,amount,if_inorder):
    i=0
    while len(word_list):
        list,word_list=select_daily(word_list,amount,if_inorder)
        print_to_csv(list,'output/'+str(i)+'.csv',if_getpercent)
        i=i+1





def main():

    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    #2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' %(len(f_words))
    
    #3. 统计单词和排序
    word_list = statictcs_words(f_words)
    word_list1=tup2list(word_list)

    start_and_end = [0.5, 0.7] #截取这一部分的单词

    if if_getpercent:
        word_list2 = percent(word_list1, total_word_count)
        if if_select:
            word_listrecite=select_word(word_list2,start_and_end)
        else:
            word_listrecite=word_list2
    else:
        word_listrecite=word_list1

    #4生成释义
    dict = read_dict("8000-words.txt")
    wl_withmeaning = look_up(dict,word_listrecite)

    #5. 输出文件
    print_to_csv(wl_withmeaning, 'output/test.csv',if_getpercent)
    wl_raw=wl_withmeaning

    csv_dailys(wl_raw, everyday_amount, if_in_order)
if __name__ == "__main__":
    main()