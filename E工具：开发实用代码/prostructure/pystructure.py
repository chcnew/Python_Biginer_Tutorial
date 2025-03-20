# -*- coding: utf-8 -*-

"""
该模块可以配合亿图脑图MindMaster
"""

import os
import shutil
import time


class Utils:
    """方法类"""

    @staticmethod
    def readmylines(f, newline=""):
        """大文件生成器读取"""
        buf = ""
        while True:
            while newline and newline in buf:
                pos = buf.index(newline)  # 找到字符的位置
                yield buf[:pos]
                buf = buf[pos + len(newline):]
            chunk = f.read(4096 * 5)  # 读取相应的字符长度
            if not chunk:
                # 说明已经读到文件结尾
                yield buf
                break
            buf += chunk


class Structure:
    """获取文件夹内全部py文件函数级结构"""

    def __init__(self, dir_path):
        self.dir_path = dir_path

    @property
    def pyfile_list(self):
        """全部py文件的路径列表"""
        res_list = []
        for root, dirs, files in os.walk(self.dir_path, topdown=False):
            for name in files:
                if name.endswith(".py"):
                    res_list.append(os.path.join(root, name))
        return res_list

    @staticmethod
    def cls_func_list(pyfile):
        """py文件里面的类与函数列表"""
        context = ""
        with open(pyfile, "r", encoding="utf-8") as r_file:
            for line in r_file.readlines():
                sline = line.strip()
                if sline.endswith(":"):
                    if sline.startswith("class ") or sline.startswith("def "):
                        if "(" in sline:
                            line = line.split("(")[0] + "\n"
                        else:
                            line = line.split(":")[0] + "\n"
                        myline = " " * 8 + line
                        context += myline
        return context


class ExecPyDirs:
    """处理多个文件夹"""

    def __init__(self, head, pydir_list, outf_name=None):
        """
        :param head: 目标包的上一级路径
        :param pydir_list: 需要查看那些包的结构
        :param outf_name: 导出文件名，可以自定义文件名，如果向自定义到处文件夹，填写形式：outfiles/output，必须是“/”分隔
        """
        self.head = head
        self.pydir_list = pydir_list
        if not outf_name:
            self.outf_name = "outfiles/output"
            outdir = "outfiles"
            if os.path.exists(outdir):
                os.removedirs(outdir)
            shutil.rmtree(outdir)
        else:
            self.outf_name = outf_name
            outdir = outf_name.split("/")[0]
            if os.path.exists(outdir):
                shutil.rmtree(outdir)
            os.makedirs(outdir)

    def run(self):
        """执行函数"""
        name_list = ["Apath", "Bpyf"]  # 包 路径 py文件名
        f_out_list = ["{}_{}".format(self.outf_name, name) for name in name_list]
        # 清理上次结果文件
        for file in f_out_list:
            if os.path.exists(file):
                os.remove(file)
        # 遍历文件夹列表处理
        timestr = time.strftime("%Y%m%d-%H%M%S")
        apath_list = []
        for pydir in self.pydir_list:
            pro_name = os.path.split(pydir)[1]  # 文件夹名
            ssplit = " " * 4
            # 输出文件名
            af = "{}_{}_{}.txt".format(f_out_list[0], pro_name, timestr)
            bf = "{}_{}_{}.txt".format(f_out_list[1], pro_name, timestr)
            # 写如文件
            w_file0 = open(af, "a+", encoding="utf-8")
            w_file1 = open(bf, "a+", encoding="utf-8")
            structure = Structure(pydir)
            ppath = ""
            for item in structure.pyfile_list:
                if item.endswith("__init__.py"):
                    continue
                spath = str(item.split(pro_name, 1)[1])  # 相对文件夹名的路径
                pyfile_list = list(os.path.split(spath))
                pyfile_list[0] = pyfile_list[0] + "\\"
                # Apath文件写入
                if not apath_list or apath_list[-1].strip() != pyfile_list[0].strip():
                    w_file0.write(pyfile_list[0] + "\n")
                    apath_list.append(pyfile_list[0])
                s1 = pyfile_list[0] + "\n"
                s2 = ssplit + pyfile_list[1] + "\n"
                s3 = structure.cls_func_list(item)
                if ppath != s1:
                    # Bpyf文件写入
                    content = s1 + s2 + s3
                    ppath = s1
                else:
                    content = s2 + s3
                w_file1.write(content)
            w_file0.close()
            w_file1.close()


if __name__ == '__main__':
    # head = r"D:\PythonProjects"
    # head = r"F:\My_Study\1.Python_learning\2.Python_Biginer_Tutorial_51zxw\C专题：远程运维系列工具"
    head = r"D:\python3\Lib\site-packages\netmiko"
    # pydir_list = [rf"{head}\exam"]
    pydir_list = [rf"{head}\linux"]
    execpydirs = ExecPyDirs(head, pydir_list, outf_name="outfiles/output")
    execpydirs.run()
    print("脚本运行完成，文件列表：")
    for item in os.listdir("outfiles"):
        print(item)
