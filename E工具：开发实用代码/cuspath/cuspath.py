# _*_ coding: utf-8 _*_

"""
功能：
"""

from pathlib import Path

path = Path("./__init__.py")

if __name__ == '__main__':
    # print(Path.cwd())
    print(path)
    print(path.absolute())
    print(path.name)
    print(path.is_dir())
    print(path.is_file())
    print(path.parent)
