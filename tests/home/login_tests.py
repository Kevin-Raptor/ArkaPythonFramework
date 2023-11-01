from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import time


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseurl = "https://dev.arkaenergy.com/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)
        loginpage = LoginPage(driver)
        loginpage.login("crm1@gmail.com", "crm1@gmail.com")

        # dashboardButton = driver.find_element(By.XPATH,"//img[@class='Group-1544']")
        # dashboardButton.click()

        # time.sleep(2.5)

        # local_storage_data = driver.execute_script("return window.localStorage.getItem('user')")


        # print(local_storage_data )
        # dashboardLogo = driver.find_element(By.XPATH,"//div[@class='selection-container el-popover__reference']//p[contains(text(),'Default Dashboard')]")


        # if dashboardLogo is not None:
        #     print("Login Successful")
        # else:
        #     print("Login Failed")

