# -- coding:utf-8 --

# 导入pyplot
from matplotlib import pyplot as plt
# 从pyplot导入FontProperties类，这个类用于设置自定义字体及字体大小
from matplotlib.font_manager import FontProperties
# 从pyplot导入MultipleLocator类，这个类用于设置刻度间隔
from matplotlib.pyplot import MultipleLocator
import pandas as pd

# import numpy as np

# 字体设置 存在变量font_set 字体用微软雅黑 大小10
font_set = FontProperties(fname=r'c:/windows/fonts/msyh.ttc', size=18)
font_xyticks = FontProperties(fname=r'c:/windows/fonts/simsun.ttc', size=10)

df = pd.read_csv('绘图Test.csv')
x_lie = df.loc[0:30, ['开始时间']]  # loc取连续行列的时候，标签取完，这与切片概念不同。
y_lie = df.loc[0:30, ['306024:忙时话音信道总话务量(erl)']]

# datafram['A'].tolist()  A列转换为list类型
x1 = x_lie['开始时间'].tolist()
y1 = y_lie['306024:忙时话音信道总话务量(erl)'].tolist()

x = [i.replace('0:00', '') for i in x1]  # 横坐标
y = y1  # 纵坐标

# 英文 figure:图形   dpi=dots per inch:每英寸点数
# 设置图片尺寸
# fig=plt.figure(figsize=(16,10),dpi=80)
fig = plt.figure(figsize=(16, 10), dpi=80)

# 设置刻度 用于清楚地显示刻度标签
scale = [i for i in range(1, 32, 4)]
plt.xticks(scale)

# 设置刻度的字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

MultipleLocator(1)

# 设置刻度旁边label:标签
# 设置x、y轴标签(set_xlabel)
plt.xlabel(u'------>时间------>')
plt.ylabel(u'------>话务量(erl)------>')

# 设置标题
plt.title('4DS_14站D_bts1-3月每日话务量折线图', color='red', fontweight=800, size=25)

# 生成网格
plt.grid()

# 绘图
plt.plot(x, y)

# 输出图片
plt.show()

# 保存 png jpg svg/高清放大无锯齿 ...等类型
# plt.savefig('./testpicture.svg')
