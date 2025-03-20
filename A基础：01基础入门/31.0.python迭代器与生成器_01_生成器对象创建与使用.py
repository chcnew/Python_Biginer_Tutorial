"""
 * @Description: Python
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Environment: Anaconda3
"""
import sys


def main():
    not_generator = [x * x for x in range(5)]  # 列表迭代，不属于生成器，消耗内存空间较大
    for i1 in not_generator:
        print(i1, end=" ")
    print("\n")

    generator = (x * x for x in range(5))  # 生成器()表示，节约内存空间，但是用完以后，下次再使用就为空了。
    for i2 in generator:
        print(i2, end=" ")


# yield 关键字
# 输出0至不大于max的偶数 使用生成器完成
def generator_even(max_num):
    for i3 in range(0, max_num + 1):
        if i3 % 2 == 0:
            yield i3  # 创建并返回生成器对象，与return类型，直接退出并返回。


if __name__ == '__main__':
    # main()
    generatorA = generator_even(10)
    print("返回值：", generatorA, "\n返回类型：", type(generatorA))
    for i in generatorA:
        print(i, end=" ")
    print("\n")

    # 生成器对象__next__()方法，每次使用返回一次直至迭代全部。
    # __next()__方法超过可迭代个数，会抛出异常，所以使用时必须搭配try except使用
    # next(generatorB)  等价于  generatorB.__next__()
    generatorB = generator_even(10)
    while True:
        try:
            print(next(generatorB))
        except StopIteration:
            sys.exit()
