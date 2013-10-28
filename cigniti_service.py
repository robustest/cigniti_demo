from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CignitiService(unittest.TestCase):

    desired_capabilities = {
                "browserName": "firefox",
                "appID" : "appID",
                "version": "23",
                "platform":"LINUX",
                "hubUrl" : "http://127.0.0.1:4444/wd/hub"
                }


    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=CignitiService.desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.cigniti.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_serviceGrid(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Services").click()
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Test Center of Excellence\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Test the Cloud\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Mobile Testing\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Bigdata Testing\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"test-advisory-services\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Functional Testing\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Automation Testing\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Performance Testing\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Regression Testing\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Compatibility Testing\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Globalization Testing\"]").text)
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Security Testing\"]").text)


    def test_sideLink(self):
        driver = self.driver
        driver.get(self.base_url + "/services")
        try: self.assertEqual("Services", driver.find_element_by_css_selector("div.content-right-col2-item > span.block-title > h2.title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Test Center of Excellence", driver.find_element_by_link_text("Test Center of Excellence").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Test the Cloud", driver.find_element_by_link_text("Test the Cloud").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Mobile Testing", driver.find_element_by_link_text("Mobile Testing").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Big Data Testing", driver.find_element_by_link_text("Big Data Testing").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Test Advisory Services", driver.find_element_by_link_text("Test Advisory Services").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Functional Testing", driver.find_element_by_link_text("Functional Testing").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Functional Testing", driver.find_element_by_link_text("Functional Testing").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Automation Testing", driver.find_element_by_link_text("Automation Testing").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Performance Testing", driver.find_element_by_link_text("Performance Testing").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Regression Testing", driver.find_element_by_link_text("Regression Testing").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Compatibility Testing", driver.find_element_by_link_text("Compatibility Testing").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Globalization Testing", driver.find_element_by_link_text("Globalization Testing").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Security Testing", driver.find_element_by_link_text("Security Testing").text)
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
