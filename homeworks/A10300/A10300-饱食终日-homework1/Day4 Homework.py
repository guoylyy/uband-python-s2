# -*- coding: utf-8 -*-

import codecs
import os

# 1. read source file
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
    f = codecs.open(file_path, 'r', "utf-8")  # open file
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ")  # space split
        words = word_split(words)  # -split
        word_list.extend(words)
    return word_list


def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


# read words from txts
def read_files(file_paths):
    final_words = []
    for path in file_paths:
        final_words.extend(read_file(path))
    return final_words


# 2.format&obtain word
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


# 3. count words
# {'aa':4, 'bb':1}
def statictcs_words(words):
    s_word_dict = {}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    # word ranking
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict


# 4.export csv
def print_to_csv(volcaulay_list, to_file_path, total_count):
    nfile = open(to_file_path, 'w+')
    current_count = 0
    for val in volcaulay_list:
        num = val[1]
        current_count = current_count + num
        word_rate = (float(current_count) / total_count) * 100
        nfile.write("%s,%s,%0.2f\n" % (val[0], str(val[1]), word_rate))
    nfile.close()


def main():
    # 1. read files
    words = read_files(get_file_from_folder('data1'))
    print '获取未格式化的单词 %d 个' % (len(words))

    # 2. format file
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已格式化的单词 %d 个' % (len(f_words))

    # 3. count word&ranking
    word_list = statictcs_words(f_words)

    start_and_end = [0.5, 0.7]  # extract words

    # 4. file export
    print_to_csv(word_list, 'output/test.csv', total_word_count)


if __name__ == "__main__":
    main()

