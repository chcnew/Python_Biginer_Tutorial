# 求1+2+3+...+100=?

y = 0
for x in range(1, 101, 1):
    y = y + x
print('求和结果：', y, '\n')

# 求列表中最大值
# 求列表中最小值

a = [3322, 1758, 4578, 2256, 8456]
b = max(a)
c = min(a)
print('列表a中最大值：', b)
print('列表a中最小值：', c, '\n')

# 用循环实现
a = [9922, 1758, 4578, 2256, 8456]
for x in range(0, len(a) - 1):
    if a[0] <= a[x + 1]:
        y = a[x + 1]
    else:
        y = a[0]
print('列表a中最大值：', y)

a = [9988, 1758, 4578, 2256, 50]
for x in range(0, len(a) - 1):
    if a[0] >= a[x + 1]:
        y = a[x + 1]
    else:
        y = a[0]
print('列表a中最小值：', y)
