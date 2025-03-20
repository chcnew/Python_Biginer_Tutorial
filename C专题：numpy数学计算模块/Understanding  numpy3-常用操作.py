# numpy常用操作
import numpy as np

# print(np.arange(1,11).reshape([2,5]))
x = np.arange(1, 11).reshape([2, 5])  # .reshape([x,y])生成x行y列的东西
print(x)
y = np.exp(x)  # 自然指数e的x次方
print(y)
print(np.exp2(x))  # 底数为2的x次方
print(np.sqrt(x))  # x的1/2次方
print(np.sin(x))  # 三角函数
print(np.log(x))  # 对数函数 e为底x为变量的对数函数
print('\n')

lst = np.array(
    [[[1, 2, 3, 4],
      [4, 5, 6, 7]],
     [[7, 8, 9, 10],
      [10, 11, 12, 13]],
     [[14, 15, 16, 17],
      [18, 19, 20, 21]]])

# axis 是决定计算维度深度 值越大,越深入
print(lst.sum(axis=0))  # 这里是最外层三个列表相加。
print('\n')

print(lst.max(axis=1))  # 这里是最外层再进入1层元素之间相比较取最大值操作。
print('\n')

print(lst.min(axis=2))  # 这里是最外层再往内进入2层元素之间相比较取最小值操作。
print('\n')
