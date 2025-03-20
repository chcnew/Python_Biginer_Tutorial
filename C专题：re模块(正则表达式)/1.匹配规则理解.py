"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/11
 * @Environment: Anaconda3
"""
# ################ 字符相关 ################
# 匹配指定字符
# import re
#
# text = "你好wupeiqi,阿斯顿发wupeiqasd阿士大夫能接受的wupeiqiff"
# data_list = re.findall("wupeiqi", text)
# print(data_list)  # [ 'wupeiqi ' , 'wupeiqi '] # 匹配指定字符
# print(data_list.count("wupeiqi"))  # 计算出现次数

# [abc]匹配a或b或c字符。
# import re
#
# text = "你2b好wupeigi,阿斯顿发awupeiqasd阿士大夫a能接受的wffbbupqaceiqiff"
# data_list = re.findall("[abc]", text)
# print(data_list)  # ["b", "a ", "a ", "a ', 'b ", 'b", "c"]

# q[abc]匹配q搭配a或b或c字符。
# import re
#
# text = "你2b好wupeigi,阿斯顿发awupeiqasd阿士大夫a能接受的wffbbupqcceiqiffqbqb"
# data_list = re.findall("q[abc]", text)
# print(data_list)  # ['qa', 'qc', 'qb', 'qb']

# [^abc]匹配除了abc意外的其他字符。
# import re
#
# text = "你wffbbupceiqiff"
# data_list = re.findall("[^abc]", text)
# print(data_list)  # ['你', 'w', 'f', 'f', 'u', 'p', 'e', 'i', 'q', 'i', 'f', 'f']

# [a-z]匹配a-z的字符
# [0-9]匹配a-z的字符
# import re

# text1 = "TATAalexrootrootadmin456我"
# text2 = "ale456我撒旦撒旦dsdsad"
# data_list1 = re.findall("t[a-z]", text1)
# data_list2 = re.findall("[0-9]", text2)
# print(data_list1)  # ['TA', 'TA']
# print(data_list2)  # ['4', '5', '6']

# ·代指除换行符以外的任意字符。
# import re
# text1 = "alexraotrootrootadmin"
# data_list1 = re.findall("r.o", text1)
# print(data_list1)  # ['rao', 'roo', 'roo']
#
# text2 = "alexraotrootrootadmin"
# data_list2 = re.findall("r.+o", text2)  # 贪婪匹配[就是匹配到最远符合的]
# print(data_list2)  # ['raotrootroo']
#
# text3 = "alexraotrootrootadmin"
# data_list3 = re.findall("r.+?o", text3)  # 非贪婪匹配.+?[就是匹配到最近符合的]
# print(data_list3)  # ['rao', 'roo', 'roo']


# \w代指字母、数字、下划线、汉字
# import re
#
# text = "北京武沛alex齐 北京武沛alex浙"
# data_list = re.findall("武\\w+x", text)
# print(data_list)  # ['武沛alex', '武沛alex']

# \d 代指数字
# import re
#
# text = "root-ad32min-add3-ad1mdlin"
# data_list = re.findall(r"d\d", text)
# print(data_list)  # [ " d3 ', 'd3" , "d1 " ]
#
# text = "root-ad32min-add3655464-ad1mdlin"
# data_list = re.findall(r"d\d+", text)  # 贪婪匹配+代表前一个字符或代表的类型出现一次或多次
# print(data_list)  # [ " d32 ', 'd3" , "d1 " ]

# \s代指任意的空白符，包括空格、制表符等
# import re
#
# text = "root admin add admin"
# data_list = re.findall(r"a\w+\s\w+", text)
# print(data_list)  # ['admin add']


# ################ 数量相关 ################
# ● *代表前一个字符或类型出现0次或多次
# import re
#
# text = "他是大B个，确实是个大2B，大3B，大66666B。"
# data_list = re.findall("大2*B", text)
# print(data_list)  # ['大B', '大2B']

# ● +代表前一个字符或类型出现1次或多次
# import re
#
# text = "他是大B个，确实是个大2B，大3B，大66666B。"
# data_list = re.findall(r"大\d+B", text)
# print(data_list)  # ['大2B', '大3B', '大66666B']

# ● ?代表前一个字符或类型出现0次或1次
# import re
#
# text = "他是大B个，确实是个大2B，大3B，大66666B。"
# data_list = re.findall(r"大\d?B", text)
# print(data_list)  # ['大B', '大2B', '大3B']

# {n}重复n次
# {n,}重复n次或更多次
# {n,m}重复最少n次到最多m次
# import re
#
# text = " 楼主太牛逼了，在线想要4426625780qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
# data_list = re.findall(r"151312\d{5}", text)  # 数字次数5
# print(data_list)  # ['15131255789']
#
# text = " 楼主太牛逼了，在线想要4426625780qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
# data_list = re.findall(r"\d{9,}", text)  # 数字次数区间[9,infinity]
# print(data_list)  # ['4426625780', '15131255789']
#
# text = " 楼主太牛逼了，在线想要4426625780qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
# data_list = re.findall(r"\d{10,15}", text)  # 数字次数区间[10,15]
# print(data_list)  # ['4426625780', '15131255789']

# ################ 括号 ################
# 提取数据区域
# import re
#
# text = " 楼主太牛逼了，在线想要4426625780qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
# data_list = re.findall(r"15131(2\d{5})", text)
# print(data_list)  # ['255789']
#
# # 同级括号，分别匹配
# text = " 楼主太牛逼了，在线想要4426625780qq.com和xxxxx@live.com谢谢楼主，151312557323315444手机号也可15131255789，搞起来呀"
# data_list = re.findall(r"15(13)1(2\d{5})", text)
# print(data_list)  # [('13', '255732'), ('13', '255789')]']
#
# 括号增多，由外到里匹配。
# text = " 楼主太牛逼了，在线想要4426625780qq.com和xxxxx@live.com谢谢楼主，151312557323315444手机号也可15131255789，搞起来呀"
# data_list = re.findall(r"(15(13)1(2\d{5}))", text)
# print(data_list)  # [('15131255732', '13', '255732'), ('15131255789', '13', '255789')]
#
# 提取数据区域
import re

# 括号搭配或运算，由外到里
text = " 楼主15131root太牛逼了，在线想要4426625780qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
data_list = re.findall(r"15131(2\d{5}|r\w+太)", text)
print(data_list)  # ['root太', '255789']

text = " 楼主15131root太牛逼了，在线想要4426625780qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
data_list = re.findall(r"(15131(2\d{5}|r\w+太))", text)
print(data_list)  # [('15131root太', 'root太'), ('15131255789', '255789')]
