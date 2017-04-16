#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re


def find_link(file):
    with open(file, encoding='UTF-8') as f:
        Soup = BeautifulSoup(f.read(), 'html.parser')
        if Soup.find_all('link'):
            for link in Soup.find_all('link' or 'a'):
                print(link.get('href'))

if __name__ == '__main__':
    find_link('D:\pygit\www\static\littleProject\htmlAnalysis/testHTML.html')

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

url = 'http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html'
data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')
link = soup.findAll('a')
for u in link:
    print(u.get('href'))