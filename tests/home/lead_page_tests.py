from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.home.lead_page import LeadPage as LeadPageObject
import unittest
import time

class LeadPage(unittest.TestCase):

    def test_sortLeadsByName(self):
        baseurl = "https://beta.arkaenergy.com/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)
        login_page = LoginPage(driver)
        login_page.login("CRM1beta@gmail.com", "CRM1beta@gmail.com")
        lead_page = LeadPageObject(driver)
        lead_page.redirectToLeadManagement()
        lead_page.sortByName()

        time.sleep(5)