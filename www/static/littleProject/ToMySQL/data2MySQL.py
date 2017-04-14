import pymysql
import os
'''
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='ActiveCode', charset='utf8')
cursor = conn.cursor()

cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
'''


def save_code():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='ActiveCode', charset='utf8')
    #  连接数据库MySQL
    cursor = conn.cursor()
    database = list(os.popen('python D:/pygit/www/static/littleProject/ActivationCode/ActiveCode.py'))
    cursor.execute("create table Code (code varchar(20) primary key)")
    #  创建储存code的table--->Code
    for i in range(len(database)):
        cursor.execute("insert into Code (code) values (%s)", [database[i]])
        # 向Code中插入database中生成的随机激活码
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    save_code()
