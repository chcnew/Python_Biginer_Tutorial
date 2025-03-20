"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Environment: Anaconda3
"""
import os
import time


def main():
    # 获取对当前文件所在绝对路径；
    print(os.path.abspath(''))
    # 获取路径基础部分，若指向文件，则返回文件名；若指向目录，则返回最后一个目录名；
    print(os.path.basename(r'F:\My_Study\1.Python_learning\2.Python Biginer Tutorial-51zxw'))
    # 获取路径中的上级目录部分；
    print(os.path.dirname(r'F:\My_Study\1.Python_learning\2.Python Biginer Tutorial-51zxw'))
    # 判断文件是否存在；
    print(os.path.exists('20.2.模块学习_datetime.py'))
    # 判断参数是否是文件，返回True或False
    print(os.path.isfile('20.2.模块学习_datetime.py'))
    # 判断参数是否是目录，返回True或False
    print(os.path.isdir('20.2.模块学习_datetime.py'))


if __name__ == '__main__':
    start = time.perf_counter()  # 程序运行起始时间
    main()
    print('运行耗时:', time.perf_counter() - start)  # 程序运行结束时间
