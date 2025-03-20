# while循环和for循环不同的是，它的停止条件是个人自己设定的:
# while判断条件:
# 判断条件和if语句是相同的，而什么时候用while呢?
# 在你确定满足条件而不确定需要的循环次数时，那么while是 最好的选择。

import time

i = 0
while i <= 100:
    if i == 50:
        print("稍等5秒有惊喜！")
        time.sleep(5)
        print("I LOVE U")
    i = i + 1
