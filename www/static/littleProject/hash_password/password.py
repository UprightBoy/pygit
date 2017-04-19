#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
from collections import defaultdict

db = {}
db = defaultdict(lambda: 'N/P')


def get_md5(password):
    a = hashlib.md5()
    a.update(password.encode('utf-8'))
    return a.hexdigest()


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


def login(username, password):
    b = get_md5(password + username + 'the-Salt')
    if b == db[username]:
        return True
    else:
        return False

name = input('注册输入用户名:')
password = input('注册输入密码:')
register(name, password)
login_name = input('登录输入用户名:')
login_password = input('登录输入密码:')
print(login(login_name, login_password))
