# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: basemethod.py
@Time: 2020/7/28 09:28 
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BaseMethod:
    def __init__(self, driver: WebDriver=None):
        self.driver = driver

    def find_text(self, locators):
        """查找并获取text"""
        return self.driver.find_element(*locators).text

    def find_click(self, locators):
        """查找并点击"""
        return self.driver.find_element(*locators).click()

    def send_keys(self, locators, value):
        """输入数据"""
        return self.driver.find_element(*locators).send_keys(value)

    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')
