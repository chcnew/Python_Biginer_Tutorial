import random

# red_nums是采集红色球的数字，
# 集合的目的是不用判断随机数字是否重叠,比较方便。如果使用列表，就要先去重后再来判断长度是否到６，如果先判断长度是否到６，万一列表里有重复的元素，去重后就没有６个元素了。
xh = int(input("请输入买的注数:"))

sta = 1
while sta <= xh:
    red_nums = set()

    while True:
        red_num = int(random.random() * 34)  # random.random()返回随机生成的一个实数，它在[0,1)范围内，所以要想得到33，必须乘以34
        if red_num == 0:
            continue
        else:
            red_nums.add(red_num)  # add()方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作
        if len(red_nums) == 6:
            break

    # 将集合进行排序，彩票就是这样的，前６个数字从小到大
    red_ = sorted(red_nums)
    # 将集合转为列表的形式，方便向该数字中增加蓝色数值
    double_ball = list(red_)

    # 生成一个不为0的1～16的蓝色球数字
    while True:
        blue_num = int(random.random() * 17)
        if blue_num != 0:
            break

    # 组合成双色球，蓝色球数字和前六个红色球的数字之间没有关系
    double_ball.append(blue_num)

    print(double_ball)

    sta = sta + 1
