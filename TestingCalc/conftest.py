# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: conftest.py
@Time: 2020/7/11 11:44 
"""

import pytest


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture()
def upAndDown(request):
    print("*****【开始计算】*****")
    yield request.param
    print("*****【计算结束】*****")
