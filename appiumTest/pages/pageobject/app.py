# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: huan.yu
@File: app.py
@Time: 2020/7/22 07:38 
"""
from appium import webdriver

from appiumTest.pages.basemethod import BaseMethod
from appiumTest.pages.pageobject.mainPage import MainPage


class App(BaseMethod):
    def start(self):
        appPackage = "com.tencent.wework"
        appActivity = ".launch.WwMainActivity"
        desire_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": appPackage,
            "appActivity": appActivity,
            "noReset": "true",
            "skipServerInstallation": "true",
            "skipDeviceInitialization": "true",
            "dontStopAppOnReset": "false"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(3)
        return self

    def main(self):
        """入口函数"""
        return MainPage(self.driver)
