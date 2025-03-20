# _*_ coding: utf-8 _*_

"""
getops模块

该模块是专门用来处理命令行参数的。
函数：opts, args = getopt(args, shortopts, longopts = [])
参数：

args： 一般是sys.argv[1:]
shortopts： 短格式 (-) ， 只表示开关状态时，即后面不带附加数值时，在分析串中写入选项字符。
当选项后面要带一个附加数值时，在分析串中写入选项字符同时后面加一个:号 ， 如"vc:"。
longopts：长格式(--) ， 只表示开关状态时，即后面不带附加数值时，在队列中写入选项字符。
当选项后面要带一个附加数值时，在队列中写入选项字符同时后面加一个=号 ， 如["help", "log="] 。
返回：

opts： 分析出的格式信息，是一个两元组的列表，即[(选项串1, 附加参数1), (选项串2, '')]， 注意如果没有附加数值则为空字符串
args： 为不属于格式信息的剩余的命令行参数
"""

import getopt
import sys

if __name__ == '__main__':
    # 设置启动形参：-V --help --input=000
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'V', ['help', 'input='])
        print(opts, args)
    except getopt.GetoptError as e:
        print('Got a eror and exit, error is %s' % str(e))

