"""
 * @Description: Python
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Version: 1.0
"""
import time


def main():
    """
    Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
    基本语法是通过 {} 和 : 来代替以前的 % 。
    format 函数可以接受不限个参数，位置可以不按顺序.
    说明：*args 以元组（tuple）或者列表（list）的形式传参数； **kwargs不知道往函数中传递多少个关键词参数或者想传入字典的值作为关键词参数
    """

    print('\n')
    print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
    print("{0} {1}".format("hello", "world"))  # 设置指定位置
    print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置

    print('\n')
    # 设置参数方式
    print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
    # 通过字典设置参数
    site = {"name": "菜鸟教程", "url": "www.runoob.com"}
    print("网站名：{name}, 地址 {url}".format(**site))

    print('\n')
    # 数字格式化
    print("{:.2f}".format(3.1415926))  # 保留2位小数【3.14】
    print("{:+.2f}".format(-3.1415926))  # 附带符号保留2位小数【-3.14】
    print("{:.2%}".format(0.1415926))  # 附带符号保留2位小数【314.16%】


if __name__ == '__main__':
    start = time.perf_counter()  # 程序运行起始时间
    main()
    print('运行耗时:', "{.2f}".format(time.perf_counter() - start))  # 程序运行结束时间
