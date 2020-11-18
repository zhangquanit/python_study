# coding=utf-8

print("你好 世界 hello world")
print("第二行代码")

# Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
if True:
    print("true")
else:
    print("false")

# 单行注释
'''
多行注释
多行注释
'''

'''
Python有五个标准的数据类型：
Numbers（数字）：int long（长整型） float（浮点型） complex（复数）
String（字符串）:从左右往右：0...n 从右往左：-1...-n
List（列表）: 列表用[]表示，从左右往右：0...n 从右往左：-1...-n
Tuple（元组): 元组用 () 标识。但是元组不能二次赋值，相当于只读列表。
Dictionary（字典）：字典是无序的对象集合。类似map
'''
print("---------------字符串")
str = 'Hello World!'
print(str)  # 输出完整字符串
print(str[0])  # 输出字符串中的第一个字符   从左到右：0.....n
print(str[-1])  # 倒序输出第一个字符       从右到左：-1....-n
print(str[2:5])  # 输出字符串中第三个至第六个之间的字符串
print(str[2:])  # 输出从第三个字符开始的字符串
print(str[:])  # 输出所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串

# 占位符
print("My name is %s and age is %d kg!" % ('zhangquan', 34))

print("---------------列表")
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[-1])  # 从右往左输出第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表

# 添加元素
list.append("append item")
# 更新元素
list[0] = "update item"
# 删除元素
del list[1]

print(list)

print("---------------元祖")

tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[-1])  # 从右往左输出第一个元素
print(tuple[1:3])  # 输出第二个至第四个（不包含）的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组

print("---------------字典")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 删除字典元素
del dict["one"]
print(dict)



print("---------------运算符")
'''
位运算符
& ：都为True 返回True
| ：一个为True 返回True

逻辑运算符
and ：都为True 返回True
or ：一个为True 返回True
not ：取反 

成员运算符
in : 如果在指定的序列中找到值返回 True，否则返回 False。
not in : 如果不在指定的序列中找到值返回 True，否则返回 False。

身份运算符
is：判断两个标识符是不是引用自一个对象，x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not：

is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。
c = [1, 2]
d = [1, 2]
print(c is d)  # False内存不同
print(c == d)  # True 值相同

'''
a = True
b = False

c = a & b
print(c)

c = a | b
print(c)

c = a and b
print(c)

c = a or b
print(c)

c = not a
print(c)

list = ["a", "b"]
c = "a" in list
print(c)
c = "c" not in list
print(c)

c = "str"
d = "str"
print(c is d)
print(c is not d)

c = [1, 2]
d = [1, 2]
print(c is d)  # False内存不同
print(c == d)  # True 值相同
