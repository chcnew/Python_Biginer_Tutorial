# python的面向对象：
# 	面向对象的程序设计的核心是对象（上帝式思维），要理解对象为何物，必须把自己当成上帝，上帝眼里世间存在的万物皆为对象，
# 不存在的也可以创造出来。面向对象的程序设计好比如来设计西游记，如来要解决的问题是把经书传给东土大唐，如来想了想解决这
# 个问题需要四个人：唐僧，沙和尚，猪八戒，孙悟空，每个人都有各自的特征和技能（这就是对象的概念，特征和技能分别对应对象
# 的属性和方法），然而这并不好玩，于是如来又安排了一群妖魔鬼怪，为了防止师徒四人在取经路上被搞死，又安排了一群神仙保驾
# 护航，这些都是对象。然后取经开始，师徒四人与妖魔鬼怪神仙互相缠斗着直到最后取得真经。如来根本不会管师徒四人按照什么流程去取。

# 面向对象的程序设计：
# 优点是：解决了程序的扩展性。对某一个对象单独修改，会立刻反映到整个体系中，如对游戏中一个人物参数的特征和技能修改都很容易。
# 缺点：可控性差，无法向面向过程的程序设计流水线式的可以很精准的预测问题的处理流程与结果，面向对象的程序一旦开始就由对象之间的交互解决问题，
# 即便是上帝也无法预测最终结果。于是我们经常看到一个游戏人某一参数的修改极有可能导致阴霸的技能出现，一刀砍死3个人，这个游戏就失去平衡。

# 应用场景：需求经常变化的软件，一般需求的变化都集中在用户层，互联网应用，企业内部软件，游戏等都是面向对象的程序设计大显身手的好地方。
# 在python 中面向对象的程序设计并不是全部。
# 面向对象编程可以使程序的维护和扩展变得更简单，并且可以大大提高程序开发效率 ，另外，基于面向对象的程序可以使它人更加容易理解你的代码逻辑，
# 从而使团队开发变得更从容。

# 了解一些名词：类、对象、实例、实例化
# coding: utf-8

# 创建一个类：
class Dog(object):  # 继承于object 即对象类
    """docstring for ClassName"""
    Dog_type = '宠物'  # 类变量

    def __init__(self, name, age, color):  # 初始化方法
        self.name = name  # 实例变量（属性）
        self.age = age
        self.__color = color

    def eat(self):  # 普通方法1 定义参数
        print(self.name, '-', self.age, '在啃骨头！')

    def run(self, speed, attitude):  # 普通方法2 定义参数调用无 self.
        print(self.name, '-', self.color, '在飞快的跑步！', '速度：', speed, '姿态：', attitude)


dog = Dog('小黑', 3, '金黄色')
print(dog.color)
dog.eat()
dog.color = '黑色'
dog.run('3m/s', '可爱')
