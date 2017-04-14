import random

'''
data = []
print(random.random())
randomnum1 = int(random.random() * 1000000)
data.append(randomnum1)
for i in range(1, 200):
    randomnum = int(random.random() * 1000000)
    while randomnum != (lambda x: x for x in data):
        data.append(randomnum)
        break
print(data)
'''


def creat_num(num, long):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    data = []
    for i in range(num):
        a = ''
        for j in range(long):
            a += random.choice(str)
        data.append(a)
    for num in range(len(data)):
        print(data[num])
    return data

if __name__ == '__main__':
    creat_num(200, 9)
