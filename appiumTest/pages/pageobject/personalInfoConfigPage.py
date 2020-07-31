# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: personalInfoConfigPage.py
@Time: 2020/7/28 07:56 
"""
from appium.webdriver.common.mobileby import MobileBy

from appiumTest.pages.basemethod import BaseMethod
from appiumTest.pages.pageobject.editMemeberPage import EditMemeberPage

locator = (MobileBy.XPATH, "//*[@text='编辑成员']")

class PersonalInfoConfigPage(BaseMethod):
    def goto_edit_member_page(self):
        """去往编辑成员页"""
        self.find_click(locator)
        return EditMemeberPage(self.driver)
