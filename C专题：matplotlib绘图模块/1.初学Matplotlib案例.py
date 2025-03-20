# matplotlib基本要点
# from matplot1ib import pyplot as plt - -> 导入pyplot
# x = range(2,26,2)
# #数据在x轴的位置,是-个可迭代对象
# y = [15,13,14.5,17,20,25,26,26 ,24,22,18,15]
# #数据在y轴的位置,是一个可迭代对象
# -> x轴和y轴的数据一起组成了所有要绘制出的坐标
# -->分别是(2,15),(4,13),(6,14.5)...
# plt.plot(x,y)一>传入x和y ,通过plot绘制出折线图
# plt.show()一>在执行程序的时候展示图形

# 进阶
# WE CAN DO MORE
# 1.设置图片大小(想要一个高清无码大图) fig=figure(figsize=(20.8),dpi=80)
# 2.保存到本地
# 3.描述信息,比如x轴和y轴表示什么,这个图表示什么
# 4.调整x或者y的刻度的间距
# 5.线条的样式(比如颜色，透明度等)
# 6.标记出特殊的点(比如告诉别人最高点和最低点在哪里)
# 7.给图片添加一个水印(防伪,防止盗用)


from matplotlib import pyplot as plt

fig = plt.figure(figsize=(16, 10), dpi=80)

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 绘图
plt.plot(x, y)

# scale 刻度
# 设置X刻度为float（默认系统不支持） 假设为0.5
scale = [i / 2 for i in range(4, 49)]
# plt.xticks(kd_xticks)
plt.xticks(scale, fontsize=14)
plt.yticks(fontsize=14)

# 保存 可以保存为.svg格式 放大后不会有锯齿
# plt.savefig('./picture.svg')

# 展示
plt.show()
