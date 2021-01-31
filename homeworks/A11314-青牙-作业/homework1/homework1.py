# -*- coding: utf-8 -*-

import codecs
import os,sys,random
reload(sys)
sys.setdefaultencoding('utf-8')


# 1. 读取文件
# ['aa', 'aaa-bbb-sds'] => ['aa', 'aaa', 'bbb', 'sds']
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
    f = codecs.open(file_path, 'r', "utf-8")  # 打开文件
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ")  # 用空格分割
        words = word_split(words)  # 用-分割
        word_list.extend(words)
    return word_list


def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


# 读取多文件里的单词
def read_files(file_paths):
    final_words = []
    for path in file_paths:
        final_words.extend(read_file(path))
    return final_words


# 2.获取格式化之后的单词
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


# 3. 统计单词数目
# {'aa':4, 'bb':1}
def statictcs_words(words):
    s_word_dict = {}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    # 排序
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict


# 4.输出成csv
def print_to_csv(volcaulay_list, to_file_path):
    nfile = open(to_file_path, 'w+')
    for val in volcaulay_list:
        s = ''
        for i in xrange(0, len(val)):
            if i == 0:
                s = val[i]
            else:
                s = s + ',' + str(val[i])
        nfile.write(s + "\n")
    nfile.close()


# 统计单词所占百分比
def words_rate(word_list, total_num):
    word_list_rate = []
    current=0
    for word in word_list:
        num = word[1]
        current=current+num
        word_rate = float('%.2f' % ((float(current) / total_num) * 100))
        word_list_rate.append([word[0], current, word_rate])
    return word_list_rate

# 输出固定词频的单词
def words_list_split(word_list_rate, start_and_end):
    word_list_split = []
    for val in word_list_rate:
        num = val[2]
        if num/100 < start_and_end[1] and num/100 > start_and_end[0]:
            word_list_split.append(val)
    return word_list_split


# 构造单词释义字典
def dict(file_name):
    fi=codecs.open(file_name, 'r', "utf-8")  # 打开文件
    lines = fi.readlines()
    dict_word={}
    for line in lines:
        line=line.strip()
        word_ex=line.split()
        word_mean=word_ex[1]
        word_mean=word_mean.replace(',','，')
        dict_word[word_ex[0]]=word_mean
    return dict_word

#构造单词字典
def word_ex_list(words_list,dict_word):
    word_ex=[]
    word_no_ex=[]
    for val in words_list:
        if dict_word.has_key(val[0]):
            word_ex.append([val[0],str(val[1]),str(val[2]),dict_word[val[0]]])
        else:
            word_no_ex.append([val[0],str(val[1]),str(val[2])])
    return word_ex,word_no_ex

#生成顺序每日单词列表
def req_wordex_list(word_list,num):

    if len(word_list) % num > 0:
        days = int(len(word_list) / num) + 1
    else:
        days = int(len(word_list)/ num)
    word_req_list = [[] for i in range(days)]
    i=0
    for index,item in  enumerate(word_list):

        word_req_list[i].append(item)
        if index%50 ==49:
            i=i+1
    return word_req_list

#生成乱序的每日单词表
def noreq_wordex_list(word_list,num):
    if len(word_list) % num > 0:
        days = int(len(word_list) / num) + 1
    else:
        days = int(len(word_list)/ num)
    word_noreq_list = [[] for i in range(days)]
    for i in range(days-1):
        for j in range(50):
            x=random.randint(0,len(word_list)-1)
            word=word_list[x]
            word_noreq_list[i].append(word)
            word_list.remove(word)
    word_noreq_list[days-1].extend(word_list)

    return word_noreq_list



def main():
    # 是否输出固定词频的单词表
    fix_frequency = True
    start_and_end = [0.5, 0.7]  # 截取这一部分的单词

    # 1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    # 2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' % (len(f_words))

    # 3. 统计单词和排序
    word_list = statictcs_words(f_words)

    # 固定词频的文件\
    word_list_rate = words_rate(word_list, len(f_words))
    if fix_frequency:
        word_list_split = words_list_split(word_list_rate, start_and_end)
        word_list_freq=word_list_split
    else:
        word_list_freq=word_list_rate
    #有翻译的文件盒没有翻译的文件
    word_translate,word_no_translate=word_ex_list(word_list_split,dict("8000-words.txt"))

    #设置每天的背单词数
    recite_num_day=50
    req_or_no=True
    if req_or_no:
        recite_words=req_wordex_list(word_translate,recite_num_day)
    else:
        recite_words=noreq_wordex_list(word_no_translate,recite_num_day)

    for index,item in enumerate(recite_words):
        print_to_csv(item,'output/'+str(index+1)+'.csv')

if __name__ == "__main__":
    main()