# test = {'A': 'chc', 'B': 'dsq'}
# print(test)
# print('\n')
#
# print(test.items())
# print('\n')  # 字典的键值对
#
# print(type(test.items()))  #
# print('\n')
#
# print(test.keys())  # 字典的键
# print('\n')
#
# print(test.values())  # 字典键的值

# test = {'A': 'chc', 'B': 'dsq'}
# tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(test)

l1 = [1, 2]
l2 = [2, 4]
print(l1 + l2)  # 列表相加为元素增加，不做算数运算

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'd': 4}
dict1['b'] = dict1['b'] + dict2['b']
print(dict1)  # {'a': 1, 'b': 5} 字典值为数字，相加做算术运算

dict1 = {'a': ['A'], 'b': ['B']}
dict2 = {'b': ['m'], 'd': ['D']}
dict1['b'] = dict1['b'] + dict2['b']
print(dict1)  # {'a': ['A'], 'b': ['B', 'm']} 字典内部为列表，相加则为元素个数增加，不是直接加
x = dict1.keys()  # 注意并不是列表
y = dict1.values()  # 注意并不是列表
print(type(x))  # <class 'dict_keys'>
print(type(y))  # <class 'dict_values'>
y = list(x)
print(y)  # <class 'dict_keys'>

# 字典整体（键值一起）不支持相加操作！
