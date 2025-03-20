# _*_ Anaconda3-Python3.8 _*_
lst = [1, 3, 77, 454, 23, 34, 55, 23, 6765, 998, 34, 123, 1, 67, 2, 90, 324, 21, 565, 8, -111]


# 冒泡排序,从小到大排序
def sortli(li):
    leng = len(lst)
    for i in range(leng):
        # 循环少一个，留出空位存当次最大值
        for j in range(0, leng - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


sortli(lst)
print(lst)  # [-111, 1, 1, 2, 3, 8, 21, 23, 23, 34, 34, 55, 67, 77, 90, 123, 324, 454, 565, 998, 6765]
