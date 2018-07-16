# -*- coding: utf-8 -*-

import codecs
import os

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
    return sorted_dict

#获取词频
def get_rate(word_list, total_count):
    rate = {}
    current_count = 0
    for val in word_list:
        num = val[1]
        current_count = current_count + num
        word_rate = (float(current_count)/total_count) * 100
        rate[val] = word_rate
    return rate

#截取单词
def cut_words(word_rate, range):
    start = range[0]*100
    end = range[1]*100
    cut_list = []
    for val in word_rate:
        if((word_rate[val]>= start) and (word_rate[val]<= end)):
            cut_list.append(val[0])
    return cut_list

#4.输出成csv
def print_to_csv(volcaulay_list, to_file_path, rate):
    nfile = open(to_file_path, 'w+')
    for val in volcaulay_list:
        nfile.write("%s,%s,%0.2f\n" % (val[0], str(val[1]), rate[val]))
    nfile.close()

def print_to_csv_no_rate(volcaulay_list, to_file_path):
    nfile = open(to_file_path, 'w+')
    for val in volcaulay_list:
        nfile.write("%s,%s\n" % (val[0], str(val[1])))
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
    word_list = statictcs_words(f_words)

    if(is_rate):
    #获取词频
        word_rate = get_rate(word_list, total_word_count)

    # 截取这一部分的单词
        start_and_end = [0.5, 0.7]
        partition_words = cut_words(word_rate, start_and_end)
        print(len(partition_words))

    #4. 输出文件
        print_to_csv(word_list, 'output/test.csv', word_rate)

    else:
        print_to_csv_no_rate(word_list, 'output/test.csv')

if __name__ == "__main__":
    main()