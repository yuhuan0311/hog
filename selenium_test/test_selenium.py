# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: test_selenium.py
@Time: 2020/7/16 10:06 
"""
import os
from selenium import webdriver

class TestBrowser:
    """测试多浏览器选择"""
    def setup(self):
        browser = os.getenv("browser")
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        else:
            print("no this browser")

    def teardown(self):
        self.driver.quit()

    def test_getBrowser(self):
        self.driver.get("http://baidu.com")
        

