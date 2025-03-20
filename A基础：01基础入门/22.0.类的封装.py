# coding: utf-8

# 类的封装 为了让数据更安全的使用
# 建立位私有 在return访问

class Card(object):
    """docstring for myconstom"""

    def __init__(self, num, pwd, ban):
        self.num = num  # 卡号
        self.pwd = pwd  # 密码
        self.__ban = ban  # 余额 加上双下滑线代表私有化 访问先在内部建立方法

    def getBan(self):
        return self.__ban


card = Card('0421', 'cc854', 1200)

print(card.num)
print(card.getBan())  # 内部建立访问方法，可取得到
print(card.__ban)  # 封装类，直接取报错。(但是其实python即使是对数据进行了封装，依然有方法取得到！所以一般对于安全性较高的开发项目不建议使用pthon编写，可考虑java等)
