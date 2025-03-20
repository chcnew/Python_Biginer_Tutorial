#!/bin/bash/python3
# _*_ coding: utf-8 _*_

import paramiko

host_list = [
    {"hostname": "192.168.127.150", "port": "22", "username": "root", "password": "数据库密码"},
]

for item in host_list:
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在~/.ssh/known_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    hostname = item.get("hostname")
    port = item.get("port")
    username = item.get("username")
    password = item.get("password")
    # 连接服务器
    ssh.connect(
        hostname=hostname,
        port=port,
        username=username,
        password=password,
        timeout=10,
    )

    cmd = """
    apt-get update
    python3 --version
    """

    # 执行命令，不要执行top之类的在不停的刷新的命令(可以执行多条命令，以分号来分隔多条命令)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # stdin.write("终端等待输入...\n")  # test.py文件有input()函数，如果不需要与终端交互，则不写这两行
    # stdin.flush()

    # 获取命令结果
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode("utf-8")
    print(res)

    # 关闭服务器连接
    ssh.close()
