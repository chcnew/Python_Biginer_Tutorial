# _*_ coding: utf-8 _*_

"""
USER: Administrator
DATE: 2023/1/30
FILE: 1.read_xml.py
"""

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse("xml.xml")
    print(tree)
