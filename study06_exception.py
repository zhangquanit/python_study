# coding=utf-8
'''
异常
BaseException	所有异常的基类
Exception	常规错误的基类
1、捕获异常
捕捉异常可以使用try/except语句
2、try-finally 语句
出现异常，会执行finally，但是没有except，会抛出异常
3、try-except-finally
出现异常，except会拦截异常，最后执行finally

4、异常的参数
一个异常可以带上参数，可作为输出的异常信息参数。
try:
    正常逻辑
except Exception as err:
    处理异常err
else:
    其余代码

5、抛出异常
使用raise语句自己触发异常，类似java的 thorw
try:
    a = 1
    if a == 1:
        raise Exception("a==1 excpetion")  # 抛出异常
except Exception as err:
    print(err)
'''

# 捕获异常
print("----------try except else---------")
try:
    f = open("file_test.txt", "r")
    f.write("不能写入文件")
    print("执行完毕")
except Exception:
    print("发生异常了")
except BaseException:
    print("类似java，可以多次捕获异常，按照从子类到父类的顺序")
else:
    print("执行成功")

# print("----------try finally---------")
# try:
#     f = open("file_test.txt", "r")
#     f.write("不能写入文件")
#     print("执行完毕")
# finally:
#     print("执行finally")

print("----------try except finally---------")
try:
    f = open("file_test.txt", "r")
    f.write("不能写入文件")
    print("执行完毕")
except Exception:
    print("发生异常了")
finally:
    print("执行finally")

print("----------异常参数---------")
try:
    f = open("file_test.txt", "r")
    f.write("不能写入文件")
    print("执行完毕")
except Exception as err:
    print("发生异常")
    print(err)

print("----------抛出异常---------")
try:
    a = 1
    if a == 1:
        raise Exception("a==1 excpetion")  # 抛出异常
except Exception as err:
    print(err)


print("----------自定义异常---------")
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print(e)
