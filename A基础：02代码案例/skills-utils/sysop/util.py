# _*_ coding: utf-8 _*_

"""
功能：系统相关的操作
psutil是一个跨平台的Python库，用于获取有关进程和系统的信息，包括进程的状态、CPU、内存和磁盘使用情况等.
"""

import subprocess

import psutil


class Utils:

    @staticmethod
    def subprocess_execute(cwd, command):
        """
        :param cwd: 执行目录
        :param command: 执行命令
        :return:
        """
        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=cwd,
            universal_newlines=True,
            bufsize=1
        )
        count = 0
        for line in iter(proc.stdout.readline, b''):
            if count >= 5:
                break  # 连续5次输出为空内容，则退出循环。
            if line:
                res_line = line.replace("\n", "")
                if res_line:
                    print(res_line)
            else:
                count += 1

        # 获取.sh脚本执行结果，执行有误抛出异常终止任务
        if (command.endswith(".sh") or command.endswith(".bat")) \
                and proc.poll() != 0:
            _, err = proc.communicate(timeout=10)
            raise ValueError(err)

    @staticmethod
    def process_exists(pro: str or int):
        """
        获取进程是否存在

        :param pro:
        :return:
        """
        if not isinstance(pro, (str, int)):
            raise ValueError("Arguments can only be strings or integers.")

        # 检测进程是否存在
        for proc in psutil.process_iter():
            try:
                if isinstance(pro, str) and pro in proc.name():
                    return True, proc
                if isinstance(pro, int) and pro == proc.pid:
                    return True, proc
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False, None

    @staticmethod
    def retn_pkg_version(command):
        """获取某个包的版本号"""
        proc = subprocess.Popen(
            command,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        stdout, _ = proc.communicate(timeout=10)
        jstr_list = stdout.strip().split("\n")
        for item in jstr_list:
            if item.startswith("Version"):
                return item.split(":")[1]
        return None

    @staticmethod
    def get_middle_str(content, start, end):
        """
        获取两个字符串之间中间的字符串

        :param content: 全部内容
        :param start: 开头字符串
        :param end: 结尾字符串
        :return: str
        """
        start_index = content.index(start)
        if start_index >= 0:
            start_index += len(start)
        end_index = content.index(end)
        return content[start_index:end_index]


if __name__ == '__main__':
    # tf, pro = Utils.process_exists("nginx")
    # print(tf, pro)
    # Utils.subprocess_execute(".\\", ".\\eee.bat")
    # version = Utils.retn_pkg_version("pip show pytest")
    # print(version)
    print(Utils.get_middle_str('<div class="a">jb51.net</div>', '<div class="a">', '</div>'))
