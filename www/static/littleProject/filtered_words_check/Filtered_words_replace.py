#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

'''
def filtered_words_replace(file):
    inputwords = input('please type in word:')
    with open(file, 'r', encoding='UTF-8') as f:
        for words in f.readlines():
            W = re.match(r"(.*)"+words.strip()+r"(.*)", inputwords)
            if W:
                return W.group(0).replace(words.strip(), '**')
        return inputwords

if __name__ == '__main__':
    print(filtered_words_replace('D:\pygit\www\static\littleProject/filtered_words_check/filtered_words.txt'))
'''

word_filter = set()
with open('D:\pygit\www\static\littleProject/filtered_words_check/filtered_words.txt','r' ,encoding='UTF-8') as f:
    for w in f.readlines():
        word_filter.add(w.strip())

while True:
    s = input()
    if s == 'exit':
        break
    for w in word_filter:
        if w in s:
            s = s.replace(w, '*'*len(w))
    print(s)
