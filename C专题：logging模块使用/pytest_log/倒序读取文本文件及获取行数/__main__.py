#!/bin/bash/python3
# _*_ coding: utf-8 _*_

"""
从文本文件最后一行往上读取
"""

import os
from typing import List


class BackwardsReader:
    """Read a file line by line, backwards"""
    BLKSIZE = 4096

    def __init__(self, file):
        """
        :param file: 文件句柄
        """
        self.file = file
        self.buf = ""
        self.file.seek(-1, 2)
        self.trailing_newline = 0
        lastchar = self.file.read(1)
        if lastchar == "\n":
            self.trailing_newline = 1
            self.file.seek(-1, 2)

    def readline(self):
        while 1:
            newline_pos = str.rfind(self.buf, "\n")
            pos = self.file.tell()
            if newline_pos != -1:
                # Found a newline
                line = self.buf[newline_pos + 1:]
                self.buf = self.buf[:newline_pos]
                if pos != 0 or newline_pos != 0 or self.trailing_newline:
                    line += "\n"
                return line
            else:
                if pos == 0:
                    # Start-of-file
                    return ""
                else:
                    # Need to fill buffer
                    toread = min(self.BLKSIZE, pos)
                    self.file.seek(-toread, 1)
                    self.buf = self.file.read(toread).decode('utf-8') + self.buf
                    self.file.seek(-toread, 1)
                    if pos - toread == 0:
                        self.buf = "\n" + self.buf


class Utils:
    """Utils类"""

    @staticmethod
    def get_last_lines(file_path: str, num: int) -> List[str]:
        """
        获取最后num行

        :param file_path: 文件路径
        :param num: 行数
        :return: 最后num行的内容
        """
        # 获取文件句柄
        with open(file_path, "rb") as rf:
            br = BackwardsReader(rf)
            count = 1
            content = []
            for i in range(40):
                if count >= 5:
                    break
                line = br.readline()
                if line:
                    content.insert(0, line)
                else:
                    count += 1
        return content


if __name__ == "__main__":
    content = Utils.get_last_lines("../log.log", 40)
    for idx, line in enumerate(content):
        if idx == 0:
            line = line.replace("\r", "\r\n")
        print(line)
