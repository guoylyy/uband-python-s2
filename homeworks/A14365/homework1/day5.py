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
    f = codecs.open(file_path, 'r') #打开文件
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


#2. 获取格式化之后的单词
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
    s_word_dict = {}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    #排序
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict


#4. 计算单词累计百分比
def word_rating(vocabulary_list, total_count):
    current_count = 0
    rate_list = [] # new list for word frequency + rate
    for val in vocabulary_list:
        num = val[1] # word frequency
        current_count += num
        word_rate = (float(current_count) / total_count) * 100 # accumulated percentage
        rate_tuple = (val[0], val[1], word_rate)
        rate_list.append(rate_tuple)
    return rate_list


#5. 截取百分比内的单词
def in_section_words(rate_list, rate_section):  # get words within given rate section
    final_list = [] # new list for words within given rate section
    for val in rate_list:
        if val[2] >= 100 * rate_section[0] and val[2] <= 100 * rate_section[1]: 
            rate_tuple = (val[0], val[1], val[2])
            final_list.append(rate_tuple)
    return final_list

#6. 获取释义
def get_explanation(file_path, current_list):
    f = codecs.open(file_path, 'r') #打开文件
    lines = f.readlines()
    word_dic = {}
    for line in lines:
        line = line.strip()
        line = line.replace(']', ' ') ### BUG KILLER ### very important!!!!!!
        words = line.split("   ") #用空格分割
        # words = word_split(words) #用-分割  # not necessary
        word_dic[words[0]] = words[1]
    fi_final_list = []
    for val in current_list:
        if word_dic.has_key(val[0]):
            word_tuple = (val[0], val[1], val[2], word_dic[val[0]])
        else:
            word_tuple = (val[0], val[1], val[2], '#暂无释义#')
        fi_final_list.append(word_tuple)
    return fi_final_list

#7. 输出成csv
def print_to_csv(final_list, to_file_path):
    nfile = open(to_file_path,'w+')
    for val in final_list:
        nfile.write("%s, %s, %0.2f%%, %s\n" % (val[0], str(val[1]), val[2], val[3]))
    nfile.close()

#4'. 输出成csv
def print_to_csv2(word_list, to_file_path):
    nfile = open(to_file_path,'w+')
    for val in word_list:
        nfile.write("%s, %s\n" % (val[0], str(val[1])))

def main():
    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % len(words)

    #2. 清洗文本
    f_words = format_words(words)
    print '获取了已经格式化的单词 %d 个 ' % len(f_words)
    total_word_count = len(f_words)

    #3. 统计单词和排序
    word_list = statistics_words(f_words)
    print '最终总单词数 %d 个 ' % len(word_list)

    # 是否进行百分比统计
    rating = True # True for rating, False for not rating
    if rating:
        #4. 计算单词累计百分比
        rate_list = word_rating(word_list, total_word_count) # inherit rate_list from word_rating()

        #5. 截取百分比内的单词
        start_and_end = [0.5, 0.7] #截取这一部分的单词
        final_list = in_section_words(rate_list, start_and_end)

        import sys  ### to solve UnicodeEncodeError
        reload(sys)
        sys.setdefaultencoding('utf-8') ###

        #6. 获取释义
        fi_final_list = get_explanation('8000-words.txt', final_list)
        print '生成单词表，应背单词 %d 个' % len(fi_final_list)

        #7. 输出文件
        print_to_csv(fi_final_list, 'output/with_meaning.csv')

    else: # not rating
        #4'. 输出文件
        print_to_csv2(word_list, 'output/all_words.csv')

if __name__ == "__main__":
    main()
