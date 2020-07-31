# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: test_delete_memeber.py
@Time: 2020/7/28 09:31 
"""

from appiumTest.pages.basemethod import BaseMethod
from appiumTest.pages.pageobject.app import App


class TestDeleteMemeber:
    """
    删除成员
    """
    def setup_class(self):
        self.app = App()

    def test_delete_contact(self):
        result = self.app.start().main().goto_contact_page().goto_findcontact("测试").goto_personal_info_page().\
            goto_edit_member_page().delete_member()
        assert result.is_deleted()
