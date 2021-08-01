import unittest

from selenium import webdriver

class E2ETests(unittest.TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(options = self.options, executable_path = r'/home/rohit/Downloads/chromedriver')
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)
