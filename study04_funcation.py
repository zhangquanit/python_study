# coding=utf-8
'''
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

语法：
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''


def printme(str):
    print(str)


def add(a, b):
    return a + b


printme("hello world")
print(add(1, 2))

'''
参数传递
不可变类型：strings, tuples(元祖), 和 numbers 是不可更改的对象
可变类型： list,dict 等则是可以修改的对象。
'''


def change(a):  # 传不可变对象实例
    a = 11


a = 10
change(a)
print(a)  # 还是10  number类型都是不可变对象


def change(list):  # 传可变对象实例
    list.append(3)


list = [1, 2]
change(list)
print(list)  # [1,2,3]

'''
以下是调用函数时可使用的正式参数类型：
必备参数
默认参数
不定长参数:  *args
'''


def println(str):  # 必备参数
    print(str)


def println(str, num=10):  # 默认参数
    print(str)


println("str")
println("str", 10)


def method(str, *args):  # 可变参数
    for item in args:
        print(item)


method("a", "b", "c")

'''
变量作用域
局部变量：定义在函数内部的变量拥有一个局部作用域，
全局变量：定义在函数外的拥有全局作用域。

1、在函数中使用global，将临时变量改变为全局变量
x = 1
def test():
    global x
    x = 2
    print(x)

test()    #2
print(x)    #2

2、函数里面的变量不影响外边，而且函数不能调用外边的变量，相当于两个变量
x = 1
def test():
    x = 2 #虽然变量名相同，但是属于不同的变量，不会改变外部变量的值
    print(x)

test()    #2
print(x)    #1

3、在函数外边声明的变量，在函数里边是不能直接用的，他们属于两个不同的变量
x = 1
def test():
    print(x)    #Error  不能直接访问外部变量
    x = 2
    print(x)

test()
print(x)
'''

