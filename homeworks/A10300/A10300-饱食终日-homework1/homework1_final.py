# -*- coding: utf-8 -*-

import codecs
import os
# 解决 'ascii' codec can't decode byte 0xe5的问题！！（以下三句
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    #排序
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict

#4.输出成csv
def print_to_csv(word_percent_dict, to_file_path ): # volcaulay_list is a dict
    nfile = open(to_file_path,'w+')
    for val in word_percent_dict:
        if len(val) == 4:
            nfile.write("%s,%s,%0.2f,%s \n" % (val[0], str(val[1]), val[2], val[3]))
        elif len(val) == 3:
            nfile.write("%s,%s,%0.2f\n" % (val[0], str(val[1]), val[2]))
    nfile.close()

def tup2list(volcaulay_list_tup):
    volcaulay_list_lst = []
    for val in volcaulay_list_tup:
        volcaulay_list_lst.append(list(val))
    return volcaulay_list_lst

#5.获取相应的百分比列表
def word_percent(volcaulay_list_lst, total_count):
    word_percent_list = []
    current_count = 0
    for val in volcaulay_list_lst:
        num = val[1]
        current_count = current_count + num
        word_perct = (float(current_count)/float(total_count)) * 100
        val.append(word_perct)
        word_percent_list.append(val)
    return word_percent_list

def select_word(word_percent_list, rate_range):
    word_list_recite = []
    start = rate_range[0] * 100
    end = rate_range[1] * 100
    for val in word_percent_list:
        if val[2] >= start and val[2] <= end:
            word_list_recite.append(val)
    return word_list_recite

def read_explanation(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    word_list = []
    word_list_utf = []
    for line in lines:
        line = line.strip()
        words = line.split("   ") #用空格分割
        word_list.append(words)
    for word in word_list:
        word_utf = []
        for index in word:
            word_new = index.encode("utf-8")
            word_utf.append(word_new)
            word_list_utf.append(word_utf)
    return word_list_utf

def add_explanation(word_list_recite, explanation_list):

    words_list = []
    explanation = []
    fword_list_recite =[]
    fword_list_noExp =[]
    for words in explanation_list:
        if len(words) == 2:
            words_list.append(words[0])
            explanation.append(words[1])
    for word in word_list_recite:
        if word[0] in words_list:
            idx = words_list.index(word[0])
            word.append(explanation[idx])
            fword_list_recite.append(word)
        else:
            fword_list_noExp.append(word)
    return fword_list_recite , fword_list_noExp

def main():
    get_wordlist = True
    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))
    #2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' %(len(f_words))
    #3. 统计单词和排序
    word_list = statictcs_words(f_words)
    #4. 将tuple格式转为可变的list格式
    volcaulay_list_lst = tup2list(word_list)
    #5.计算得到单词频次
    word_percent_dict = word_percent(volcaulay_list_lst,total_word_count)
    #6. 截取这一部分的单词
    if get_wordlist:
        start_and_end = [0.5, 0.7]  #
    else:
        start_and_end = [0.0, 1.0]
    word_list_recite = select_word(word_percent_dict, start_and_end)
    print '需要背诵的单词有%d个' % len(word_list_recite)
    explanation_list = read_explanation('8000-words.txt')
    fword_list_recite, fword_list_noExp = add_explanation(word_list_recite, explanation_list)
    #4. 输出文件
    print_to_csv(fword_list_recite, 'output/Day5.csv' )  #查到释义的单词
    print_to_csv(fword_list_noExp, 'output/Day5_2.csv')  #未查到释义的单词

if __name__ == "__main__":
    main()