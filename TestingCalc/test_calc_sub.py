# !usr/bin/env python
# -*- coding:utf-8 _*-

import sys
from decimal import Decimal

import pytest

sys.path.append("..")

from calc_code.calc import Calculator


@pytest.mark.sub
@pytest.mark.parametrize("a, b, result", [
    (1, 1, 0),
    (Decimal("0.01"), Decimal("0.00002"), Decimal("0.00998")),
    (1000, -1001, 2001),
    ("1", 2, "请输入合法数据")],
    ids=["整数相减为正", "浮点型相减", "减数为负", "非法入参"])
def test_sub(a, b, result):
    """正常+非法 校验"""
    cal = Calculator()
    assert cal.sub(a, b) == result



