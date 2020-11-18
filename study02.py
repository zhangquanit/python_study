# coding=utf-8

print("----------if条件")
'''
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
    
a = 1  # 0表示False 非0表示True
if a:
    print(True)
else:
    print(False)
        
'''

num = 9
if num == 9: print("if简单语句")

num = 8
# 判断值是否在0~5或者10~15之间
if (0 <= num <= 5) or (8 <= num <= 10):
    print('多表达式组件的条件')
else:
    print("--")

a = 1  # 0表示False 非0表示True
if a:
    print(True)
else:
    print(False)

'''
while
while ..else
'''
print("----------while循环语句")
count = 1
while count < 5:
    print(count)
    count += 1

while count < 5:
    print(count)
    count += 1
else:
    print("count>=5")

'''
for item in sequence:
    statement
    
通过序列索引迭代
for index in range():
    statement    
'''
print("----------for循环语句")
list = [1, 2]
for a in list:
    print(a)

str = "ab"
for letter in str:
    print(letter)

print("通过序列索引迭代")
for index in range(len(str)):
    print(str[index])

list = [1, 2]
list2 = list[:]  # 相当于拷贝一份list，值相同，内存地址不同
print(list2)
print(list == list2)
print(list is list2)
