import re
import os

# 找出txt文档中出现频率最高的英文单词


def searchWord(DirPath):
    if not os.path.isdir(DirPath):
        print('please check file directory name!')
    filelist = os.listdir(DirPath)
    print(filelist)
    re0bj = re.compile(r'\w+\s+')
    for file in filelist:
        filePath = os.path.join(DirPath, file)
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.txt':
            with open(filePath) as f:
                data = f.read()
                words = re0bj.findall(data)
                wordDict = dict()
                for word in words:
                    word = word.lower()
                    if word in ['a', 'the', 'to']:
                        continue
                    if word in wordDict:
                        wordDict[word] += 1
                    else:
                        wordDict[word] = 1
                ansList = sorted(wordDict.items(), key=lambda t: t[1], reverse=True)
                print('file: %s-->the most word:%s' % (file, ansList[0]))

if __name__ == '__main__':
    searchWord('D:\pygit\www\static\littleProject\SearchImportantWord\Diary')
