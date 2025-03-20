# _*_ coding: utf-8 _*_

"""
功能：求中位数
写一个函数 get_median(l) 计算列表中的中位数，如果列表中的元素个数是偶数，则返回中间那两个数值的平均值
例如：get_median([3,5,7])则返回5 get_median([3,5,7,9])  则返回6
"""
from typing import List


# 本题面试官已设置测试用例
def get_median(nums: List[int]) -> float:
    # 在这⾥写代码
    length = len(nums)

    if length < 1 or length > 1000:
        return

    nums.sort()
    # 奇数
    if length % 2 != 0:
        return nums[int((length - 1) / 2)]
    # 偶数
    a = int(length / 2) - 1
    b = a + 1
    return (nums[a] + nums[b]) / 2


x = get_median([1, 3, 5, 6, 9, 11])
print(x)
