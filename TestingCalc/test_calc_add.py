# !usr/bin/env python
# -*- coding:utf-8 _*-

import sys
import pytest

sys.path.append("..")

from calc_code.calc import Calculator


@pytest.mark.add
@pytest.mark.parametrize("a, b, result", [
    (1, 1, 2),
    (0.01, 0.00002, 0.01002),
    (1000, -1001, -1),
    ("1", 2, "请输入合法数据")],
    ids=["整数相加为正", "浮点型相加", "相加为负", "非法入参"])
def test_add(a, b, result):
    """正常+非法 校验"""
    cal = Calculator()
    assert result == cal.add(a, b)
