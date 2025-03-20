# -*- coding: utf-8 -*-

"""
功能：
"""
import os

from setuptools import setup, find_packages, findall

INSTALL_REQUIRES = ["Flask==2.0.0"]


def get_relative_path(start: str, path_list: list):
    """获取某个包下的非.py文件相对路径,用于资源列表填写"""
    num = len(start)
    lst = []
    for item in path_list:
        if not item.strip().endswith(".py") and \
                (item.startswith(f"{start}\\") or item.startswith(f"{start}/")):
            lst.append(item[num + 1:])
    lst.insert(0, "*")
    return lst


def get_data(dir_path_list: list, resource_path_list: list):
    """构造填写资源文件的数据结构
    {
        "ttt": [
            "*",
            "realtime_log/static/plugins/xxx.yyy",
            "realtime_log/templates/xxx.yyy",
            "resource/xxx.yyy"
            ]
    }
    """
    data = {}
    for package_name in dir_path_list:
        fpath = get_relative_path(package_name, resource_path_list)
        data[package_name] = fpath
    return data


dirlist = [item for item in os.listdir() if os.path.isdir(item)]
package_data = get_data(dirlist, findall())


def main(req: list):
    """main"""
    setup(
        name="pkg_name",
        description="xxx",
        version="xxx",
        packages=find_packages(),
        package_data=package_data,
        zip_safe=False,
        include_package_data=False,
        install_requires=req,
        python_requires=">3.6,<3.10",
    )


if __name__ == "__main__":
    main(INSTALL_REQUIRES)
