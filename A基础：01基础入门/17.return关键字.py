# 函数结构体内部的变量名与外部变量名无联系，可以重复使用。

def custom_def1(a, b):
    x = a + b * b  # x等于a加上b的平方
    return x


x = custom_def1(3, 5)
print(x)
