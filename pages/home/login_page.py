from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time
import json

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    username_field = "//input[@placeholder='Email Id']"
    password_field = "//input[@placeholder='Password']"
    login_button = "//div[@class='button'][normalize-space()='Login']"
    # logout_button = '//div[@class='button'][normalize-space()='Login']'

    def enterEmail(self, username):
        self.sendKeys(username, self.username_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self.password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self.login_button, locatorType="xpath")

    def checkIfUserTokenStored(self):
        return self.getFromLocalStorage('user')

    def login(self, username, password):
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(2)
        data = self.checkIfUserTokenStored()
        print('here',data)
        if data is not None:
            parsed_data = json.loads(data)
            print('has data',parsed_data['token'])
            if parsed_data['token']:
                print('has user token')
            else:
                print('no user token')
        else:
            print('No user data found')
                
