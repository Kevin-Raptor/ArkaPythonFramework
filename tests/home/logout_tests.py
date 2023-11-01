from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.logout_page import LogoutPage
from pages.home.login_page import LoginPage
import unittest
import time

class LogoutTests(unittest.TestCase):

    def test_logoutClearsData(self):
        baseurl = "https://beta.arkaenergy.com/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)
        loginpage = LoginPage(driver)
        loginpage.login("CRM1beta@gmail.com", "CRM1beta@gmail.com")
        time.sleep(2)
        logoutPage = LogoutPage(driver)
        logoutPage.logout()

        
        # if dashboardLogo is not None:
        #     print("Login Successful")
        # else:
        #     print("Login Failed")
