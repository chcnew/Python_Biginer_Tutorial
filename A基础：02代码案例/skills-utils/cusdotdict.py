# _*_ coding: utf-8 _*_

"""
功能：
"""
import json5
from dotdict import dotdict


def get_dotdict(file):
    """get_dotdict"""
    with open(file, 'r', encoding='utf-8') as rf:
        option_config = dotdict(json5.load(rf))
    print(option_config.name)


class DotDict(dict):
    """DotDict"""

    def __init__(self, *args, **kwargs):
        super(DotDict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        value = self[key]
        if isinstance(value, dict):
            value = DotDict(value)
        return value
