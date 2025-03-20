# -*- coding: utf-8 -*-

"""
功能：
"""
import json
import os
import pathlib
import platform


def print_sysinfo():
    print("全部信息：", platform.uname())
    print("操作系统名称：", platform.system())
    print("操作系统版本：", platform.release())
    print("操作系统详细版本信息：", platform.version())
    print("底层硬件架构：", platform.machine())
    print("处理器信息：", platform.processor())
    print("计算机的网络名称：", platform.node())


def retn_linux_system_info():
    """retn_linux_system_info"""
    info = {}
    if platform.system() == "Windows":
        info = {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "node": platform.node(),
            "uname": platform.uname()
        }
    else:
        with open("/etc/os-release", "r", encoding="utf-8") as r_fff:
            for line in r_fff.readlines():
                if not line.strip():
                    continue
                slist = line.strip().split("=")
                info[slist[0].replace("'", "")] = slist[1].replace("'", "").replace("\"", "")
        with open(os.path.join(pathlib.Path.home(), "os-release-info.json"), "w",
                  encoding="utf-8") as w_fff:
            json.dump(info, w_fff, indent=2)
    return info


if __name__ == '__main__':
    info = retn_linux_system_info()
    print(json.dumps(info, indent=2))
