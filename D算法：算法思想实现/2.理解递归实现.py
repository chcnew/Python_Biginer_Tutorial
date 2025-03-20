# _*_ Anaconda3-Python3.8 _*_

# 有一个多层嵌套的列表A=[1,2,[3,4,["434",...]]], 请写一段代码遍历A中的每一个元素并打印出来？
# 递归写法，函数调用自己

def list_item(lst):
    for item in lst:
        if isinstance(item, list):
            list_item(item)
        else:
            print(item)


A = [1, 2, [3, 4, ["434", 'ddd'], [1, 2, 3], "x", "y", ["as", "ts", ["w", "r", ["ssd", "pp"], "h"]]]]

list_item(A)
