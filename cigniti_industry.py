from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CignitiIndustry(unittest.TestCase):
    desired_capabilities = {
                "browserName": "firefox",
                "appID" : "appID",
                "version": "23",
                "platform":"LINUX",
                "hubUrl" : "http://127.0.0.1:4444/wd/hub"
                }
    def setUp(self):
	self.driver = webdriver.Remote(desired_capabilities=CignitiIndustry.desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.cigniti.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_cignit_industry(self):
        driver = self.driver
        driver.find_element_by_link_text("Industries").click()
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='content-body']/div/div/p[3]/img").text)
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
