import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Test_case:

    def setup(self):

        desired_cap = {
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

    @pytest.mark.skip
    def test_justForReset(self):
        pass

    #@pytest.mark.skip
    def test_initAppInfo(self):
        # 初始化页面
        print("初始化页面")
        touchAction = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        window_height = window_rect['height']
        window_width = window_rect['width']
        start_x = window_width * 0.9
        end_x = window_width * 0.1
        y = window_height * 0.5

        time.sleep(2)
        for i in range(2):
            touchAction.press(x=start_x, y=y).move_to(x=end_x, y=y).release().perform().wait(2000)

        self.driver.find_element("xpath", '//*[@text="立即体验"]').click()
        # self.driver.find_element_by_xpath('//*[@text = "同意"]').click()
        self.driver.find_element("xpath", '//*[@text = "同意"]').click()

        pass

    #@pytest.mark.skip
    def test_loginFunc(self):
        print("登录功能")
        # 登录
        self.driver.find_element("id", "ai.argrace.oem:id/cetUserName").send_keys("13516610913")
        self.driver.find_element("id", "ai.argrace.oem:id/petPassword").send_keys('Mse123')
        self.driver.find_element("id", "ai.argrace.oem:id/cb_privacy").click()
        self.driver.find_element("id", 'ai.argrace.oem:id/btnLogin').click()

        # 获取位置权限
        location_permission = self.driver.find_element("xpath",
                                                       '//*[@package = "com.android.permissioncontroller" and @text = "仅使用期间允许"]')
        if location_permission.is_displayed():
            location_permission.click()
        # 获取读取文件内容权限
        readFile_permission = self.driver.find_element("xpath",
                                                       '//*[@package = "com.android.permissioncontroller" and @text = "允许"]')
        if readFile_permission.is_displayed():
            readFile_permission.click()

        pass

    def test_CreatNewHome(self):

        self.driver.find_element("id","ai.argrace.oem:id/hello_account").click()
        self.driver.find_element("id", "ai.argrace.oem:id/btn_family_manage").click() #点击"家庭管理"
        self.driver.find_element("id", "ai.argrace.oem:id/menu_item_new_item").click() #点击新建
        self.driver.find_element("id","ai.argrace.oem:id/cet_new_family_name").send_keys("新家庭001")


        pass

    def teardown(self):
        pass


if __name__ == '__main__':
    pytest.main()
