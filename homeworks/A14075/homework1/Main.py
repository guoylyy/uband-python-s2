# -*- coding: utf-8 -*-

import codecs
import os

# 1.获取文件路径列表
def get_file_from_folder(folder_path):
  paths = []
  for root, dirs, files in os.walk(folder_path): # .walk()遍历文件夹
    for file in files:
      file_path = os.path.join(root, file) # path.join 将目录和文件名组合成路径
      paths.append(file_path)
  if show_details:
    print ("总共",len(paths),"个文件")
  return paths

# 3.分词
## 3.1去除非英文字符
def format_word(text):
    fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '  # 注意空格
    for char in text:
        if char not in fmt:
            text = text.replace(char, ' ')       # 用' '替换文本中的char
    return text.lower()     # Todo: 解决JAVA等大写问题

## 3.2处理单字母
def discard_single(words):
    new_words = []
    for word in words:
        if len(word) > 1:
            new_words.append(word)
    return new_words

## 3.0  text由文件操作传递
def process_words(text):
    text = format_word(text)
    words = text.split(' ')
    words = discard_single(words)
    return words

# 2.文件操作
## 2.2读取单文件 返回单词
def read_file(file_path):
  words = []
  f = codecs.open(file_path, 'r', "utf-8")
  lines = f.readlines()   # .readlines()返回各行组成的list
  for line in lines:
    line = line.strip()   # .strip() 清除行尾'\n'
    if len(line) > 0:     # 本行非空
        words.extend(process_words(line))
  return words

## 2.1读取所有文件 整合所有单词
def read_files(paths):
    world_words = []
    for index,path in enumerate(paths):
        words = read_file(path)
        world_words.extend(words)
    if show_details:
        print ("分词over,总共",len(world_words),'个单词')
    return world_words

# 4.统计词频
def statictics_words(words):
  s_dict = {}
  for word in words:
    if word in s_dict:
      s_dict[word] = s_dict[word] + 1
    else:
      s_dict[word] = 1
  print ("统计词频over.共",len(s_dict.keys()),'个不重复单词')
  return s_dict


## 5.5 转换
def list_to_dict(wlist):
    wdict = {}
    for item in wlist:
        wdict[item[0]] = item[1:]
    return wdict

# 5.排序
def sort_by_value(word_dict):
  item_list = word_dict.items()     # 返回(key,value)的list
  item_list = [[it[1], it[0]] for it in item_list]  # key,value换位
  item_list.sort(reverse=True)  # reverse降序排序
  item_list = [[it[1], it[0]] for it in item_list]  # key,value换位
  item_dict = list_to_dict(item_list)
  return item_dict

# 6.百分比统计
def rate_statistics(items_Dict,total_num,rate_on):
    rate_begin,rate_end = 0, 100
    if rate_on:
        rate_begin , rate_end = rate[0],rate[1]
    final_Dict = {}
    curr_total = 0
    for word,item in items_Dict.items():
        curr_total = curr_total + item[0]
        curr_percent = (float(curr_total) / total_num) * 100
        if curr_percent<rate_begin:
            continue
        if curr_percent>rate_end:
            break
        curr_percent_str = '%0.3f' % (curr_percent)
        final_Dict[word] = [str(item[0]),curr_percent_str,'']  # value:词频-百分比-释义
    if show_details:
        print ('排序over')
    return final_Dict

# 7.筛选词汇
# 7.1
def clear_words(wordDict,clearlist):
    for cword in clearlist:
        if cword in wordDict.keys():
            del wordDict[cword]
    print ('已去除已掌握单词')
    return wordDict

# 7.2 读单文件
def read_clearlist(clear_path):
    clearlist = []
    f = codecs.open(clear_path, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        clearlist.append(line)
    return clearlist

# 7.3 整合多文件
def read_clearlist_from_folder(folder):
    clear_paths = get_file_from_folder(folder)
    clearlists = []
    for clear_path in clear_paths:
        clearlist = read_clearlist(clear_path)
        clearlists.extend(clearlist)
    if show_details:
        print("共有", len(clearlists), '个已掌握单词')
    return clearlists

# 8.添加释义
## 8.1读取词典
def read_dict(dict_path,dicts):
    f = codecs.open(dict_path, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        list = line.split("_____", 1)
        word = list[0]
        value = list[1]
        dicts[word] = value
    return dicts

def read_dicts_from_folder(folder):
    dict_paths = get_file_from_folder(folder)
    dicts = {}
    for dict_path in dict_paths:
        dicts = read_dict(dict_path,dicts)
    print("已获取", len(dicts.keys()), '个单词释义')
    return dicts

# 8.2 添加释义
def add_meaning(final_dict,dicts):
    found_words = {}
    notfound_words = {}
    for word,value in final_dict.items():
        if word in dicts.keys():
            value[2] = dicts[word]
            found_words[word] = value
        else:
            notfound_words[word] = value
    if show_details:
        print ("有释义的单词",len(found_words),'个')
    return found_words,notfound_words

# 9.输出csv
def print_to_csv(word_Dict, filename):
    to_file_path = os.path.join('output', filename)
    nfile = codecs.open(to_file_path,'w+')
    for word, item in word_Dict.items():
        if show_statistics:
            nfile.write("%s,%s,%s,%s\n" % (word,item[0], item[1],item[2]))
        else :
            nfile.write("%s,%s\n" % (word, item[2]))
    nfile.close()
    print ("输出文件",to_file_path)

# 9.2 输出anki导入文件
def print_to_anki(word_Dict, filename):
    to_file_path = os.path.join('output', filename)
    nfile = codecs.open(to_file_path,'w+','utf-8')
    for word, item in word_Dict.items():
        nfile.write("%s\t%s\r\n" % (word, item[2]))
    nfile.close()
    print ("输出文件",to_file_path)

def main():
    # words = read_file('data1/dt01.txt')
    file_path = get_file_from_folder('text') #1.获取文件路径列表

    words = read_files(file_path) #2.3.读取文件并分词

    total_num = len(words)
    word_dict = statictics_words(words)   #4.统计词频

    word_dict = sort_by_value(word_dict) #5.排序


    word_dict = rate_statistics(word_dict,total_num, rate_on)
    if show_details:
        print_to_csv(word_dict, 'before_clear.csv')  #6.百分比统计  True-按百分比

    clearlists = read_clearlist_from_folder('clear_lists')
    word_dict = clear_words(word_dict,clearlists)
    if show_details:
        print_to_csv(word_dict, 'after_clear.csv')  # 7. 筛选已掌握单词

    Real_dicts = read_dicts_from_folder('buildin_dicts')    #8.1读取词典
    found_words, notfound_words = add_meaning(word_dict,Real_dicts) # 8.2 生成单词释义

    print_to_csv(found_words, 'found.csv')
    print_to_csv(notfound_words, 'notfound.csv') # 9.输出至文档

    print_to_anki(found_words,'anki.txt')   #9.2输出anki导入文件

if __name__ == "__main__":
    # 将需修改的参数放至此处 方便修改
    show_details = True # 显示调试信息
    rate_on = False  # 筛选百分比开关
    rate = [50,70]  # 百分比始末
    show_statistics = True  # 显示词频&百分比
    eachday_recite_num = 20 # 每天背单词数
    main()
