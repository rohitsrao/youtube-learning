import unittest

from selenium import webdriver

class E2ETests(unittest.TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(options = self.options, executable_path = r'/home/rohit/Downloads/chromedriver')
        self.driver.get('http://localhost:5000')

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("heading").text
        self.assertEqual('Named Entity Finder', heading)

    def _find(self, val):
        return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"]')

    def tearDown(self):
        print('TearDown entered')
        self.driver.quit()

