# -*- coding: utf-8 -*-

from math import cos, sin, atan2, sqrt, radians, degrees


def center_geolocation(geolocations):
    """
    输入多个经纬度坐标，找出中心点
    :param geolocations: 集合
    :return:
    """
    x = 0
    y = 0
    z = 0
    length = len(geolocations)
    for lon, lat in geolocations:
        lon = radians(float(lon))
        lat = radians(float(lat))
        x += cos(lat) * cos(lon)
        y += cos(lat) * sin(lon)
        z += sin(lat)

    x = float(x / length)
    y = float(y / length)
    z = float(z / length)

    return degrees(atan2(y, x)), degrees(atan2(z, sqrt(x * x + y * y)))


if __name__ == '__main__':
    lst = [(112.977324, 28.178376), (112.975782, 28.172258), (112.975782, 28.172258)]
    print(center_geolocation(lst))
