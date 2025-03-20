# _*_ coding: utf-8 _*_

"""
python setup.py bdist_wheel
"""

from setuptools import setup

setup(
    name='cute_snek',
    entry_points={
        'snek_types': ['cute = cute_snek:cute_snek']
    }
)
