# !usr/bin/env python
# -*- coding:utf-8 _*-
from decimal import Decimal

import pytest

from calc_code.calc import Calculator


@pytest.mark.multi
@pytest.mark.parametrize("a, b, result", [
    (1, 1, 1), (-1, -1, 1),
    (Decimal("0.2"), Decimal(" 0.2"), Decimal("0.04")),
    ("1", 3, "111"),
    ("1", 0.2, "请输入合法参数")],
    ids=["正常相乘", "负负为正", "float相乘", "str与整数相乘，输出1三次", "str与float相乘"])
def test_div(a, b, result):
    assert Calculator().multi(a, b) == result