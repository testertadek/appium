
# -*- coding: utf-8" -*


import os
import unittest
from appium import webdriver
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
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit()

    title = False
    body =  False

    def test_Wifi(self):
        self.driver.open_notifications()
        notifications = self.driver.find_elements_by_class_name("android.view.View")
        assert(len(notifications) >1)
        print(len(notifications))
        notification_exists = False
        for notification in notifications:
            text_in_notification = notification.find_elements_by_class_name('android.widget.TextView')
            print(len(text_in_notification))
            for el in notification:
                if el.text == 'USB debugging connected':
                    title = True
                elif el.text =="Tap to disable USB debugging.":
                    body = True

        self.assertEqual(notification_exists, True)









if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)