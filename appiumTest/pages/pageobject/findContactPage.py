# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: findContactPage.py
@Time: 2020/7/28 07:52 
"""
from appium.webdriver.common.mobileby import MobileBy

from appiumTest.pages.basemethod import BaseMethod
from appiumTest.pages.pageobject.personalInfoConfigPage import PersonalInfoConfigPage

locator = (MobileBy.ID, 'com.tencent.wework:id/h9p')

class FindContact(BaseMethod):
    def goto_personal_info_page(self):
        """去往个人信息页"""
        self.find_click(locator)
        return PersonalInfoConfigPage(self.driver)