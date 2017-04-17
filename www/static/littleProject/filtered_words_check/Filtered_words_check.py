#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def filtered_words_check(file):
    inputwords = input('please type in word:')
    with open(file, 'r', encoding='UTF-8') as f:
        for words in f.readlines():
            if re.match('.*'+words.strip()+'.*', inputwords):
                return 'Human Rights'
        return 'Freedom'

if __name__ == '__main__':
    print(filtered_words_check('D:\pygit\www\static\littleProject/filtered_words_check/filtered_words.txt'))
