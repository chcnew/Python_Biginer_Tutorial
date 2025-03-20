# _*_ coding: utf-8 _*_

"""
功能：
"""
import re

# 输入要匹配的字符串
# str = input('ip：')

# 测试用字符串
# str = "fsff123.12.12.12q we1764.12.12.76asd12.12.23.287frg45.23.278.34hrdf127.0.0.1jj255.45.45.45bghtbh43.0.76.345"
str = "123.12.12.12q we1764.12.12.76asd12.12.23.287frg45.23.278.34hrdf127.0.0.1jj255.45.45.45bghtbh43.0.76.345"

# 分为开头，中间和结尾三部分，提取可能包含ip地址的字符串
# 匹配中间部分的ip，返回列表
result = re.findall(r'\D(?:\d{1,3}\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\D', str)
print(result)

# 匹配开头可能出现ip
ret_start = re.match(r'(\d{1,3}\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\D', str)
if ret_start:
    print("start:", ret_start.group())
    result.append(ret_start.group())

# 匹配结尾
ret_end = re.search(r'\D(\d{1,3}\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$', str)
if ret_end:
    print("end: ", ret_end.group())
    result.append(ret_end.group())

print('*' * 20)
print("result: ", result)  # result:  ['g45.23.278.34h', 'f127.0.0.1j', 'j255.45.45.45b', '123.12.12.12']

# 构造列表保存ip地址
ip_list = []
for r in result:
    # 正则提取ip
    ret = re.search(r'((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)', r)
    if ret:
        # 匹配成功则将ip地址添加到列表中
        ip_list.append(ret.group())

# 输入结果列表
print(ip_list)  # ['127.0.0.1', '255.45.45.45', '123.12.12.12']
