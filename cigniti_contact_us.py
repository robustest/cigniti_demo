from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CignitiContactUs(unittest.TestCase):

    desired_capabilities = {
                "browserName": "firefox",
                "version": "23",
                "platform":"LINUX",
                "hubUrl" : "http://127.0.0.1:4444/wd/hub"
                }

    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=CignitiContactUs.desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.cigniti.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_basic_link_text(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Contact Us").click()
        try: self.assertEqual("Contact Us", driver.find_element_by_css_selector("div.content-right-item > span.block-title > h2.title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("info@cigniti.com", driver.find_element_by_id("edit-submitted-to").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("edit-submitted-name").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("edit-submitted-email").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("edit-submitted-LEADCF3").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("edit-submitted-description").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("India Office", driver.find_element_by_xpath("//div[@id='block-block-25']/div/div/div/div/table/tbody/tr[2]/td/p").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("marketing@cigniti.com", driver.find_element_by_css_selector("p.c-mail").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("lucy.dass@2020msl.com", driver.find_element_by_xpath("//div[@id='block-block-25']/div/div/div/div/table/tbody/tr[3]/td/p[7]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("info@cigniti.com", driver.find_element_by_xpath("//div[@id='block-block-25']/div/div/div/div/table/tbody/tr[3]/td/p[9]").text)
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
