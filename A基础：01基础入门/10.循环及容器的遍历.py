"""
for i in range(1000):
	print("第",i+1,"次打印hell~","i的值其实是",i)
	print("\n")
"""
# for 元素变量 序列
#    执行语句

# 序列格式 （x,y,z）
# x为元素变量第一个值，循环至y-1 ，z 是序列差值(步长)

# for i in range(50,100,8):  #对序列进行遍历
#	print("第",i+1,"次打印hell~","i的值其实是",i)

"""
range()语法：
range(start,end,step=1):顾头不顾尾
正序遍历：

range(10):默认step＝1，start＝0,生成可迭代对象，包含[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range(1,10):指定start＝1，end＝10，默认step＝1，生成可迭代对象，包含[1, 2, 3, 4, 5, 6, 7, 8, 9]

range(1,10,2):指定start＝1，end＝10，step＝2，生成可迭代对象，包含[1, 3, 5, 7, 9]

逆序遍历：
range(9,-1,-1):  step＝-1，start＝9,生成可迭代对象，包含[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(9, -1, -1):
	print(i)
"""

# 对容器遍历
list1 = [1, 2, 3, 4, 5]
tuple1 = (5, 6, 7, 8, 9)
dict1 = {"name": "张三", "age": 18}
col = {"a", "b", "c"}

# for i in dict1: #对字典进行遍历
#	print(i,dict1[i])

# for i in tuple1:
#	print(i,tuple1(i))  #TypeError: 'tuple' 对象不可调用
