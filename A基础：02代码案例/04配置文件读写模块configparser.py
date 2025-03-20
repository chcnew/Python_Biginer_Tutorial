# -*- coding: utf-8 -*-

import configparser
import json


class IniParser(configparser.ConfigParser):
    """解析ini文件为python字典"""

    def as_dict(self):
        """转为字典"""
        return {**{"DEFAULT": self._defaults}, **self._sections}


if __name__ == '__main__':
    configer = IniParser()
    configer.sections()
    configer.read("./test-resource/example.ini", encoding="utf-8")
    print(json.dumps(configer.as_dict(), indent=2, ensure_ascii=False))

    sections = configer.sections()
    print(type(sections), ":", sections)

    configer["TEST"] = {"name": "ccplayer", "age": 28, "job": "IT"}
    print(configer.as_dict())

    with open("./test-resource/example-new.ini", "w", encoding="utf-8") as w_fff:
        configer.write(w_fff)
