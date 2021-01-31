# -*- coding: utf-8 -*-

import codecs
import os

# 1.读取new_dicts文件夹 找到新词典
def get_file_from_folder():
  dict_names = []
  for root, dirs, files in os.walk('new_dicts'):
    for file in files:
      dict_names.append(file)
  return dict_names

# 2.1截取至第一个非空格字符
def get_alph(text):
    for index,char in enumerate(text):
        if char != ' ':
            text = text[index:]
            break
    return text

# 2.读取新词典
def get_dict(filename):
    dict_path = os.path.join('new_dicts', filename)
    dicts = {}
    f = codecs.open(dict_path, 'r', 'utf-8')
    lines = f.readlines()
    for line in lines:  # Todo:不同字典文件 分法不同
        try:
            line = line.strip()
            line = line.replace("，",' ')    #防止输出excel时的bug
            #line = get_alph(line)
            list = line.split("\t",1)
            word = list[0]
            #value = get_alph(list[1])
            value = list[1]
            if len(word)<2 or len(value) <2 :
                continue
            dicts[word] = value
        except:
            print (filename,"本行读取错误:",line)
    f.close()
    print ("已读取",filename)
    return dicts

# 2.2删除词典
def delete_dict(filename):
    dict_path = os.path.join('new_dicts', filename)
    if Delete_On:
        try:
            os.remove(dict_path)
        except:
            print ("删除失败",filename)

# 3.输出新词典
def generate_dicts(filename,dicts):
    save_path = os.path.join('buildin_dicts', filename)
    nfile = open(save_path,'w+')
    for key,value in dicts.items():
        try:
            nfile.write("%s_____%s\n" % (key,value))    #用_____分隔
        except:
            print ('写入失败',key,value)
    nfile.close()
    print ("已生成",filename)

def main():
    dict_names = get_file_from_folder()
    for dict_file in dict_names:
        dicts = get_dict(dict_file)
        delete_dict(dict_file)
        generate_dicts(dict_file,dicts)

# 测试生成的词典
def test(dict_path):
    dicts = {}
    f = codecs.open(dict_path, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        list = line.split("_____", 1)
        word = list[0]
        value = list[1]
        dicts[word] = value
    print("已获取", len(dicts.keys()), '个单词释义')
    return dicts


if __name__ == '__main__':
    Delete_On = False # 读取后自动删除
    main()
    #test('buildin_dicts\\liuji.txt')