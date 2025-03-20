# -*- coding:utf-8 -*-

class Solution:
    def getNumber(self, a, b, c):
        lst = [a, b, c]
        lst_sort = sorted(lst)

        x, y, z = lst_sort[0], lst_sort[1], lst_sort[2]

        num = 0
        while y > 0:
            y -= 1
            z -= 1
            num += 1

        while x > 0 and z > 0:
            x -= 1
            z -= 1
            num += 1

        return num


solution = Solution()
res = solution.getNumber(1, 8, 8)
print(res)
