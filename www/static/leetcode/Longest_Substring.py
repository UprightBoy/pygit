#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def lengthOfLongestSubstring(s):
    start = maxLength = 0
    usedchar = {}

    for i in range(len(s)):
        if s[i] in usedchar and start <= usedchar[s[i]]:
            start = usedchar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
        usedchar[s[i]] = i
    return maxLength

print(lengthOfLongestSubstring('qwerqwerty'))