import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    user = (By.ID, 'username')
    pwd = (By.ID, 'password')
    Button = (By.CLASS_NAME, 'radius')
    text = (By.CLASS_NAME, 'subheader')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.driver.maximize_window()

    def test_invalid_login(self):
        self.assertEqual(self.driver.find_element(*self.text).text, 'This is where you can log into the secure area. ' \
                                                                    'Enter tomsmith jifor the username and SuperSecretPassword! for the password. ' \
                                                                    'If the information is wrong you should see error messages.')

        self.driver.find_element(*self.user).send_keys('Andreea')
        self.driver.find_element(*self.pwd).send_keys('tot')
        self.driver.find_element(*self.Button).click()
        self.driver.implicitly_wait(3)
        time.sleep(5)

    def test_valid_login(self):
        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.pwd).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.Button).click()
        self.driver.implicitly_wait(3)
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.quit()

# TODO locatorii sa fie intr-O cLasa specifica - gen login locators (variabilele)
# TODO si testele pe care le faceam in modul 9 sa le migram in Module 9OOP
