# -*- coding: utf-8 -*-

"""
开启winrm命令（cmd）：

winrm quickconfig -q &
winrm enumerate winrm/config/listener &
winrm set winrm/config/service/auth @{Basic="true"} &
winrm set winrm/config/service @{AllowUnencrypted="true"} &
winrm get winrm/config/service/auth

"""

import json
import os
import sys
import time
from multiprocessing import Process
from socket import gaierror

import pandas as pd
import paramiko
import winrm
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException

import cuslogger
from cuslogger import LOG_ROOT

logger = cuslogger.get_logger("update_pkgname.log")


def get_middle_str(content, start, end):
    """
    获取中间字符串

    :param content: 内容
    :param start: 前面字符串
    :param end: 后面字符串
    :return:
    """
    start_index = content.index(start)
    if start_index >= 0:
        start_index += len(start)
    end_index = content.index(end)
    return content[start_index:end_index]


def retn_command_winrm(pkg_name: str):
    """windows远程winrm"""
    agent_name = pkg_name.replace("pkgname-", "")
    command = f"""
    python --version
    pytest --version
    echo "WinRM - UPDATING: {agent_name}"
    echo "ALL pkgname UNINSTALL"
    taskkill /f /im python.exe 1>nul 2>nul
    python -m pip install --upgrade pip
    pip uninstall -y pkgname
    echo "START UPDATE pkgname"
    pip install --trusted-host 192.168.127.150 --index-url http://192.168.127.150:8888/simple/ {pkg_name}
    reg add HKEY_CURRENT_USER\\Console /v QuickEdit /t REG_DWORD /d 00000000 /f
    """.strip().replace("\n    ", ";")
    return command


def retn_command_winssh(pkg_name: str):
    """windows远程ssh"""

    agent_name = pkg_name.replace("pkgname-", "")
    command = f"""
    python --version
    pytest --version
    echo "WinSSH - 正在更新: {agent_name}"
    echo "pkgname系列旧版本包全部卸载"
    taskkill /f /im python.exe
    python -m pip install --upgrade pip
    pip uninstall -y pkgname
    echo "pkgname系列包重新安装最新版本，请稍等..."
    pip install --trusted-host 192.168.127.150 --index-url http://192.168.127.150:8888/simple/ {pkg_name}
    reg add HKEY_CURRENT_USER\\Console /v QuickEdit /t REG_DWORD /d 00000000 /f
    """.strip().replace("\n    ", ";")
    return command


def retn_command_linuxssh(pkg_name: str):
    """linux远程ssh"""
    agent_name = pkg_name.replace("pkgname-", "")
    install = f"pip install --user --trusted-host 192.168.127.150 " \
              f"--index-url http://192.168.127.150:8888/simple/ {pkg_name}"
    command = f"""
    python --version
    pytest --version
    echo "LinuxSSH - 正在更新: {agent_name}"
    echo "pkgname系列旧版本包全部卸载"
    python3 -m pip install --upgrade pip
    pip uninstall -y pkgname
    pip uninstall -y pkgname-devicetest
    pip uninstall -y pkgname-devicetestagent
    pip uninstall -y pkgname-devicetestagent-cida
    pip uninstall -y pkgname-google
    pip uninstall -y pkgname-ohos
    pip uninstall -y pkgname-xy
    pip uninstall -y pkgname-xypytest
    echo "pkgname系列包重新安装最新版本，请稍等..."
    {install}
    echo "pkgname关闭进程"
    pgrep -f agent_main.py -u $USER | xargs kill -9
    pgrep -f {agent_name}  -u $USER | xargs kill -9
    source /root/pytest.bashrc >/dev/null 2>&1 ; source /root/HY/bin/sw/xy_env.sh >/dev/null 2>&1
    """.strip().replace("\n    ", ";")
    return command


def retn_config_data(file_path: str = "update_pkgname.xlsx"):
    """数据处理及返回"""
    data_frame = pd.read_excel(file_path, sheet_name="info")
    split_str = "-" * 100
    logger.info("\n{}\n{}\n{}".format(split_str, data_frame, split_str))
    logger.info("请确认要连接的机器信息(y/n)：")
    y_or_n = input()
    logger.info(y_or_n)
    if y_or_n not in ["Y", "y"]:
        logger.info("您选择n，即将退出！")
        sys.exit()
    config_data = json.loads(data_frame.to_json(orient="records"))
    res_list = []
    for data in config_data:
        res_dict = {}
        for key, value in data.items():
            new_key = key.strip()
            if isinstance(value, int):
                new_value = value
            else:
                new_value = value.strip().lower()
            res_dict[new_key] = new_value
        res_list.append(res_dict)
    return res_list


def retn_win_seesion(hostname: str, port: int, username: str, password: str):
    """
    windows获取远程会话对象

    :param hostname: 主机
    :param port: 端口
    :param username: 用户名
    :param password: 密码
    :return:
    """
    wintest = winrm.Session(
        'http://' + hostname + f':{port}/wsman', auth=(username, password))
    return wintest


def win_cmd(wintest, command: str, ):
    """远程调用 windows 执行命令

    :param wintest: 会话
    :param command: 命令

    :return:
    """
    res = wintest.run_cmd(command)
    if res.status_code == 0:
        res = res.std_out.decode().replace('\n', '').replace('\r', '')
        return {'sta': 200, 'res': res}
    return {'sta': 201, 'res': res.std_err}


def linux_shell(command: str, code_style: str, hostname: str, port: int, username: str,
                password: str, etime: int):
    """
    远程调用 linux 执行命令

    :param command: 命令
    :param code_style: windows_ssh: gbk; linux_ssh: utf-8
    :param hostname: 主机
    :param port: 端口
    :param username: 用户名
    :param password: 密码
    :param etime: 超时时间
    :return:
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)
    _, stdout, stderr = ssh.exec_command(command, timeout=etime)
    res, err = stdout.read(), stderr.read()
    logger.info("执行命令：{}".format(command))
    if not err:
        logger.info('status : 200')
        msg = str(res, encoding=code_style)
    else:
        logger.info('status : 201')
        msg = str(err, encoding=code_style)
    logger.info('message : {}'.format(msg))
    ssh.close()


def ssh_sub_process(command, hostname, port, username, password, etime=10):
    """
    windows创建子进程执行启动

    :param command: 命令
    :param hostname: ip
    :param port: 端口
    :param username: 用户名
    :param password: 密码
    :param etime: 超时时间
    :return:
    """
    sub_process = Process(target=linux_shell,
                          args=(command, "gbk", hostname, port, username, password, etime))
    logger.info(f"Start the version replacement subprocess. [Running {etime}s]")
    logger.info(f"Command：{command}")
    sub_process.start()
    time.sleep(etime)
    if sub_process.is_alive():
        logger.info("Stop the version replacement subprocess. [sub_process]")
        sub_process.terminate()


class Update:
    """Update"""

    def __init__(self, pkg_name: str = "pkgname-devicetestagent",
                 excel_file: str = "update_pkgname.xlsx"):
        """
        :param pkg_name: pkgname-devicetestagent 或 pkgname-devicetestagent-cida
        :param excel_file: 机器excel信息文件路径
        """
        self.pkg_name = pkg_name
        self.agent_name = pkg_name.replace("-", "").replace("pkgname", "")
        self.command_winrm = retn_command_winrm(pkg_name).split(";")
        self.command_winssh = retn_command_winssh(pkg_name).split(";")
        self.command_linuxssh = retn_command_linuxssh(pkg_name).split(";")
        self.config_data = retn_config_data(excel_file)

    @staticmethod
    def item_info(data: dict):
        """
        item_info

        :param data: 读取的数据
        :return: dict
        """
        data_dict = {
            "hostname": data.get("hostname"),
            "port": data.get("port"),
            "username": data.get("username"),
            "password": data.get("password"),
        }
        return data_dict

    @staticmethod
    def excucmd_err_write(file_obj, func, item):
        """
        执行命令与捕获异常

        :param file_obj: 文件
        :param func: 函数
        :param item: 字典数据
        :return:
        """
        try:
            func(item)
        except (NoValidConnectionsError, AuthenticationException, gaierror) as err:
            logger.info(str(err) + "\n\n")
            # 连接失败的ip写入文件
            line = "{}\t{}\t{}\t{}\t{}\t{}\n".format(item.get("hostname"),
                                                     item.get("port"),
                                                     item.get("username"),
                                                     item.get("password"),
                                                     item.get("password"),
                                                     item.get("systype"),
                                                     str(err))
            file_obj.writelines(line)

    def run(self):
        """启动入口"""
        file = os.path.join(LOG_ROOT, "logs", "FailedList.txt")
        with open(file, mode="w+", encoding="gbk") as info_file:
            for item in self.config_data:
                local_ip = item.get("hostname")
                logger.info("{} Current Host: {} {}".format("-" * 30, local_ip, "-" * 30))
                sys_type = item.get("systype")
                # winrm
                if sys_type == "windows" and str(item.get("port")) == "5985":
                    logger.info("WinRM:")
                    self.excu_winrm(self.item_info(item))
                # win-ssh
                elif sys_type == "windows" and str(item.get("port")) == "22":
                    logger.info("WinSSH:")
                    self.excucmd_err_write(info_file, self.excu_winssh, item)
                # linux-ssh
                elif sys_type == "linux" and str(item.get("port")) == "22":
                    logger.info("LinuxSSH:")
                    self.excucmd_err_write(info_file, self.excu_linuxssh, item)
                else:
                    raise ValueError("The input parameter is incorrect. Please check.")

    def excu_winrm(self, item):
        """执行winrm连接的命令"""

        wintest = retn_win_seesion(**self.item_info(item))
        # 远程获取agent包的位置
        content = win_cmd(wintest, "pip show {}".format(self.pkg_name)).get("res")
        pkg_location = get_middle_str(content, "Location: ", "Requires:")
        logger.info(pkg_location)
        # 获的启动bat绝对路径
        start_agent_bat = "{}\\{}\\start_agent.bat".format(pkg_location, self.agent_name)
        logger.info(start_agent_bat)
        for line in self.command_winrm:
            logger.info(win_cmd(wintest, line))
        # 启动命令
        winrm_excu_exe_cmd = 'winrm invoke create wmicimv2/win32_process -SkipCAcheck ' \
                             '-skipCNcheck @{{commandline="python -m {}"}}'.format(self.agent_name)
        logger.info(win_cmd(wintest, winrm_excu_exe_cmd))
        logger.info(win_cmd(wintest, "taskkill /f /im winrshost.exe 1>nul 2>nul"))

    def excu_winssh(self, item):
        """执行winssh连接的命令
        # winrm启动命令
        # winrm_excu_exe_cmd = 'winrm invoke create wmicimv2/win32_process -SkipCAcheck ' \
        #                      '-skipCNcheck @{{commandline="{}"}}'.format(start_cmd)
        # 测试链接代码
        # linux_shell("python -m pytest --version", code_style="gbk", etime=3, **self.item_info(item))
        """
        # if self.agent_name.endswith("cida"):
        #     start_cmd = "python -m {} {} {} {}".format(self.agent_name, item.get("server_port"),
        #                                                item.get("realtime_log_server_port"),
        #                                                item.get("product"))
        # else:
        #     start_cmd = "python -m {}".format(self.agent_name)
        # # 卸载安装
        # for line in self.command_winssh:
        #     linux_shell(line, "gbk", **self.item_info(item))
        # # 启动命令
        # ssh_sub_process(start_cmd, etime=3, **self.item_info(item))
        linux_shell("python -m pytest --version", code_style="gbk", etime=3, **self.item_info(item))

    def excu_linuxssh(self, item):
        """执行linuxssh连接的命令
        # 测试链接代码
        linux_shell("python3 -m pytest --version", code_style="utf-8", etime=3, **self.item_info(item))
        """
        # if self.agent_name.endswith("cida"):
        #     start_cmd = "python3 -m {} {} {} {}".format(self.agent_name, item.get("server_port"),
        #                                                 item.get("realtime_log_server_port"),
        #                                                 item.get("product"))
        # else:
        #     start_cmd = "python3 -m {}".format(self.agent_name)
        # for line in self.command_linuxssh:
        #     linux_shell(line, "utf-8", **self.item_info(item))
        # # 启动命令
        # linux_shell("nohup {} > ~/nohup.out 2>&1 &".format(start_cmd),
        #             "utf-8", **self.item_info(item))
        # 测试链接代码
        linux_shell("python3 -m pytest --version", code_style="utf-8", etime=3, **self.item_info(item))


if __name__ == '__main__':
    update = Update("pkgname-devicetestagent", "update_pkgname.xlsx")
    update.run()
