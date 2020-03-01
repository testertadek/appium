import os
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit()


# funcje testujace:

    def test_gestures(self):
        self.assertTrue(self.driver.is_app_installed('io.appium.android.apis'))

        # Kliknij Views za pomoca tap() - tu zamiast click()
        el=self.driver.find_element_by_accessibility_id('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        self.driver.find_element_by_accessibility_id('Expandable Lists').click()
        self.driver.find_element_by_accessibility_id('1. Custom Adapter').click()
        el1= self.driver.find_element_by_xpath("//android.widget.TextView[@text='People Names']")
        el1.click()

        action.long_press(el1).release().perform()

        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Sample Action']").click()
        sleep(3)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)