# _*_coding: utf-8 _*_

"""
功能：
"""

import requests


def address_to_location(address):
    """将地址转换为经纬度
    :param address: 地址
    :return: 经度和维度
    """
    # 在高德地图开发者平台（https://lbs.amap.com/）申请的key，需要替换为自己的key
    parameters = {
        'key': '***f3cfdf1a2b0d8***',
        'address': address,
    }
    base = 'http://restapi.amap.com/v3/geocode/geo?'
    contest = requests.get(base, parameters).json()
    location = contest['geocodes'][0]['location']
    return location


if __name__ == '__main__':
    print(address_to_location("北京西站"))
