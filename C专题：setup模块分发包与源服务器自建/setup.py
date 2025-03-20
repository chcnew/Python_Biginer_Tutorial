# coding=utf-8

import os
import shutil
import sys

from setuptools import setup, find_packages, findall

INSTALL_REQUIRES = [
    "kafka-python==2.0.2",
]


def get_data(dir_path_list: list, resource_path_list: list):
    """构造填写资源文件的数据结构
    {
        "ttt": [
            "*",
            "realtime_log/static/plugins/xxx.yyy",
            "realtime_log/templates/xxx.yyy",
            "resource_templates/xxx.yyy"
            ]
    }
    """

    def get_relative_path(start: str, path_list: list):
        """获取某个包下的非.py文件相对路径,用于资源列表填写"""
        num = len(start)
        lst = []
        for item in path_list:
            if item.endswith(".py"):
                path_list.remove(item)
                continue
            if item.startswith(f"{start}\\") or item.startswith(f"{start}/"):
                lst.append(item[num + 1:])
        lst.insert(0, "*")
        return lst

    data = {}
    for package_name in dir_path_list:
        fpath = get_relative_path(package_name, resource_path_list)
        data[package_name] = fpath
    return data


srcname = "src"
src_dirpath = os.path.join(os.path.dirname(sys.argv[0]), srcname)
resource_path_list = [item[4:] for item in findall()]

# 删除.egg-info文件夹
dirlist = os.listdir(src_dirpath)
for item in dirlist:
    if item.endswith(".egg-info"):
        shutil.rmtree(os.path.join(src_dirpath, item))
        dirlist.remove(item)


def main():
    """
    ttt 版本号修改说明：
        3.1.1 xxx
        3.2.0 xxx
    """
    setup(
        name='xdevice-ttt',
        description='plugin for ttt',
        version="3.2.0",
        package_dir={"": "src"},
        packages=find_packages(srcname),
        package_data=get_data(dirlist, resource_path_list),
        zip_safe=False,
        include_package_data=False,
        install_requires=INSTALL_REQUIRES,
        python_requires=">=3.7.4,<=3.8.5"
    )


if __name__ == "__main__":
    main()
