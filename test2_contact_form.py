
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
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit()

    def test_is_app1_installed(self):
       self.assertTrue(self.driver.is_app_installed('io.appium.android.apis'))

    def test_is_app2_installed(self):
        self.assertTrue(self.driver.is_app_installed('com.example.android.contactmanager'))

    def test_contact_form(self):

        self.driver.find_element_by_accessibility_id('Add Contact').click()
        #name
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactNameEditText').send_keys('Tadek')
        #phone
        phone  = self.driver.find_element_by_id('com.example.android.contactmanager:id/contactPhoneEditText')
        phone.send_keys('678123321')
        #email
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactEmailEditText').send_keys('data@data.com')

        #

        #savebutton
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactSaveButton').click()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)