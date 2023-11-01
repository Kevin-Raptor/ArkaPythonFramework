from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time
import json
class LogoutPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def checkIfUserTokenStored(self):
        return self.getFromLocalStorage('user')

    def logout(self):
        time.sleep(2)

        #locators
        logout_button="//img[@class='Group-1544']"

        dashboardButton = self.elementClick(logout_button,locatorType="xpath")
     
        time.sleep(2)
        data = self.checkIfUserTokenStored()
        if data is not None:
            print('User token not cleared')
        else:
            print('User token cleared')

        