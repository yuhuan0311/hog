# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: testyaml.py
@Time: 2020/7/11 17:55 
"""
import os

import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "testData", "calc_test.yaml")
data = yaml.safe_load(open(data_path))
print(data)
