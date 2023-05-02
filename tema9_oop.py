"""This module provides functionality to check multiple data from a web page."""
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TesttLogin(unittest.TestCase):
    """
        This class is used for testing the authentication functionality of the application.

        This test case contains several test methods that check different aspects of the
        authentication process, such as:
        - verification of authentication with a valid user and password
        - verification of authentication with an invalid user
        - verification of authentication with an invalid password
        - checking that the user is redirected to the correct page after authentication
        """
    user = (By.ID, 'username')
    username = (By.XPATH, '//*[@id="login"]/div[1]/div/label')
    pwd = (By.ID, 'password')
    password = (By.XPATH, '//*[@id="login"]/div[2]/div/label')
    button = (By.CLASS_NAME, 'radius')
    text = (By.XPATH, "//h2[normalize-space()='Login Page']")
    login_button = (By.XPATH, "/html/body/div[2]/div/div/h2")
    page_title = (By.XPATH, '//*[@id="content"]/div/h2')
    valHref = (By.XPATH, 'html/body/div[3]/div/div/a')
    logging_error = (By.XPATH, '//*[@id="flash"]')
    close_error = (By.XPATH, '// *[ @ id = "flash"] / a')
    text2 = (By.ID, 'flash')
    secure_area = (By.XPATH, '/html/body/div[2]/div/div/h2')
    log_out = (By.XPATH, '//*[@id="content"]/div/a/i')
    flash = (By.CLASS_NAME, 'flash success')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.driver.maximize_window()

    def test1_valid_url(self):
        """implementing the authentication verification test with the new url"""
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected)

    def test2_page_title(self):
        """implementation of the authentication verification test page title"""
        self.assertEqual(self.driver.find_element(*self.page_title).text, 'Login Page')

    def test3(self):
        """implementing the test to verify the correctness of the element xpath=//h2"""
        self.assertEqual(self.driver.find_element(*self.text).text, 'Login Page')

    def test4_login_button(self):
        """implementation of the login button verification test"""
        self.assertEqual(self.driver.find_element(*self.login_button).is_displayed(), True)

    def test5(self):
        """implementation of the test to verify the correctness of the href attribute in the link
        'Elemental Selenium'"""
        self.assertEqual(self.driver.find_element(*self.valHref).get_attribute("href"),
                         "http://elementalselenium.com/")

    def test6(self):
        """implementation of the error verification test that occurred when logging in without
        a username and password"""
        self.driver.find_element(*self.button).click()
        self.assertEqual(self.driver.find_element(*self.logging_error).is_displayed(), True)

    def test7(self):
        """implementation of the error verification test that occurred when logging in with
        an invalid username and password. check that the message displayed is the expected one"""
        self.driver.find_element(*self.user).send_keys('ana')
        self.driver.find_element(*self.pwd).send_keys('bala')
        self.driver.find_element(*self.button).click()
        self.assertTrue(self.driver.find_element(*self.text), 'Your username is invalid!')

    def test8(self):
        """implementation of the authentication verification test with invalid username
        and password, verification of the disappearance of the error that appeared after
        clicking on x"""
        self.driver.find_element(*self.button).click()
        self.driver.find_element(*self.close_error).click()
        self.assertEqual(self.driver.find_element(*self.logging_error).is_displayed(), True)

    def test9(self):
        """implementing the test to verify the correctness of the text on the labels"""
        labels_list = ["Username", "Password"]
        self.assertEqual(labels_list[0], "Username")
        self.assertEqual(labels_list[1], "Password")

    def test10(self):
        """implementation of the new url verification test and appearance
        of the 'flash success' element, after logging in with a valid username and password."""
        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.pwd).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.button).click()
        assert "/secure" in self.driver.current_url
        success_flash = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "flash.success")))
        assert success_flash.is_displayed()

    def test11(self):
        """implementing the url verification test after logging in with a valid username
         and password"""
        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.pwd).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.button).click()
        self.driver.find_element(*self.log_out).click()
        actual = self.driver.current_url
        self.assertEqual(actual, 'https://the-internet.herokuapp.com/login')

    def test12_brut_force_pwd_hacking(self):
        """implementing the password verification test, taking each word from a
         string in turn until we find the correct password"""
        lista = self.driver.find_element(By.TAG_NAME, "h4").text.split()
        logg_in = False

        for word in range(len(lista)):
            self.driver.find_element(*self.user).send_keys('tomsmith')
            self.driver.find_element(*self.pwd).send_keys(lista[word])
            self.driver.find_element(*self.button).click()
            loggin_confirmation = self.driver.find_element(*self.secure_area).text
            if loggin_confirmation == 'Secure Area':
                logg_in = True
                print(f'The password was found and it is {lista}')
                break
        assert logg_in == True

    def tearDown(self) -> None:
        self.driver.quit()
