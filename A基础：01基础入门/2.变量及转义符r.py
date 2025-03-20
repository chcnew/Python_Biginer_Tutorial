# x = "chc\nnew"
# y = r"chc\nnew"
#
# print("未转义之前分行显示结果：")
# print(x)
#
# print("\n")
#
# print(r"转义之后\n\t等制表符不起作用：")
# print(y)
#


# str = "sdadsa123"
# if int(str):
#     print("True")
# else:
#     print("False")

import re

strx = "sdadsa123"
x = re.findall("\\d", strx)

print(strx.isdigit())
print("".join(x))
