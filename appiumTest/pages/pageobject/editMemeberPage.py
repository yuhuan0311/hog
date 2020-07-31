# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: editMemeberPage.py
@Time: 2020/7/28 07:58 
"""
# from appiumTest.pages.pageobject.contactPage import ContactPage
from appium.webdriver.common.mobileby import MobileBy

from appiumTest.pages.basemethod import BaseMethod

"""编辑成员页"""

# 定位删除成员
delete_memeber = (MobileBy.XPATH, "//*[@text='删除成员']")
# 点击确定按钮
sure_delete = (MobileBy.XPATH, "//*[@text='确定']")


class EditMemeberPage(BaseMethod):
    def delete_member(self):
        """在编辑成员页删除个人信息"""
        self.find_click(delete_memeber)
        self.find_click(sure_delete)
        # 删除完成后return至搜索页
        from appiumTest.pages.pageobject.contactPage import ContactPage
        return ContactPage(self.driver)
