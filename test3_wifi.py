
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



    def test_Wifi(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text = 'Preference']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text = '3. Preference dependencies']").click()

        #checkbox
        checboxes_list = self.driver.find_elements_by_class_name("android.widget.CheckBox")
        print(checboxes_list)
        self.assertEqual(len(checboxes_list), 1)

        is_checked_bool = False
        is_checked_value = self.driver.find_element_by_class_name("android.widget.CheckBox").get_attribute("checked")

        if is_checked_value == "false":
            print("Checkbox nie jest zaznaczony")
            self.driver.find_element_by_class_name("android.widget.CheckBox").click()
            is_checked_bool = True

        self.assertTrue(is_checked_bool)
        sleep(3)

        self.driver.back()
        self.driver.find_element_by_accessibility_id('3. Preference dependencies').click()

        is_checked_value = self.driver.find_element_by_class_name("android.widget.CheckBox").get_attribute("checked")
        if is_checked_value == "true":
            is_checked_bool =True
            self.assertEqual(is_checked_bool, True)
            print("Element jest zaznaczony")




        # czy checkbox jest zaznaczony ? jesli tak to nie zaznaczaj i daj wynik testu; OK ????



        #checboxes_list[0].click()
        #self.driver.find_elements_by_xpath("//android.widget.RelativeLayout")[1].click()
        #sleep(2)



        #self.driver.find_element_by_xpath(('//*[@class = "android.widget.RelativeLayout"]')
        #self.driver.find_element_by_class_name('android.widget.EditText').send_keys("1234")
        #self.driver.find_element_by_xpath('//android.widget.Button[@text="OK"]')





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)