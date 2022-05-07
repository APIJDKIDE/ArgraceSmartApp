import time

import pytest
from appium import webdriver
class Test_case:

    def setup(self):

        desired_cap ={
            'deviceName': 'huawei-cdy_tn90--V4DUT20508007711',
            'platformName': 'Android',
            'platformVersion': '10',
            'appPackage': 'ai.argrace.oem',
            'appActivity': 'ai.argrace.app.akeeta.main.Akeeta_SplashActivity',
            'noReset': True,
            'donStopOnReset': True
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_cap)
        self.driver.implicitly_wait(5)


    def test_login(self):
        print("登录接口")
        pass


if __name__ =='__main__':
    pytest.main()