# coding=utf-8
'''
文件读取
model介绍
r：只读，文件的指针将会放在文件的开头。这是默认模式。
r+：打开一个文件用于读写。文件指针将会放在文件的开头。
w：只写，如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+：打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a：打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。如果要读取文件 需要seek(0)将文件指针放到开头

'''
filename = "file_test.txt"
f = open(filename, "r+")
f.write("第一行代码\n第二行代码")
f.flush()
f.seek(0)
content = f.read()  # 读取所有内容

f.close()
print(content)

'''
print("--------read")
f = open(filename, "r")
content = f.read()  # 读取所有内容
f.close()
print(content)

print("--------readline")
f = open(filename, "r")
line = f.readline()  # 读取一行
f.close()
print(line)

print("--------逐行读取1")
f = open(filename, "r")
line = f.readline()  # 调用文件的 readline()方法，一次读取一行
while line:
    print(line)
    line = f.readline()
f.close()

print("--------逐行读取2")
f = open(filename, "r")
for line in open(filename):
    print(line)
f.close()

print("--------逐行读取3")
f = open(filename, "r")
lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
for line in lines:
    print(line)
f.close()
'''
