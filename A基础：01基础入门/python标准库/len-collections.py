"""
Python的collections库提供了一些有用的数据结构，它们是Python内置数据类型的扩展。以下是一些常见的使用场景：
1. defaultdict：当我们需要创建一个字典，但是不确定某些键是否存在时，可以使用defaultdict。它会自动为不存在的键创建一个默认值。
2. Counter：当我们需要对一个可迭代对象中的元素进行计数时，可以使用Counter。例如，统计一段文本中每个单词出现的次数。
3. deque：当我们需要高效地从序列的两端添加或删除元素时，可以使用deque。它比列表更快，因为它实现了双向队列。
4. OrderedDict：当我们需要按照插入顺序或者键的顺序来遍历一个字典时，可以使用OrderedDict。
5. namedtuple：当我们需要定义一个类似于元组的数据结构，并且希望可以通过属性名来访问元素时，可以使用namedtuple。
"""
import math
from collections import Counter

string = input()
n = len(string)
down_list = []
for m, n in Counter(string).items():
    if n > 1:
        down_list.append(math.factorial(n))
up = math.factorial(len(string))
down = 1
for i in down_list:
    down *= i
print(up // down)
