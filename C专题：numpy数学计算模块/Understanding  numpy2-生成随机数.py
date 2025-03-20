# numpy数据结构中,只能有一种数据类型
# 定义数据类型
import pandas as pandas
import numpy as np

list_a = [[1, 3, 5], [2, 4, 6], [55, 28, 24, ]]  # 列表中的元素还是列表
np_list = np.array(list_a, dtype=np.float)  # 定义为浮点数
print("类型:", type(np_list), "\n")
print(np_list, "\n")
print(np_list.shape, "\n")  # 形状 行数与列数 3行3列
print(np_list.ndim, "\n")  # 维度 2维
print(np_list.dtype, "\n")  # 数据类型
print(np_list.itemsize, "\n")  # 每个元素占存储量（字节） float64一个元素占8个字节
print(np_list.size, "\n\n")  # 长度大小，3行3列 9个数，就是9

# numpy常用的array
print(np.zeros([3, 5], "\n"))  # 输出3行5列数据为0的数字 初始化数字  np.ones([x,y])  只有zeros和ones两个用于初始化

print("rand:特征为介于0和1之间的随机数")
print(np.random.rand(2, 4), "\n")  # 生成介于0和1之间的 2行4列 随机数  数据类型：numpy.ndarray
print(np.random.rand(2), "\n")  # 生成介于0和1之间的2个随机数  数据类型：list
print(np.random.rand(), "\n\n")  # 生成介于0和1之间的1个随机数 数据类型：float

print("randint:特征为介于符合定义范围的随机整数")
print(np.random.randint(1, 10, 5), "\n\n")  # 生成介于1和10之间的5个随机数

# 科普正态分布知识
# [1]正态分布为什么常见？真正原因是中心极限定理（central limit theorem）。根据中心极限定理，
#   如果一个事物受到多种因素的影响，不管每个因素本身是什么分布，它们加总后，结果的平均值就是正态分布。
# [2]正态分布只适合各种因素累加的情况，如果这些因素不是彼此独立的，会互相加强影响，那么就不是正态分布了。
#   PS:如果各种因素对结果的影响不是相加，而是相乘，那么最终结果不是正态分布，而是对数正态分布（log normal distribution）
print("randn:特征为标准正态分布随机数")
print(np.random.randn(4, 5), "\n\n")  # 生成4行5列正态分布随机数

print("choice:定义数当中随机选择一个，可用列表为对象")
print(np.random.choice([5, 2, 0]), "\n")  # 随机生成5\2\0这三个当中的一个
A = [3, 7, 99, 2, 5, 0]
print(np.random.choice(A), "\n\n")  # 随机列表A当中的一个数

# 其他分布 如beta分布
print(np.random.beta(1, 100, 14), "\n")  # 随机生成介于1和100之间的14个随机数 1维数据  数据类型：numpy.ndarray
x = np.random.beta(1, 100, 18)
print(x.shape)  # 输出形状 行 列
print(x.ndim)  # 输出维度
