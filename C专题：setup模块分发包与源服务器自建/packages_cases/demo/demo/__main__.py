#!/bin/bash/python3
# _*_ coding: utf-8 _*_
import os.path
import sys

print(sys.path)
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
print(sys.path)
from demo import test
import pytest

if __name__ == '__main__':
    test()
