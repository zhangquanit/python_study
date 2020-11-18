# coding=utf-8
'''
面向对象
1、类和实例

2、类的继承
class 子类(基类1,基类2,....)
issubclass(sub,parent)
isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。

单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

'''


class Employee:
    'doc描述，所有员工的基类'
    empCount = 0  # 它的值将在这个类的所有实例之间共享。

    # __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # __del__在对象销毁的时候被调用,即调用 del 对象时，会调用__del__
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name + "销毁")

    # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
    def displayCount(self):
        print("Total Employee: %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def printSelf(self):
        print(self)
        print(self.__class__)


def test():
    employee = Employee("张三", 1000)
    employee.displayCount()
    employee.displayEmployee()
    print(employee)

    print("---------------")
    employee = Employee("李四", 1000)
    employee.displayCount()
    employee.displayEmployee()
    employee.printSelf()

    print("-------动态添加属性--------")
    employee.age = 100
    print(employee.age)
    del employee.age  # 删除属性

    print("-------属性操作方法--------")
    setattr(employee, 'age', 8)  # 添加属性 'age' 值为 8
    has_age = hasattr(employee, 'age')  # 如果存在 'age' 属性返回 True。
    age_value = getattr(employee, 'age')  # 返回 'age' 属性的值
    delattr(employee, 'age')  # 删除属性 'age'

    print(has_age)
    print(age_value)

    print("-------内置类属性--------")
    print("Employee.__doc__: %s" % Employee.__doc__)
    print("Employee.__name__: %s" % Employee.__name__)
    print("Employee.__module__：%s:" % Employee.__module__)
    print("Employee.__bases__: %s" % Employee.__bases__)
    print("Employee.__dict__: %s" % Employee.__dict__)


'''
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''

test()

print("=======================类的继承===========")


class Parent:  # 定义父类
    parentAttr = 100  # 公共属性 所有实例共享
    __private_attrs = 100  # 两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

    def __init__(self):
        print("调用父类构造函数")

    def __private_method(self):  # 两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods
        print("私有方法")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr
        self.__private_attrs = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)
        print("私有属性 :", self.__private_attrs)

    def overideMethod(self):
        print("父类中的 overideMethod")


class Child(Parent):  # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')

    # 方法的重写
    def overideMethod(self):
        print("重写父类的overideMethod方法")


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值

# 测试公共变量和私有变量
c2 = Child()
c2.getAttr()

# 调用重写的方法
c.overideMethod()

issub = issubclass(Child, Parent)
is_child = isinstance(c, Child)
is_parent = isinstance(c, Parent)
print("Child issubclass Parent: %s" % issub)
print("c isinstance Child: %s" % is_child)
print("c isinstance Parent: %s" % is_parent)
