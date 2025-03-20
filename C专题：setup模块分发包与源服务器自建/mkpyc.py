# -*- coding: utf-8 -*-

"""
功能：将包py文件编译为pyc出包
"""
import compileall
import os
import shutil


def mddir(fdir: str):
    """mddir"""
    with os.scandir(fdir) as entries:
        for entry in entries:
            if entry.is_dir():
                mddir(entry.path)
            if entry.is_file():
                if entry.name.endswith(".py"):
                    os.remove(entry.path)
                if entry.name.endswith(".pyc"):
                    cache_dir = os.path.dirname(entry.path)
                    upone_dir = os.path.dirname(cache_dir)
                    new_name = entry.name.split(".")[0] + "." + entry.name.split(".")[-1]
                    new_path = os.path.join(cache_dir, new_name)
                    os.rename(entry.path, new_path)
                    shutil.move(new_path, upone_dir)


def rmcache(fdir: str):
    """rmcache"""
    with os.scandir(fdir) as entries:
        for entry in entries:
            if entry.is_dir():
                if entry.name == "__pycache__":
                    os.system(f"rmdir /q /s {entry.path}")
                else:
                    rmcache(entry.path)


def run():
    """入口"""
    project_dir = os.path.dirname(__file__)
    fdir_list = [
        os.path.join(project_dir, "src")
    ]
    output_dir = os.path.join(project_dir, "ZZZ-output")
    for fdir in fdir_list:
        if os.path.exists(output_dir):
            os.system(f"del /f /q /s {output_dir}")
            os.system(f"rmdir /q /s {output_dir}")
        # 复制代码文件夹
        tardir = os.path.join(output_dir, os.path.split(fdir)[-1])
        shutil.copytree(fdir, tardir)
        # 编译复制文件夹
        for item in os.listdir(tardir):
            pkgdir = os.path.join(tardir, item)
            if os.path.isdir(pkgdir):
                compileall.compile_dir(pkgdir, maxlevels=20, force=True, optimize=2)
                mddir(pkgdir)
                rmcache(pkgdir)
        os.chdir(tardir)
        os.system("pkg.bat")


if __name__ == '__main__':
    run()
