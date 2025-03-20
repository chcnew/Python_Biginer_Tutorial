# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
linux默认已经存在ssh服务，不用操作。

windows需要先在机器开启WinRM服务：
查看->开启（需要输入两次y）->Basic参数设置->AllowUnencrypted参数设置->查看配置
winrm enumerate winrm/config/listener
winrm quickconfig
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/service  '@{AllowUnencrypted="true"}'
winrm get winrm/config/service/auth
"""

import json
import os
import sys
import time
from multiprocessing import Process

import paramiko
import winrm

import logger_config

logger = logger_config.get_logger("updateXdevice.log")


class Update:
    """Update"""

    def __init__(self, info: list):
        """
        :param info: 信息列表
        """
        self.info = info
        for item in self.info:
            # 端口为区分系统的标识
            port = item.get("port")
            if str(port) == "22":
                self.update_ssh(**item)
            elif str(port) == "5985":
                # 使用Git拉取最新代码及工具
                self.update_winrm(**item)
                # 执行run.bat更新xdevice系列包
                para = tuple(item.values())
                self.runbat_sub_process(
                    r"""
                    d: &
                    pip3 install -r D:\DeviceTestTools\xdevice\tools\requirements.txt --trusted-host mirrors.aliyun.com -i https://mirrors.aliyun.com/pypi/simple &
                    cd D:\DeviceTestTools\xdevice\ &
                    start /b run.bat
                    """,
                    10,
                    *para
                )
                # 执行start_agent.bat后台启动DeviceTestAgent
                self.runbat_sub_process(
                    r"""
                    d: &
                    cd D:\DeviceTestTools\devicetestagent\ &
                    start /b start_agent.bat
                    """,
                    5,
                    *para
                )
                # 关闭远程winrm全部会话
                self.close_winrm(**item)
            else:
                raise TypeError("The host information is incorrect.")

    @staticmethod
    def update_ssh(hostname, port, username, password):
        """
        linux更新xdevice及agent

        :param hostname: 主机
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # paramiko.util.log_to_file("updateXdevice.log")
        ssh.connect(hostname, port, username, password)

        cmd = """
        echo "Remove xdevice/tools and mkdir temp"
        rm -rf /usr/local/temp >/dev/null
        rm -rf /usr/local/xdevice/tools >/dev/null
        mkdir /usr/local/temp >/dev/null
        
        echo "Git Global Settings"
        echo "https://xxx" > ~/.git-credentials
        git config --global credential.helper store
        git config --global http.sslVerify false
        
        echo "Pull devicetestagent and xdevice/tools/"
        cd /usr/local/temp
        git init
        git config core.sparsecheckout true
        git remote add devicetools https://xxx
        echo devicetestagent/ > ./.git/info/sparse-checkout
        echo xdevice/tools/ >> ./.git/info/sparse-checkout
        git pull devicetools master
        """

        cmd1 = """
        kill -9 \`pgrep -f agent_main.py\` >/dev/null 2>&1
        sleep 1
        rm -rf /usr/local/devicetestagent
        cp -r /usr/local/temp/devicetestagent /usr/local/
        cp -r /usr/local/temp/xdevice/tools /usr/local/xdevice/
        /bin/bash /usr/local/xdevice/run.sh
        sleep 3
        bashrcPath="/root/pytest.bashrc"
        if [ ! -f "$bashrcPath" ]; then source "$bashrcPath"
        fi
        nohup python3 /usr/local/devicetestagent/agent_main.py >/dev/null 2>&1 &
        """
        # 拉取代码
        stdin, stdout, stdee = ssh.exec_command(cmd)
        logger.info(stdout.read())
        logger.info(stdee.read())

        # 重启agent
        stdin, stdout, stdee = ssh.exec_command(cmd1)
        logger.info(stdout.read())
        logger.info(stdee.read())

        ssh.close()

    @staticmethod
    def update_winrm(hostname, port, username, password):
        """
        windows更新xdevice及agent

        :param hostname: 主机
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        session = winrm.Session(f"{hostname}:{port}", auth=(username, password), transport='ntlm')
        command = fr"""
        D: &
        echo "****** Shutdown DeviceTestAgent Server ******" &
        taskkill /f /im python.exe 2>nul 1>nul &
        echo "****** Remove folder 【D:\temp\】" &
        rd /s/q "D:\temp\" &
        echo "****** Create temp folder "D:\temp" ******" &
        mkdir "D:\temp" &
        cd "D:\temp" &
        echo "****** Pull the latest xdevice and devicetestagent ******" &
        set /p="https://xxx" <nul > "C:\Users\{username}\.git-credentials" &
        git init &
        git config --system --unset credential.helper &
        git config core.sparsecheckout true &
        git config --global http.sslVerify false &
        git config --global credential.helper store &
        git remote add devicetools "https://xxx" &
        echo devicetestagent/* > .\.git\info\sparse-checkout &
        echo xdevice/tools/* >> .\.git\info\sparse-checkout &
        git pull devicetools master &
        echo "****** Copy 【xdevice\tools\ packages】 ******" &
        copy /y D:\temp\xdevice\tools\* D:\DeviceTestTools\xdevice\tools &
        echo "****** Remove old 【devicetestagent】and copy the latest ******" &
        rd /s/q "D:\DeviceTestTools\devicetestagent\" &
        copy /y D:\temp\xdevice\tools\* D:\DeviceTestTools\xdevice\tools &
        echo "****** Copy 【devicetestagent】 packages ******" &
        xcopy D:\temp\devicetestagent D:\DeviceTestTools\devicetestagent\ /y /s &
        echo "****** Completed!  Now Install Latest XdevicePackags And Restart DeviceTestAgent . ******"
        """
        # 运行命令run_cmd/run_ps
        Update.excute_command_winrm(session.run_cmd, command)

    @staticmethod
    def close_winrm(hostname, port, username, password):
        """
        关闭winrm远端的进程

        :param hostname: 主机
        :param port: 端口
        :param username: 用户名
        :param password: 密码"""
        session = winrm.Session(f"{hostname}:{port}", auth=(username, password), transport='ntlm')
        Update.excute_command_winrm(session.run_cmd, r"D: & rd /s/q D:\temp\ & taskkill /f /im winrshost.exe 2>nul 1>nul")

    @staticmethod
    def excute_command_winrm(session_terminal, command):
        """
        执行cmd命令

        :param session_terminal: 会话使用的终端类型
        :param command: 命令
        :return:
        """
        ex_command = command.replace("\n", " ")
        result = session_terminal(ex_command)
        # code为0代表调用成功
        code = result.status_code
        # 根据返回码，获取响应内容（bytes）
        content = result.std_out if code == 0 else result.std_err
        # 转为字符串（尝试通过utf-8、GBK进行解码）
        try:
            result = content.decode("utf-8")
        except Exception as e:
            result = content.decode("GBK")
            logger.error(e)

        logger.info(result)

    @staticmethod
    def runbat_sub_process(command, etime, hostname, port, username, password):
        """
        创建子进程执行bat脚本

        :param command: 执行bat的命令
        :param etime: 执行时间（秒）
        :param hostname: 主机
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        session = winrm.Session(f"{hostname}:{port}", auth=(username, password), transport='ntlm')
        para = (session.run_cmd, command)
        sub_process = Process(target=Update.excute_command_winrm, args=para)
        logger.info(f"Start the version replacement subprocess. [Running {etime}s]")
        logger.info(f"Command：{command}")
        sub_process.start()
        time.sleep(etime)
        if sub_process.is_alive():
            logger.info("Stop the version replacement subprocess. [sub_process]")
            sub_process.terminate()


if __name__ == '__main__':
    config_path = os.path.join(logger_config.dirname, "updateXdevice.json")
    if not os.path.exists(config_path):
        # 如果不存在先创建配置文件
        info = [
            {"hostname": "0.0.0.0", "port": 22, "username": "root", "password": "123xxx"},
            {"hostname": "1.1.1.1", "port": 5985, "username": "root", "password": "456xxx"},
        ]
        with open(config_path, "w") as wf:
            wf.write(json.dumps(info))
        logger.info("JSON配置文件创建完成")
        logger.info("注意 - windows端口: 5985, linux端口: 22")
        sys.exit()

    with open(config_path, "r") as rf:
        content = rf.read()
    info = json.loads(content)
    up = Update(info)
