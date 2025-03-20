"""1.帮一家快递点开发一个快递价格计算器业务如下:
提示用户输入:1重量; 2.地点编号
快递费算法首重:3公斤

3公斤以内:东三省/宁夏青海/海南:12元 新疆/西萤:20元 港澳台/国外 不接受
寄件其他:10元

超过3公斤部分:东三省/宁夏青海/海南 +10元/kg 新疆/西藏 +20元/kg 港澳台国外联系总公司
其他 5元/kg

2.开发一个个人所得税计算器(用户输入工资和五险一金,计算纳税额和到手工资);
(参考http://www.gerensuodeshui.cn/)
工资个税的计算公式为:应纳税额= (总工资 - “五险一金”金额 - 起征点) X税率-速
算扣除数"""

# 实验一：

weight = float(input("请输入快递的重量（kg）："))
address = input("请选择寄去的地址类型编号:A：东三省/宁夏青海/海南、B：新疆/西萤、C：澳台/国外、D：其他：")

if 0 < weight < 3:
    if address == "A":
        print("需要付快递费:12")
    elif address == "B":
        print("需要付快递费:20")
    elif address == "C":
        print("该类型不支持寄件，抱歉！")
    elif address == "D":
        print("需要付快递费:10")
    else:
        print("输入编号错误！")

elif weight > 3 or weight == 3:
    if address == "A":
        print("需要付快递费:", weight * 10 + 12)
    elif address == "B":
        print("需要付快递费:", weight * 20 + 20)
    elif address == "C":
        print("该类型不支持寄件，抱歉！")
    elif address == "D":
        print("需要付快递费:", weight * 5 + 10)
    else:
        print("输入编号错误！")
