# numpy 

# 关键词： 开源 数据计算扩展

# 功能：ndarray  多维操作  线性代数

import numpy as np

list_a = [[1, 3, 5], [2, 4, 6], [55, 28, 24, ]]  # 列表中的元素还是列表
print("类型:", type(list_a), "\n")
print(list_a)
print("\n")

list_a = [[1, 3, 5], [2, 4, 6], [55, 28, 24, ]]  # 列表中的元素还是列表
list_b = np.array(list_a)  # 将列表中的列表竖起来排列 数据类型: numpy.ndarray
print("类型:", type(list_b), "\n")
print(list_b)

# numpy数据结构中,只能有一种数据类型
# 定义数据类型
list_a = [[1, 3, 5], [2, 4, 6], [55, 28, 24, ]]  # 列表中的元素还是列表
np_list = np.array(list_a, dtype=np.float)  # 定义为浮点数
print("类型:", type(np_list), "\n")
print(np_list, "\n")
print(np_list.shape, "\n")  # 形状 行数与列数 3行3列
print(np_list.ndim, "\n")  # 维度 2维
print(np_list.dtype, "\n")  # 数据类型
print(np_list.itemsize, "\n")  # 每个元素占存储量（字节） float64一个元素占8个字节
print(np_list.size, "\n")  # 长度大小，3行3列 9个数，就是9
