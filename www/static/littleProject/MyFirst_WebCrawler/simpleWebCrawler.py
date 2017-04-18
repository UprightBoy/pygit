#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/2166231880'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
img_urls = soup.findAll('img', changedsize="true")
for img_url in img_urls:
    img_src = img_url['src']
    with open('D:\pygit\www\static\littleProject\MyFirst_WebCrawler/Crawler_img/'+os.path.split(img_src)[1], 'wb') as f:
        f.write(requests.get(img_src).content)

