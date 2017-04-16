#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
def html_body(file):
    with open(file, encoding='UTF-8') as f:
        re_body = re.compile(r'<li>.*</li>')
        if re_body.match(f.read()):
            print('ok')
            return re_body.match(f.read())

if __name__ == '__main__':
    print(html_body('D:\pygit\www\static\littleProject\htmlAnalysis/testHTML.html'))



class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>', tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_entityref(self, name):
        print('&%s' % name)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_charref(self, name):
        print('&#%s' % name)

parser = MyHTMLParser()


def html_body(file):
    with open(file, encoding='UTF-8') as f:
        parser.feed(f.read())

if __name__ == '__main__':
    print(html_body('D:\pygit\www\static\littleProject\htmlAnalysis/testHTML.html'))
'''

import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958' \
      'f449949df42a6d3a2e542c000/001432688314740a0aed473a39f47b09c8c7274c9ab6aee000'
data = requests.get(url)
r = re.findall(r'<body>[\s\S]*</body>', data.text)
print(r[0])

print('-----------------------------------------------------------------------------------')
soup = BeautifulSoup(data.text, 'html.parser')
print(soup.get_text())

r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})
# 带参数的GET请求
print(r.url)
print(r.text)


def html_body(file):
    with open(file, encoding='UTF-8') as f:
        Soup = BeautifulSoup(f.read(), 'html.parser')
        return Soup.get_text()

if __name__ == '__main__':
    print(html_body('D:\pygit\www\static\littleProject\htmlAnalysis/testHTML.html'))





