import re
import os


def search_code(dir_path):
    if not os.path.isdir(dir_path):
        print('please check file directory name!')
    exp_re = re.compile(r'^#.*')
    filelist = os.listdir(dir_path)
    for file in filelist:
        filePath = os.path.join(dir_path, file)
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.py':
            with open(filePath, encoding='UTF-8') as f:
                # encoding='UTF-8',很关键！！！指定将unicode字符转换成'UTF-8'字节编码
                all_lines = 0
                space_lines = 0
                exp_lines = 0
                for line in f.readlines():
                    all_lines += 1
                    if line.strip() == '':
                        space_lines += 1
                        continue
                    exp = exp_re.findall(line.strip())
                    if exp:
                        exp_lines += 1
            print("%s\t%s\t%s\t%s" % (file, all_lines, space_lines, exp_lines))


if __name__ == '__main__':
    search_code('D:\Python')

'''

code_path = os.path.join(os.path.dirname(__file__), '..')

code_files = []
code_line_count = 0
code_blank_line_count = 0
code_comment_line_count = 0


def walk(rootDir):
    global code_files
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            walk(path)
        else:
            if os.path.splitext(lists)[1] == '.py':
                code_files.append(path)

walk(code_path)

for code_file in code_files:
    file = open(code_file)
    for line in file:
        code_line_count += 1
        if line == '\n':
            code_blank_line_count += 1
        if line.replace(' ', '').replace('\t', '')[0] == '#':
            code_comment_line_count += 1

print ('文件数量：', len(code_files))
print ('代码行数：', code_line_count)
print ('空行行数：', code_blank_line_count)
print ('注释行数:', code_comment_line_count)
'''