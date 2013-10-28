from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CignitiAboutUs(unittest.TestCase):

    desired_capabilities = {
                "browserName": "firefox",
                "appID" : "appID",
                "version": "23",
                "platform":"LINUX",
                "hubUrl" : "http://127.0.0.1:4444/wd/hub"
                }
    def setUp(self):
	self.driver = webdriver.Remote(desired_capabilities=CignitiHome.desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.cigniti.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_cigniti_about_us(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("About Us").click()
        try: self.assertEqual("About Us", driver.find_element_by_css_selector("div.content-right-col2-item > span.block-title > h2.title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("The Brand", driver.find_element_by_link_text("The Brand").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Who We Are", driver.find_element_by_link_text("Who We Are").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Management", driver.find_element_by_link_text("Management").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Infrastructure", driver.find_element_by_link_text("Infrastructure").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Offices / Locations", driver.find_element_by_link_text("Offices / Locations").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Partners", driver.find_element_by_css_selector("li.leaf.menu-mlid-2490 > a[title=\"Partners\"]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Clients", driver.find_element_by_link_text("Clients").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Life @ Cigniti", driver.find_element_by_link_text("Life @ Cigniti").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Corporate Social Responsibility", driver.find_element_by_link_text("Corporate Social Responsibility").text)
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
