# _*_ Anaconda3-Python3.8 _*_
lst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 32769, 65536, 4294967296]

# dict.setdefault(key, default=None)方法
# 如果存在键key,则不改变他的值；如果没有，则创建默认值为None的键值对
d = {}
for i in lst:
    k = len(str(i))
    d.setdefault(k, [])
    d[k].append(i)

print(d)
