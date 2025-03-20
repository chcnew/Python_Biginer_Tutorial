#!/bin/bash/python3
# _*_ coding: utf-8 _*_

"""
pytest -vs test_out.py | tee myoutput.log
"""

import time

import pytest
import os


def test_func1():
    assert True
    time.sleep(5)


def test_func2():
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(args=['-vs', os.path.abspath(__file__)])


