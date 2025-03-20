# _*_ coding: utf-8 _*_

"""
功能：
"""
import os.path
import re
from itertools import islice


def make_log():
    srcf = "uwsgi.log"
    targetf = "TTT.log"
    with open(srcf, "r", encoding="utf-8") as rf:
        srctxt = rf.read()

    # 416 kb * 124 * 2 = 50.375
    with open(targetf, "w", encoding="utf-8") as af:
        for i in range(124 * 2):
            af.write(srctxt)

    print("日志文件创建完成，大小：{}".format(os.path.getsize(targetf)))


def retn_data(files: tuple, start_line, end_line):
    count = 1
    for file in files:
        with open(file, "r", encoding="utf-8") as filerf:
            outf = os.path.join("tmp", f"tmp{count}.log")
            with open(outf, "w", encoding="utf-8") as outfwf:
                writed = False
                fnum = None
                for line in filerf:
                    if re.search(start_line, line):
                        if not writed:
                            line = line + "↑-此行是开始标记\n"
                            writed = True
                        else:
                            # 没有遇见结束标记之前再次遇见开始标记，则更新开始标记
                            # 俩字：难搞
                            pass

                    if re.search(end_line, line):
                        line = line + "↑-此行是结束标记\n"
                        fnum = 6
                        writed = False

                    if writed:
                        outfwf.write(line)

                    if isinstance(fnum, int) \
                            and fnum > 0:
                        outfwf.write(line)
                        fnum -= 1

                    if isinstance(fnum, int) \
                            and fnum < 0 \
                            and not writed:
                        fnum = None
                        # break

        count += 1


def retn_nolist(files, start_line, end_line):
    """获取最近两个开始与结束标记之间的日志"""
    for file in files:
        nolist = []
        with open(file, "r", encoding="utf-8") as filerf:
            for no, line in enumerate(filerf, start=1):
                if re.search(start_line, line):
                    if nolist and nolist[-1][0] != 'e':
                        nolist.pop()
                    nolist.append(("s", no))  # 开始标记行
                if re.search(end_line, line):
                    if nolist and nolist[-1][0] == 'e':
                        continue
                    nolist.append(("e", no))  # 结束标记行
        return nolist


def pair_values(data):
    # 提取所有的数值
    values = [item[1] for item in data]

    # 确保总数是偶数，才能成对处理
    if len(values) % 2 != 0:
        raise ValueError("列表中的元素数量不是偶数，无法成对组合")

    # 将数值两两分组
    result = [(values[i], values[i + 1]) for i in range(0, len(values), 2)]

    return result


def write_lines(file, snum, enum):
    with open(file, 'r', encoding="utf-8") as file:
        outf = os.path.join("tmp", "tmp.log")
        with open(outf, "w", encoding="utf-8") as outfwf:
            total_lines = enum - snum + 1  # 计算要处理的总行数
            line_count = 0  # 用来计数已读取的行

            for line in islice(file, snum - 1, enum + 5):
                line_count += 1
                # 第一个元素
                if line_count == 1:
                    line = line + "↑-此行是开始标记\n"
                # 倒数第五个元素到最后
                elif line_count == total_lines:
                    line = line + "↑-此行是结束标记\n"

                outfwf.write(line)


if __name__ == '__main__':
    make_log()
    # files = ("uwsgi.log", "TTT.log",)
    files = ("uwsgi.log",)
    start_line = r".*spawned uWSGI worker 2 \(pid: 32592, cores: 1\).*"
    end_line = (r".*\[pid: 32591\|app: 0\|req: 7/24\] 127.0.0.1 \(\) "
                r"\{34 vars in 673 bytes\} \[Tue Oct  8 21:08:28 2024\].*")
    # retn_data(files, start_line, end_line)
    nolist = retn_nolist(files, start_line, end_line)
    print(nolist)
    values = pair_values(nolist)
    print(values)
    write_lines(files[0], *values[0])
