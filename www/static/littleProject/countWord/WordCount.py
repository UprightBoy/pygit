import re

with open('D:\pygit\www\static\littleProject\countWord/EnglishExample.txt', 'r') as f:
    str = f.read()
    reobj = re.compile('\w?')
    words = reobj.findall(str)  # 为什么尾部会自动加入一个空的''？？
    words.pop()
    wordDict = dict()

    for word in words:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    print(wordDict)

    for key, value in wordDict.items():
        print('%s:%s' % (key, value))
