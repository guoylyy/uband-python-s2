# -*- coding: utf-8 -*-

import codecs
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

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
    fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
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
    return s_word_dict

#4.排序
def sort_words(s_word_dict):
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict  #返回列表，每个元素是一个元祖

#5.计算词频
def rate_words(volcaulay_list,total_count):
    rate_list = []
    current_count = 0
    for val in volcaulay_list:
        num = val[1]
        current_count = current_count + num
        word_rate = float(current_count)/total_count
        rate_list.append(word_rate)
    return rate_list

#6.截取词频
def part_words(volcaulay_list,rate_list,rate_range):
    part_word_list = []
    for index in range(len(volcaulay_list)):
        if (rate_list[index] >= rate_range[0]) & (rate_list[index] <= rate_range[1]):
            part_word_list.append(volcaulay_list[index])
    return part_word_list

#7.截取相应的频率列表
def part_rate(rate_list,rate_range):
    part_rate_list = []
    for rate in rate_list:
        if (rate >= rate_range[0]) & (rate <= rate_range[1]):
            part_rate_list.append(rate)
    return part_rate_list

#8.输出成csv
def print_to_csv(volcaulay_list, to_file_path, rate_list):
    nfile = open(to_file_path,'w+')
    for index in range(len(volcaulay_list)):
        nfile.write("%s,%s,%s\n" % (volcaulay_list[index][0], str(volcaulay_list[index][1]),rate_list[index]*100))
    nfile.close()

def print_def_to_csv(volcaulay_list, to_file_path, rate_list, def_list):
    nfile = open(to_file_path,'w+')
    for index in range(len(volcaulay_list)):
        nfile.write("%s,%s,%s,%s\n" % (volcaulay_list[index][0], str(volcaulay_list[index][1]),rate_list[index]*100,def_list[index]))
    nfile.close()

        #9.读取字典
def read_dict(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    word_dict = {}
    for line in lines:
        line = line.strip()
        word, space, meaning = line.partition(' ') #以空格区分单词与释义
        meaning = meaning.strip()
        if word:
            word_dict[word] = meaning
    return word_dict

    #10.找到单词释义
def find_defination(words_list,def_dict):
    def_list = []
    for word in words_list:
        if def_dict.has_key(word[0]):
            def_list.append(def_dict[word[0]])
        else:
            def_list.append('no defination found')
    return def_list

#12.生成每日单词表
def day_word_list(num_vol_day,word_list,word_rate_list,defination_list):
    num_day = len(word_list)/num_vol_day
    for num in range(1,num_day+1):
        day_word_list = word_list[(num-1) * num_vol_day:num * num_vol_day]
        day_word_rate_list = word_rate_list[(num-1) * num_vol_day:num * num_vol_day]
        day_word_def_list = defination_list[(num-1) * num_vol_day:num * num_vol_day]
        file_name = 'output/word_%d.csv' %num
        # print file_name
        print_def_to_csv(day_word_list,file_name,day_word_rate_list,day_word_def_list)
    if_left = len(word_list)%num_vol_day
    if if_left:
        day_word_list = word_list[-if_left:]
        day_word_rate_list = word_rate_list[-if_left:]
        day_word_def_list = defination_list[-if_left:]
        file_name = 'output/word_%d.csv' %(num_day+1)
        # print file_name
        print_def_to_csv(day_word_list,file_name,day_word_rate_list,day_word_def_list)


def main():

    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    #2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' %(len(f_words))
    
    #3. 统计单词
    word_dict = statictcs_words(f_words)

    #4.排序
    word_list = sort_words(word_dict)

    #5.统计词频
    word_rate_list = rate_words(word_list,total_word_count)
    # print word_rate_list

    #6.截取单词
    start_and_end = [0.5, 0.7] #截取这一部分的单词
    parted_words_list = part_words(word_list,word_rate_list,start_and_end)

    #7.截取相应词频列表
    parted_words_rate_list = part_rate(word_rate_list,start_and_end)

    #8. 输出文件
    # print_to_csv(word_list, 'output/total_words.csv', word_rate_list)
    # print_to_csv(parted_words_list,'output/part_words.csv',parted_words_rate_list)

    #9.读取字典
    defination_dict = read_dict('8000-words.txt')

    #10.找到单词释义
    defination_list = find_defination(parted_words_list,defination_dict)

    #11.输出释义文件
    print_def_to_csv(parted_words_list,'output/defination.csv',word_rate_list,defination_list)

    #12.生成背单词表
    num_vol_day = 10
    day_word_list(num_vol_day,parted_words_list,word_rate_list,defination_list)


if __name__ == "__main__":
    main()