import unittest

from selenium import webdriver

class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'/home/rohit/Downloads/chromedriver')
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()
