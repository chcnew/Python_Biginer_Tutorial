# 双变量嵌套的if结构
cunkuan = int(input("请输入你的存款数额(整数)："))
zizhu = int(input("请输入资助款项数额(整数)："))
if cunkuan > 100:
    print("买宝马! ")
    if zizhu > 50:
        print("合计资助款可以买一辆宝马740 ! ")
    elif zizhu > 30:
        print("合计资助款可以买一辆宝马520 !")
    elif zizhu > 20:
        print("合计资助款可以买一辆宝马320 !")
    else:
        print("合计资助款只能去二手车市场! ")
elif cunkuan > 50:
    print("买丰田")
elif cunkuan > 20:
    print("骑你的破自行车!")
