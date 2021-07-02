import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_verify_title(self):
        self.assertEqual("OrangeHRM", self.driver.title)

    def test_login(self):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="B:\\SQA Preparation\\Unit Testing\\POM + HTML Report\\Reports"))
