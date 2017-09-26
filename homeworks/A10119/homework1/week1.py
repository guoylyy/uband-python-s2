# -*- coding: utf-8 -*-

import codecs
import os
import random
# 解决中文乱码的问题，utf-8在这里不可行
import sys
reload(sys)
sys.setdefaultencoding('GBK')

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

#将tuple转化为列表
def tuple_to_list(volcaulay_list):
    change_lst = []
    for val in volcaulay_list:
        list(val)
        change_lst.append(list(val))
    return change_lst


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
    sorted_list = tuple_to_list(sorted_dict)#因为生成的是元组列表，报错提示元组没有append，下面会出问题
    return sorted_list#排序使得每一组单词和数目形成了一个单独的元组列表（xx，xx），
                      # 这里又将每一个元组列表转换为一个单独的列表样式的列表[xx,xx]

#4. 计算单词百分比
def rate_words(volcaulay_list,total_count):
    current_count = 0
    for val in volcaulay_list:
        num = val[1]
        current_count = current_count + num
        word_rate = (float(current_count)/total_count) * 100
        val.append(word_rate)

#5. 截取百分比
def cut_words(volcaulay_list,start_and_end):
    cut_list = []
    for val in volcaulay_list:
        if val[2]/100 >= start_and_end[0] and val[2]/100 <= start_and_end[1]:
            cut_list.append(val)
    return cut_list

#6.读取并构造单词释义字典
def read_dict(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    check_dict = {}
    for line in lines:
        line = line.strip()
        words = line.split("  ")#此时words是一个以空格分割了的列表
        check_dict[words[0]] = words[1]
    return check_dict#{'abandon':'v.抛弃，放弃',.....}


#7.查询单词释义
def check_words(word_list,check_dict):
    final_list = []
    final2_list = []
    for word in word_list:#遍历单词表
        if check_dict.has_key(word[0]):
            word.append(check_dict[word[0]])
            final_list.append(word)
        else:
            final2_list.append(word)
    return final_list,final2_list

#8.获取只有单词和释义的单词表
def recall_list(volcaulay_list):
    recall_list = []
    for val in volcaulay_list:
        del val[1]
        del val[1]
        recall_list.append(val)
    return recall_list

#9.设置每日单词数量--顺序版
def set_amount(volcaulay_list,number_words,index):
    set_list = []   
    if index < len(volcaulay_list):
        set_list.append(volcaulay_list[index:index+number_words])     
    return set_list

#设置每日单词数量——乱序版
def random_amount(volcaulay_list,number_words,index2):
    if index2 < len(volcaulay_list):
        set_list = random.sample(volcaulay_list, number_words)
        for val in volcaulay_list:
            if val in set_list:
                del val
    return set_list


#10.自动创建文件目录
def StringListSave(save_path, filename, slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"/"+filename+".txt"#也可以更改成其他形式如csv，记得改动下面的for否则都在一个单元格
    with open(path, "w+") as fp:
        for s in slist:
            for val in s:
                fp.write("%s\t%s\n" % (val[0], val[1]))#因为原列表中是列表中有列表，所以for两次

def StringListSave2(save_path, filename, slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"/"+filename+".txt"#也可以更改成其他形式如csv
    with open(path, "w+") as fp:
        for s in slist:
            fp.write("%s\t%s\n" % (s[0],s[1]))


#6.输出成csv
def print_to_csv(volcaulay_list, to_file_path):
    nfile = open(to_file_path,'w+')
    for val in volcaulay_list:
        if len(val) == 4:
            nfile.write("%s,%s,%0.2f,%s\n" % (val[0], str(val[1]),val[2],val[3]))
        elif len(val) == 3:
            nfile.write("%s,%s,%0.2f\n" % (val[0], str(val[1]),val[2]))
        # else:
        #     nfile.write("%s,%s" % (val[0], val[1]))
    nfile.close()

def main():
    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    #2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个　' %(len(f_words))
    
    #3. 统计单词和排序
    word_list = statictcs_words(f_words)

    #4.计算百分比
    rate_words(word_list,total_word_count)
    #5.截取单词
    start_and_end = [0.5, 0.7] #截取这一部分的单词
    cut_list = cut_words(word_list, start_and_end)

    #6.读取单词释义构造释义字典
    check_dict = read_dict('8000-words.txt')

    #7.查询单词
    final_list,final2_list = check_words(cut_list,check_dict)

    #6. 输出文件
    print_to_csv(final_list, 'output/test.csv')
    print_to_csv(final2_list, 'output/day5-2.csv')

    #输出每日单词文件——顺序版
    i = 1
    index = 1
    number_words = int(raw_input('请输入每天背诵单词数:'))
    global recall_list
    recall_list = recall_list(final_list)
    print len(recall_list)
    save_path = u"每日单词"#创建文件夹
    for i in range(1,int(len(recall_list)/number_words)+2):#这里int就是天数
        filename = str(i)
        set_list = set_amount(recall_list,number_words,index)
        StringListSave(save_path, filename, set_list)
        i += 1
        index = index + number_words

    #输出每日单词文件——乱序版
    index2 = 1#以作区分index2,set_list2等等
    save_path = u"每日单词乱序版"#创建文件夹
    for i in range(1,int(len(recall_list)/number_words)+2):#这里int就是天数
        filename = str(i)
        set_list2 = random_amount(recall_list,number_words,index2)
        StringListSave2(save_path,filename,set_list2)
        i += 1
        index2 = index2 + number_words

if __name__ == "__main__":
    main()
