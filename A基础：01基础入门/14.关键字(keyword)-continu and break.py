# _*_ encoding: utf-8 _*_

"""
丈母娘要24万彩礼，假设分期付款，20年付完。每年1.2万，每月0.1万（1000元），显示出累计支付。
嵌套循环
"""

i = 1
summ = 0
year = 20
while i <= year:
    print('第', i, "年到了......")
    # 假设第10年，女婿受了点伤，不能继续付钱了。

    if i == 10:
        print("今年你受伤了，就不给了！")
        i += 1
        year += 1
        continue  # 如果写 break 则表示直接跳出该循环结构

    j = 1
    while j <= 12:
        summ += 1000
        print(f"第{i}年第{j}月，累计支付彩礼：{round(summ, 2)}万")
        j += 1

    i += 1
