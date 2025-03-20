# _*_ coding: utf-8 _*_

"""
功能：
"""
import re
import json
from netmiko import ConnectHandler


def escape_ansi(line):
    """正则表达式删除ANSI转义序列"""
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line)


with open("device.config") as fff:
    device = json.load(fff).get("ubuntu64")

# 连接远程发送命令
with ConnectHandler(**device) as conn:
    retmsg = conn.send_command("python3 --version")
    print(repr(retmsg))
    print(repr(escape_ansi(retmsg)))
    print(escape_ansi(retmsg).strip())
