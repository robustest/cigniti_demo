from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CignitHome(unittest.TestCase):

    desired_capabilities = {
                "browserName": "firefox",
                "version": "23",
                "platform":"LINUX",
                "hubUrl" : "http://127.0.0.1:4444/wd/hub"
                }

    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=CignitHome.desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.cigniti.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_basic(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try: self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Home\"]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual("Services", driver.find_element_by_link_text("Services").text)
        try: self.assertEqual("Industries", driver.find_element_by_link_text("Industries").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Smart Tools", driver.find_element_by_link_text("Smart Tools").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Resource Center", driver.find_element_by_link_text("Resource Center").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("About Us", driver.find_element_by_link_text("About Us").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Contact Us", driver.find_element_by_link_text("Contact Us").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Success Stories", driver.find_element_by_css_selector("div.content-right-item > span.block-title > h2.title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Media", driver.find_element_by_css_selector("#block-views-News-block_8 > div.content-right-item > span.block-title > h2.title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Client Speak", driver.find_element_by_css_selector("#block-multiblock-11 > div.content-right-item > span.block-title > h2.title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Video", driver.find_element_by_css_selector("#block-block-51 > div.content-right-item > span.block-title > h2.title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
