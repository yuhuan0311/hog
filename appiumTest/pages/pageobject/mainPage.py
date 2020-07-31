# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: mainPage.py
@Time: 2020/7/28 09:25 
"""
import time

from appium.webdriver.common.mobileby import MobileBy

from appiumTest.pages.basemethod import BaseMethod
from appiumTest.pages.pageobject.contactPage import ContactPage

# 定位通讯录
locators = (MobileBy.XPATH, '//*[@text="通讯录"]')


class MainPage(BaseMethod):

    def goto_contact_page(self):
        """去往通讯录页面"""
        self.find_click(locators)
        # time.sleep(3)
        # element.click()
        return ContactPage(self.driver)
