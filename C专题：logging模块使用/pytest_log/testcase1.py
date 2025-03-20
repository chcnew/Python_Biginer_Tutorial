#!/bin/bash/python3
# _*_ coding: utf-8 _*_

import time


def run(log_path):
    count = 0
    position = 0

    with open(log_path, mode='r', encoding='utf8') as f1:
        while True:
            line = f1.readline().strip()
            if line:
                count += 1
                print("count %s line %s" % (count, line))

            cur_position = f1.tell()  # 记录上次读取文件的位置

            if cur_position == position:
                time.sleep(0.1)
                continue
            else:
                position = cur_position
                time.sleep(0.1)


if __name__ == "__main__":
    log_path = "log.log"
    run(log_path)
