# _*_ coding: utf-8 _*_

"""
功能：测试题目

来来来，考考大家9个成人带着9名儿童参观博物馆，下面是这个博物馆的售票信息。算一算，怎样购票最划算，需要多少元？
成人票：80元／人
儿童票：40元／人
团体票（10人及以上）票价：50元/人
"""
lst1 = []
lst2 = []
lst3 = []
total = 0
for x in range(9, -1, -1):  # 成人
    for y in range(9, -1, -1):  # 儿童
        z = (18 - x - y)
        # total = x * 80 + y * 40 + z * 50
        # print(x, y, z, total)

        if z >= 10 \
                or x + y == 18:
            total = x * 80 + y * 40 + z * 50
            lst1.append(x)
            lst2.append(y)
            lst3.append(total)
            print(x, y, z, total)

min_indices = [i for i, val in enumerate(lst3) if val == min(lst3)]
print(min_indices)

for loc in min_indices:
    print("----最小值搭配：----\n成人：{}\n儿童：{}\n团体：{}\n总票价：{}".format(lst1[loc], lst2[loc], 18 - lst1[loc] - lst2[loc], lst3[loc],
                                                                             total))
