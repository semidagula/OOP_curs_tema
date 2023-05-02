def test_invalid_login(self):
    self.assertEqual(self.driver.find_element(*self.text).text,
                     'This is where you can log into the secure area. Enter tomsmith for the '
                     'username and SuperSecretPassword! for the password. If the information is '
                     'wrong you should see error messages.')


def valid_login(self):
    self.driver.find_element(*self.user).send_keys('tomsmith')  # * despachetare unpacking
    self.driver.find_element(*self.pwd).send_keys('SuperSecretPasswork')
    self.driver.find_element(*self.button).click()
    self.driver.implicitly_wait(3)


def tear_down(self) -> None:
    self.driver.quit()

# TODO importam locatorii intr o clasa specifica
# TODO migram si testele in modulul 9 sa le migram in module 9oop
