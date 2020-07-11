# !usr/bin/env python
# -*- coding:utf-8 _*-
import pytest

from calc_code.calc import Calculator


@pytest.mark.div
@pytest.mark.parametrize("a, b, result", [
    (1, 1, 1), (1, 3, 0.3333333333333333),
    (0, 3, 0), (1, 0, "除数不能为0"), ("1", 2, "请输入合法参数")],
                         ids=["正常相除", "除不尽", "被除数为0", "除数为0", "输入非法数据"])
def test_div(a, b, result):
    assert Calculator().div(a, b) == result
