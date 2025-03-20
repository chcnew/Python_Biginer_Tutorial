# _*_coding: utf-8 _*_

"""
功能：
"""

import pytest


class TestCases:
    lst = ['%03d' % i for i in range(5)]

    @pytest.mark.parametrize("test_msg", lst)
    def test_muticases(self, test_msg):
        print(test_msg)
        assert test_msg == 5
