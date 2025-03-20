"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 
 * @Environment: Anaconda3
"""

# 匹配身份证号
# import re
#
# text = "dsf130429191912015219k13042919591219521xkk"
# data_list = re.findall(r"\d{17}[\dx]", text)
# print(data_list)  # ['130429191912015219','13042919591219521X']
#
# text = "dsf130429191912015219k13042919591219521xkk"
# data_list = re.findall(r"\d{17}(\d|x)", text)
# print(data_list)  # ['130429191912015219','13042919591219521X']
#
# text = "dsf130429191912015219k13042919591219521xkk"
# data_list = re.findall(r"(\d{17}(\d|x))", text)
# print(data_list)  # ['130429191912015219','13042919591219521X']
#
# text = "dsf130429191912015219k13042919591219521xkk"
# data_list = re.findall(r"(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})(\d|x)", text)
# print(data_list)

# 匹配手机号
# import re
#
# text = "我的手机哈是15133377892，你的手机号是1171123啊?"
# data_list = re.findall(r"1[3-9]\d{9}", text)
# print(data_list)  # ['15133377892']

import re

text = "楼主太牛逼了，在线想要4426625784@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
email_list = re.findall(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+.[a-zA-Z0-9_-]+", text, re.ASCII)
print(email_list)

text = "楼主太牛逼了，在线想要4426625784@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
email_list = re.findall(r"\w+@\w+.\w+", text, re.ASCII)
print(email_list)
