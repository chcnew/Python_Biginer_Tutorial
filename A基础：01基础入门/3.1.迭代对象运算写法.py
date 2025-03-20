# 学习range创建整体元素 倍数缩小 倍数放大 减小 增加

x = [i for i in range(2, 10, 2)]
print(x)

y = [i / 2 for i in range(2, 10, 2)]
print(y)

# 对列表操作有乘法，就是增加原来元素多一份
z = [2, 2, 6]
z1 = z * 2
print(z1)

# z列表元素都*2
z2 = [i * 2 for i in z]
print(z2)
