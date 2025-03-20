# _*_ coding: utf-8 _*_

"""
简单练习使用jinjia2插入数据
"""

from jinja2 import Template

# 打开模版
with open("../templates/practice01.html", "r", encoding="utf-8") as r_file:
    content = r_file.read()
# 载入模版，实例对象
template = Template(content)
# 设置参数
element = {
    "title": "taskxxx",
    "data": [
        {"name": "gtr", "age": 24, "job": "rrr"},
        {"name": "ewq", "age": 25, "job": "yyy"},
        {"name": "chc", "age": 28, "job": "eng"}
    ]
}
# 渲染模版
with open(f"output.html", "w", encoding="utf8") as w_file:
    w_file.write(template.render(element))
