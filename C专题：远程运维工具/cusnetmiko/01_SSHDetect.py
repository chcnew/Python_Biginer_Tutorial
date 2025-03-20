# _*_ coding: utf-8 _*_

"""
功能：
"""
import json

from netmiko import SSHDetect

with open("device.config") as fff:
    device = json.load(fff).get("ubuntu64")
sshd = SSHDetect(**device)
print(sshd.autodetect())
print(sshd.potential_matches)

# 结果：
# linux
# {'linux': 99}
