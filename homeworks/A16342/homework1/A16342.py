# -*- coding: utf-8 -*-

import codecs
import os
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

#读取单词释义表
def read_meaning(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    num = 0
    words_dict = {}
    for line in lines:
        line = line.strip()
        word, space, meaning  = line.partition(" ")
        if word:
            words_dict[word] = meaning
    return words_dict

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

#输出词频
def word_rate(vocabulary_list,total_count):
    rate_list = []
    current_count = 0
    for val in vocabulary_list:
        num = val[1]
        current_count += num
        word_rate = current_count *100.00 / total_count
        new_val = (val[0],val[1],word_rate)
        rate_list.append(new_val)
    return rate_list

#截取固定比例
def cut_list(rate_list,start_and_end):
    cut_list = []
    start = start_and_end[0] * 100
    end = start_and_end[1] * 100
    for val in rate_list:
        if start <= val[2] <= end :
            cut_list.append(val)
    return cut_list

#匹配,提取有释义单词
def match_meaning(vocabulary_list,words_dict):
    meaning_list = []
    without_mean = []
    for val in vocabulary_list:
        word = val[0]
        if words_dict.has_key(word) == True:
            new_val = (val[0],val[1],val[2],words_dict[word])
            meaning_list.append(new_val)
        else:
            new_val = (val[0],val[1],val[2],'NA')
            without_mean.append(new_val)
    return meaning_list

#拆分每日推送单词列表
def word_daily(word_mean):
    n = int(raw_input('请输入每天背诵单词数:'))
    is_sorted = int(raw_input('您需要按词频排序(0)还是按字母表排序（1)'))
    total_day = 0
    total_daily_list = []
    daily_list = []
    if is_sorted == 1:
        word_mean = sorted(word_mean, key = lambda d:d[0])
    while len(word_mean) >= n :
        add_word = word_mean[0: n]
        word_mean = word_mean[n:]
        daily_list.extend(add_word)
        total_daily_list.append(daily_list)
        daily_list = []
        total_day += 1
    if word_mean:
        total_daily_list.append(word_mean)
        total_day += 1
    return total_daily_list, total_day

#4.输出成csv
def print_to_csv(volcaulay_list, to_file_path):
    nfile = open(to_file_path,'w+')
    for val in volcaulay_list:
        num = val[1]
        meaning = val[3]
        nfile.write(codecs.BOM_UTF8)
        nfile.write("%s,%s,%0.2f,%s\n" % (val[0], str(num),val[2],meaning.encode('utf-8')))
    nfile.close()

def main():
    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    #2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' % (len(f_words))
    
    #3. 统计单词和排序
    word_list = statictcs_words(f_words)

    #计算词频
    word_rate_list = word_rate(word_list, total_word_count)

    #截取固定词频
    start_and_end = [0.5, 0.7] #截取这一部分的单词
    word_cut_list = cut_list(word_rate_list,start_and_end)

    #读取字典
    word_dict = read_meaning('8000-words.txt')


    #匹配释义
    words_mean = match_meaning(word_rate_list,word_dict)
    words_cut_mean = match_meaning(word_cut_list,word_dict)

    #拆分每日单词表
    total_daily_list, total_day = word_daily(words_mean)
    print '一共要背 %d 天'% (total_day)

    #4. 输出文件
    print_to_csv(words_mean, 'output/all.csv')
    print_to_csv(words_cut_mean, 'output/cut.csv')

    #输出每日单词表
    for index,item in enumerate(total_daily_list):
        print_to_csv(total_daily_list[index],'output/daily/%d.csv'% (index))

if __name__ == "__main__":
    main()
