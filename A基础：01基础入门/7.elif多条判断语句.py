"""多条件语句"""
cunkuan = int(input("请输入你的存款数额(整数)："))

if cunkuan > 100:
    print("买宝马! ")

elif cunkuan > 50:
    print("买丰田")

elif cunkuan > 20:
    print("买二手车! ")

else:
    print("骑你的破自行车!")
