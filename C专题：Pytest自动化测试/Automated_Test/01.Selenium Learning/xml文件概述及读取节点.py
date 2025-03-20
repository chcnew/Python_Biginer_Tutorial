# 什么是xml文件?。
# xml即可扩展标记语言，它可以用来标记数据、定义数据类型，是一种允许用户对自己的
# 标记语言进行定义的源语言。。
# 从结构上，很像HTML超文本标记语言。但他们被设计的目的是不同的，具体如下:。
# ● XML   被设计用来传输和存储数据。
# ● HTML  被设计用来显示数据。

from xml.dom import minidom

dom=minidom.parse('./Class_infotest.xml')

root=dom.documentElement

a=root.nodeName
b=root.nodeValue
c=root.nodeType

print(a)
print(b)
print(c)

