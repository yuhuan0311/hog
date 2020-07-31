# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: contactPage.py
@Time: 2020/7/28 07:31 
"""
from appium.webdriver.common.mobileby import MobileBy

from appiumTest.pages.basemethod import BaseMethod
from appiumTest.pages.pageobject.findContactPage import FindContact

"""通讯录页面"""

# 定位通讯录
contact_locator = (MobileBy.ID, "com.tencent.wework:id/h9z")
# 点击搜索
search_locator = (MobileBy.XPATH, '//*[@text="搜索"]')
# 点击搜索到的元素
locator = (MobileBy.ID, 'com.tencent.wework:id/d9v')
# 确认删除成功
text_locator = (MobileBy.XPATH, "//*[@text='确定']")

name = "测试"


class ContactPage(BaseMethod):
    """去往搜索页"""

    def goto_findcontact(self, name):
        """点击查找成员"""
        self.find_click(contact_locator)
        self.send_keys(search_locator, name)
        self.find_click(locator)
        return FindContact(self.driver)

    def is_deleted(self):
        """是否删除成功"""
        elems = self.find_text(text_locator)
        return "无" in elems
