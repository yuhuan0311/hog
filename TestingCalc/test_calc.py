# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: test_calc.py
@Time: 2020/7/11 16:09 
"""
import os
import sys
from decimal import Decimal

import pytest
import yaml

from calcCode.calc import Calculator

cal = Calculator()

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "testData", "calc_test.yaml")
data = yaml.safe_load(open(data_path))


class TestCalc:

    @pytest.mark.add
    @pytest.mark.parametrize("upAndDown", data["add"], ids=["整数相加为正", "浮点型相加", "相加为负", "非法入参"], indirect=True)
    def test_add(self, upAndDown):
        """加法——正常+非法 校验"""
        assert upAndDown[2] == cal.add(upAndDown[0], upAndDown[1])

    @pytest.mark.sub
    @pytest.mark.parametrize("upAndDown", data["sub"], ids=["整数相减为正", "减数为负", "非法入参"])
    def test_sub01(self, upAndDown):
        """减法——正常+非法 校验"""
        assert upAndDown[2] == cal.sub(upAndDown[0], upAndDown[1])

    @pytest.mark.sub
    def test_sub02(self):
        """减法——浮点型"""
        assert Decimal("0.00998") == cal.sub(Decimal("0.01"), Decimal("0.00002"))

    @pytest.mark.div
    @pytest.mark.parametrize("upAndDown", data["div"], ids=["正常相除", "除不尽", "被除数为0", "除数为0", "输入非法数据"])
    def test_div(self, upAndDown):
        assert upAndDown[2] == cal.div(upAndDown[0], upAndDown[1])

    @pytest.mark.multi
    @pytest.mark.parametrize("upAndDown", data["multi"], ids=["正常相乘", "负负为正", "str与整数相乘，输出1三次", "str与float相乘"])
    def test_multi01(self, upAndDown):
        assert upAndDown[2] == cal.multi(upAndDown[0], upAndDown[1])

    @pytest.mark.multi
    def test_multii02(self):
        """乘法——浮点型相乘"""
        assert Decimal("0.004") == cal.multi(Decimal("0.2"), Decimal("0.02"))


if __name__ == '__main__':
    pass
