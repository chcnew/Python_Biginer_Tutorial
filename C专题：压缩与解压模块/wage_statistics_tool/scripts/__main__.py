#!/bin/bash/python3
# _*_ coding: utf-8 _*_


r"""
unrar.rarfile需要先到RARLab官方下载库文件，http://www.rarlab.com/rar/UnRARDLL.exe，
然后运行安装(或者解压)；安装最好选择默认路径，一般在 C:\Program Files (x86)\UnrarDLL\ 目录下；
然后重要的一步，就是添加环境变量，此电脑（我的电脑）右键，属性，找到 高级系统设置，
高级 选项卡下点击 环境变量，在系统变量（注意不是用户变量）中 新建，变量名输入 UNRAR_LIB_PATH ，
必须一模一样，变量值要特别注意！如果你是64位系统，就输入 C:\Program Files (x86)\UnrarDLL\x64\UnRAR64.dll，
如果是32位系统就输入 C:\Program Files (x86)\UnrarDLL\UnRAR.dll ，这个从unrar安装目录的内容也能看出来它是区分64和32位的。
"""

import os
import re
from datetime import datetime

import pandas as pd
from unrar import rarfile

BASE_DIR = os.path.dirname(__file__)
TOOL_DIR = os.path.dirname(BASE_DIR)


def decompression_rar(rardir, excdir, pwd=None):
    """
    解压指定文件夹的rar文件至指定的文件夹

    :param rardir: rar文件目录
    :param excdir: 解压文件目录
    :param pwd: 解压密码
    :return:
    """
    for rar in os.listdir(rardir):
        file_path = os.path.join(rardir, rar)
        print(file_path)
        rf = rarfile.RarFile(file_path)
        rf.extractall(path=os.path.join(excdir), pwd=pwd)
        print(f"{file_path}解压完成！")


def get_first_last_line(fname):
    """
    获取第一行与最后一行文本(大文件适用)

    :param fname: 文件路径
    :return:
    """
    with open(fname, 'r', encoding="utf-8") as f:  # 打开文件
        lines = f.readlines()  # 读第一行
        return lines[0], lines[-1]


def run(rarfiles="rarfiles"):
    print("-" * 58 + rarfiles + "-" * 58)
    rardir = os.path.join(TOOL_DIR, rarfiles)
    excdir = os.path.join(TOOL_DIR, "excfiles{}".format(rarfiles[-4:]))
    with open("conf.json") as fff:
        pwd = fff.read().strip()
    decompression_rar(rardir, excdir, pwd)
    txt_list = os.listdir(excdir)
    file_list = [os.path.join(excdir, name) for name in txt_list]
    # 获取title(最新的文件为准)
    # re匹配 "<TH width='130'>员工身份证号</TH><TH width='60'>E－HR编号</TH>"
    last_file = file_list[-1]
    print(f"{rarfiles} last html: {last_file}")
    _, last_file_last_line = get_first_last_line(last_file)
    last_file_title = re.findall(r"<TH width='.*?'>(.*?)</TH>", last_file_last_line)
    last_file_title.insert(0, "时间")
    print(f"last html title: {last_file_title}")
    result = []
    for file_path in file_list:
        _, last_line = get_first_last_line(file_path)
        # re匹配 ""
        title = re.findall(r"<TH width='.*?'>(.*?)</TH>", last_line)
        title.insert(0, "时间")
        data = re.findall(r"<TD class='.*?'>(.*?)</TD>", last_line)
        month = re.findall(r"<TITLE>(.*?)</TITLE>", last_line)
        data.insert(0, month[0])
        # 转为字典并加入result
        res_dict = dict(zip(title, data))
        result.append(res_dict)
    for item in result:
        for name in last_file_title:
            if not item.get(name):
                item[name] = "/"
    df = pd.DataFrame(result)
    nowtime = datetime.now().strftime("%Y%m%d%H%M%S")
    writer = pd.ExcelWriter(f"./工资记录{nowtime}.xlsx")
    df.to_excel(writer, sheet_name="工资记录")
    writer.close()


# run()
run(rarfiles="rarfiles")
