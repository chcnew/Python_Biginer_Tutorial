#!/bin/bash/python3
# _*_ coding: utf-8 _*_

import time
import random
from multiprocessing import Process


def get_line(log_path):
    position = 0

    with open(log_path, mode='r', encoding='utf-8') as rf:
        while True:
            line = rf.readline().strip()
            if line:
                print(line)

            cur_position = rf.tell()  # 记录上次读取文件的位置

            if cur_position == position:
                time.sleep(0.1)
                continue
            else:
                position = cur_position
                time.sleep(0.1)


def wtxt(log_path):
    while True:
        with open(log_path, "a", encoding="utf-8") as wf:
            lines = ["123\n", "456\n", "789\n", "我去去去\n靠靠！\n"]
            tttx = random.choice(lines)
            wf.write(tttx)
            time.sleep(2)


if __name__ == "__main__":
    log_path = "log.log"
    p1 = Process(target=wtxt, args=(log_path,))
    p1.start()
    p2 = Process(target=get_line, args=(log_path,))
    p2.start()
