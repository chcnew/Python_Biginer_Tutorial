# _*_ coding: utf-8 _*_

"""
功能：
"""
from setuptools import setup

setup(
    name='snek',
    entry_points={
        'console_scripts': [
            'snek = snek:main',
        ],
    }
)
