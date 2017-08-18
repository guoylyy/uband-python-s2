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
def print_to_csv(vocabulary_list, to_file_path):
    nfile = open(to_file_path,'w+')
    for val in vocabulary_list:
        if len(val) == 4:
            nfile.write("%s,%s,%0.2f,%s \n" % (val[0], str(val[1]), val[2], val[3]))
        elif len(val) == 3:
            nfile.write("%s,%s,%0.2f\n" % (val[0], str(val[1]), val[2]))
        elif len(val) == 2:
            nfile.write("%s,%s\n" % (val[0], val[1]))
    nfile.close()

#将内含元组转换为列表
def tup_to_list(word_list):
    dict_lst = []
    for tup in word_list:
        lst = list(tup) #将元组转换为列表
        dict_lst.append(lst)
    return dict_lst

#获取百分比列表
def word_percentage(word_lst, total_count):
    word_percentage_list = []
    current_count = 0
    for val in word_lst:
        num = val[1]
        current_count = current_count + num
        word_percent = (float(current_count)/total_count) * 100
        val.append(word_percent) #添加百分比
        word_percentage_list.append(val)
    return word_percentage_list

#截取百分比
def extract_percent(word_percent_lst, start_and_end):
    extract_percent_list = []
    for val in word_percent_lst:
        percentage = val[2]/100
        if percentage >= start_and_end[0] and percentage <= start_and_end[1]:
            extract_percent_list.append(val)
    return extract_percent_list

#获取释义词典
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

#添加单词释义
def add_meaning(word_percent_lst2, dict_origin):
    words_meaning_list = []
    for val in word_percent_lst2:
        word = val[0]
        # print word
        if dict_origin.has_key(word):
            meaning = dict_origin[word]
        else:
            meaning = 'no meaning'
        val.append(meaning)
        words_meaning_list.append(val)      
    return words_meaning_list

# 判断词表是否有序
def generate_words(word_num, word_list_1, average_amount, is_random):
    day_num_abount = word_num % average_amount
    day_num = word_num / average_amount
    if day_num_abount == 0:
        day_num = day_num
    else:
        day_num = day_num + 1
    if is_random:
        get_everyday_word_list = word_list_1
    else:
        word_list_1.sort()
        get_everyday_word_list = word_list_1
    return get_everyday_word_list,day_num

def main():
    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    #2. 清洗文本
    f_words = format_words(words)
    total_count = len(f_words)
    print ' 获取了已经格式化的单词 %d 个' %(len(f_words))
    
    #3. 统计单词和排序
    word_list = statictcs_words(f_words) #获得列表内置元组
    # print word_list
    word_lst = tup_to_list(word_list)
    # print word_lst
    word_percent_lst = word_percentage(word_lst, total_count)
    start_and_end = [0.5, 0.7] #截取这一部分的单词
    word_percent_lst2 = extract_percent(word_percent_lst, start_and_end)
    print_to_csv(word_percent_lst2, 'output/test_day04.csv')
    # print word_percent_lst
    dict_origin = read_dict('8000-words.txt')
    word_meaning_lst = add_meaning(word_percent_lst2, dict_origin)
    # print word_meaning_lst
    #4. 输出文件
    print_to_csv(word_meaning_lst, 'output/test_day05.csv')
    # 每日背单词设置
    average_amount = 50
    is_random = False
    word_num = len(word_meaning_lst)
    print ' 需要背诵的单词 %s 个' % (word_num)
    get_everyday_word_list, day_num = generate_words(word_num, word_meaning_lst, average_amount, is_random)
    for day in range(0,day_num):
        word_range = get_everyday_word_list[(day * average_amount):((day+1) * average_amount)]
        current_word_list = word_range
        if day <= day_num:
            file_name = 'output/day' + str(day + 1) + '.csv'
            print_to_csv(current_word_list,file_name)

if __name__ == "__main__":
    main()