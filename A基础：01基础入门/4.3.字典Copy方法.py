"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 
 * @Environment: Anaconda3
"""

a = 1
b = a
a = 3
print(a, b)  # a=3,b=1
a = {"A": 10, "B": 20}
b = a
a["B"] = "变了"
print(a, b)  # 两个都变了

# copy方法对一级数据复制
a = {"A": 10, "B": 20}
b = a.copy()
a["B"] = "变了"
print(a, b)  # a变了,b保留

a = {"A": 10, "B": {"你": "100元"}}
b = a
a["B"] = "B变了"
print(a, b)  # a变了,b保留

# deepcopy方法对二级或以上数据复制
import copy

a = {"A": 10, "B": {"你": "100元"}}
b = copy.deepcopy(a)
a["B"] = "B变了"
print(a, b)  # a变了,b保留
