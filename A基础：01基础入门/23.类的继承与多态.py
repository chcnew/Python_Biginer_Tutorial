# coding: utf-8

class Animal(object):
    """docstring for Animal"""

    def __init__(self, color):
        self.color = color

    def eat(self):
        print(self.color, '的动物在吃！')

    def run(self):
        print(self.color, '的动物在跑！')


class Dog(Animal):  # 继承于Animal类
    """docstring for Dog"""

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print(self.name, '在啃骨头！')


class Cat(Animal):  # 继承于Animal类
    """docstring for Cat"""

    def __init__(self, name, age, color):
        super(Cat, self).__init__(color)  # 调用父类的初始化方法
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, '在吃鱼！')


dog = Dog('小黑', 10, '黑色')

dog.eat()

cat = Cat('小金', 15, '金色')

print(cat.color, '\n\n')

# 多态的使用
# 其实可以解释为多个子类中都有同一种方法的调用
# 先建立对象
an = Animal('黄色')
dog = Dog('小黑', 10, '黑色')
cat = Cat('小金', 15, '金色')

# 多态方法
