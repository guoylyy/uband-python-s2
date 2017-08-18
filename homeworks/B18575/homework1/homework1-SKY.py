# -*- coding: utf-8 -*-
import codecs
import os
import sys
import random
reload(sys)
sys.setdefaultencoding( "utf-8" )

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

# 3.2、为单词添加所占比例
def add_rate(volcaulay_list,total_count):
    current_count=0
    word_add_rate=[]
    for val in volcaulay_list:
        tem=[]
        num=val[1]
        current_count = current_count + num
        word_rate = (float(current_count) / total_count) * 100
        tem.append(val)
        tem.append(word_rate)
        word_add_rate.append(tem)
    return word_add_rate

# 3.3 截取固定比例
def intercept_word(word_list,start_and_end):
    intercepted_word=[]
    for val in word_list:
        if val[1] > start_and_end[0]:
            if val[1] < start_and_end[1]:
                intercepted_word.append(val)
    return intercepted_word

# 3.4.1 获取单词释义数据
def getMean(file_path):
    fp = codecs.open(file_path, 'r', 'utf-8')
    lines = fp.readlines()
    final_word = {}
    for line in lines:
        line = line.strip()
        word = line.split("   ")
        final_word[word[0]] = word[1]
    return final_word

# 3.4.2 为截取单词添加释义
def word_and_mean(word_list,mean_map):
    for val in word_list:
        if mean_map.has_key(val[0][0]):
            val.append(mean_map[val[0][0]])
        elif mean_map.has_key(val[0][0].replace('s','')):
            val.append(mean_map[val[0][0].replace('s','')])
        elif mean_map.has_key(val[0][0].replace('es','')):
            val.append(mean_map[val[0][0].replace('es','')])
        elif mean_map.has_key(val[0][0].replace('ed','')):
            val.append(mean_map[val[0][0].replace('ed','')])
        else:
            val.append("暂无释义")
    # print word_list
    return word_list
# 3.5 获取每日单词
def get_day_word(mean_list,day_num,now_day,mode):
    day_word=[]
    if mode:
        for index,val in enumerate(mean_list):
            day_word.append(mean_list[index+day_num*(now_day-1)])
            if len(day_word)>=day_num:
                break
    else:
        day_word=random.sample(mean_list, day_num)
        for val in day_word:
            mean_list.remove(val)
    return day_word



#4.输出成csv
def print_to_csv(volcaulay_list, to_file_path):
    nfile =codecs.open(to_file_path,'w+','utf-8')
    nfile.write(codecs.BOM_UTF8)
    for val in volcaulay_list:
        nfile.write("%s,%s,%0.2f,%s\n" % (val[0][0], str(val[0][1]),val[1],val[2]))
    nfile.close()



def main():

    #设置是否截取单词
    is_intercept=True

    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    #2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' %(len(f_words))
    
    #3. 统计单词和排序
    word_list = statictcs_words(f_words)

    # 3.2为单词添加所占比例
    word_list_rate = add_rate(word_list, total_word_count)

    # 3.3 截取固定比例
    start_and_end = [50, 70] #截取这一部分的单词
    if is_intercept:
        intercepted_list=intercept_word(word_list_rate,start_and_end)
    else:
        intercepted_list=word_list_rate

    # 3.4 为单词添加释义
    #获取释义数据
    mean_map=getMean("./8000-words.txt")
    #添加释义
    mean_list=word_and_mean(intercepted_list,mean_map)

    # 3 5 获取每日单词
    # 每日单词数量
    day_num=50
    now_day=3
    mode=False  #获取单词模式，TRUE为顺序，FALSE为乱序
    day_word_list=get_day_word(mean_list,day_num,now_day,mode)

    #4. 输出文件。输出带释义的文件
    # print_to_csv(mean_list, 'output/test4.csv')

    # 4.1 输出每日文件
    print_to_csv(day_word_list, 'output/'+str(now_day)+'.csv')



if __name__ == "__main__":
    main()