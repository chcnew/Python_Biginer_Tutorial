# -*- coding: utf-8 -*-

"""
功能：解析xml
"""
import json
import os
import stat
from xml.dom.minidom import parseString

import dict2xml
import xmltodict


def dict_to_xml(dict_in: dict, xml_out: str):
    xml_str = dict2xml.dict2xml(dict_in)
    xml_raw = '<?xml version="1.0" encoding="utf-8"?>\n' + '<xml>\n' + xml_str + '\n</xml>'
    dom = parseString(xml_raw.replace('\n', ''))  # xml_raw中有\n换行，但不美观
    pretty = dom.toprettyxml(indent="    ", newl="\n", encoding="utf-8")  # bytes
    with open(xml_out, 'w', encoding="utf-8") as f:
        f.write(pretty.decode("utf-8"))


def dict_to_xml_str(dict_in: dict, xml_out: str):
    """Turn a simple dict of key/value pairs into XML"""
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key, val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)


def dict_to_xml_cus(tag: dict, d):
    """Turn a simple dict of key/value pairs into XML"""
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key, val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)


def retn_single_data(single_dict):
    xml_list = []
    for key, value in single_dict.items():
        if key.startswith("@"):
            xml_list.append(' {}={}'.format(key.replace("@", ""), value))
    return "".join(xml_list)


def dict_to_xml_custom(idx, simple_dict, xml_list):
    # @字段数据
    aet = retn_single_data(simple_dict)
    for key, value in simple_dict.items():
        if not key.startswith("@"):
            xml_list.insert(idx, f"<{key} {aet}>")
            xml_list.insert(len(xml_list) - idx, f"</{key}>")
            idx += 1
        else:
            continue
        # 递归处理
        if isinstance(value, dict):
            dict_to_xml_custom(idx, value, xml_list)
        if isinstance(value, list):
            for item in value:
                dict_to_xml_custom(idx, item, xml_list)


def rename_key(simple_dict):
    for key, value in simple_dict.items():
        new_key = key.replace("__", "@")
        simple_dict[new_key] = simple_dict.pop(key)
        # # 递归处理
        if isinstance(value, dict):
            rename_key(value)
        if isinstance(value, list):
            for item in value:
                rename_key(item)


if __name__ == '__main__':
    # lll = []
    # lll.insert(0, "<111>")
    # lll.insert(len(lll), "</111>")
    # lll.insert(1, "<222>")
    # lll.insert(len(lll) - 1, "</222>")
    # lll.insert(2, "<333>")
    # lll.insert(len(lll) - 2, "</333>")
    # lll.insert(3, "<444>")
    # lll.insert(len(lll) - 3, "</444>")
    # print("".join(lll))

    flags = os.O_RDWR | os.O_CREAT  # 设置文件读写方式
    modes = stat.S_IWUSR | stat.S_IRUSR  # 设置文件权限
    aff = "./TestTiccAutoDemo_001.xml"
    with os.fdopen(os.open(aff, os.O_RDWR | os.O_CREAT, stat.S_IWUSR | stat.S_IRUSR),'r', encoding="utf-8") as r_file:
        xml_str = r_file.read()
    json_parse = xmltodict.parse(xml_str, encoding="utf-8")
    simple_dict = json.loads(json.dumps(json_parse))
    print(simple_dict)

    # dict_to_xml(simple_dict, 'res.xml')
    with os.fdopen(os.open('res.xml', flags, modes), 'r', encoding="utf-8") as r_file:
        xml_str = r_file.read()
    # # xml_str = xml_str.replace("<__", "<@").replace("</__", "</@")
    json_parse = xmltodict.parse(xml_str, encoding="utf-8")
    simple_dict = json.loads(json.dumps(json_parse["xml"]))
    # simple_dict = json_parse["xml"]
    # rename_key(simple_dict)
    print(simple_dict)
    # # print(json_parse)
