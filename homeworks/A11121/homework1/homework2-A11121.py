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
def statistics_words(words):
    # type: (object) -> object
    s_word_dict = {}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    return s_word_dict
    #排序
def sort_words(s_word_dict):
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict


#4.输出成csv
def print_to_csv(intercepted_word_dict, to_file_path):
    nfile = open(to_file_path,'w+')
    for val in intercepted_word_dict:
        if len(val) == 4:
            nfile.write("%s,%s,%0.2f,%s \n" % (val[0], str(val[1]), val[2], val[3]))
        elif len(val) == 3:
            nfile.write("%s,%s,%0.2f\n" % (val[0], str(val[1]), val[2]))
    nfile.close()

#5 获取累积百分数
def word_percent(volcabulary_list_lst, total_count):
    word_percent_list = []
    current_count = 0
    for val in volcabulary_list_lst:
        num = val[1]
        current_count = current_count + num
        word_perct = (float(current_count)/total_count) * 100
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

def explanation_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    word_list = []
    word_list_utf = []
    for line in lines:
        line = line.strip()
        words = line.split("   ") #用空格分割
        words = word_split(words) #用-分割
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
    return fword_list_recite, fword_list_noExp

def tup2list(volcabulary_list_tup):
    volcabulary_list_lst = []
    for val in volcabulary_list_tup:
        volcabulary_list_lst.append(list(val))
    return volcabulary_list_lst

def get_daily_task(daily_task, total_list, num):
    daily_task_list =[]
    for index,val in enumerate(total_list):#有问题！为什么一定要加上val？以及注意下enumerate的用法
        daily_task_list.append(total_list[index + daily_task * (num - 1)])
        if len(daily_task_list) >= daily_task:
            break
    return daily_task_list




def main():
    daily_task = 100 #设置每日单词量
    day_No = 1 #当前天数
    if_sort = True #顺序/乱序
    if_intercept = True #是否截取
    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    #2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' %(len(f_words))
    
    #3. 统计单词
    word_list = statistics_words(f_words)
    #4. 排序
    if if_sort:
        sorted_dict = sort_words(word_list)
    else:
        sorted_dict = word_list

    #5. 将tuple格式转为可变的list格式
    volcabulary_list_lst = tup2list(sorted_dict)

    #6.计算得到单词频次
    intercepted_word_dict = word_percent(volcabulary_list_lst, total_word_count)
    if if_intercept:
        start_and_end = [0.5, 0.7]  # 截取这一部分的单词
        word_list_recite = select_word(intercepted_word_dict, start_and_end)
    else:
        word_list_recite = intercepted_word_dict
    print '需要背诵的单词有%d个' % len(word_list_recite)
    explanation_list = explanation_file('8000-words.txt')
    fword_list_recite, fword_list_noExp = add_explanation(word_list_recite, explanation_list)

    #7. 输出文件
    print_to_csv(fword_list_recite, 'output/Day5.csv')
    print_to_csv(fword_list_noExp, 'output/Day5_2.csv')

    #8.获取每日任务
    daily_task_list = get_daily_task(daily_task, fword_list_recite, day_No)

    print_to_csv(daily_task_list,'output/'+str(day_No)+'.csv')

if __name__ == "__main__":
    main()