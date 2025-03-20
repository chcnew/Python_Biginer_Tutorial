# 1.按顺序位置传入参数
def custom_def1(a, b):  # a,b成为形式参数 简称形参
    x = a + b * b  # x等于a加上b的平方
    return x


x = custom_def1(3, 5)  # 3，5成为实际参数 简称实参
print(x)


# 2.按实参赋值给形参传入
def custom_def1(a, b):
    x = a + b * b
    return x


x = custom_def1(b=5, a=3)
print(x)


# 3.按顺序位置 和 实参赋值给形参 混合传入
# 此方法注意 只能先顺序，传入，剩下的可以按赋值方法传入。
def custom_def1(a, b, c, d):
    x = a + b * b + c * 5 + d * d * d
    return x


x = custom_def1(3, 5, d=2, c=1)
print(x)


# 4.设置，默认参数
def custom_def1(a, b=3):
    x = a + b * b
    return x


x = custom_def1(3)
print(x)


# def custom_def1(a,b=3,c):#这种是错误的!只要第一个开始存在默认参数 后面就必须设置默认值
def custom_def1(a, b=3, c=1):
    x = a + b * b + c
    return x


x = custom_def1(3, 2, 4)
print(x)


# 不定长传入参数 实质是元组数据类型
def custom_sum(*args):  # 接收不定长度的数据 组成一个元组
    x = sum(args)
    return x


x = custom_sum(1, 2, 3, 4, 5, 100)
print(x)
