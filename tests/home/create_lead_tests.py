from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.home.lead_page import LeadPage
from pages.home.create_lead_page import CreateLeadPage
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LeadUserCreation(unittest.TestCase):

    def test_createLead(self):
        baseurl = "https://beta.arkaenergy.com/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)
        login_page = LoginPage(driver)
        login_page.login("CRM1beta@gmail.com", "CRM1beta@gmail.com")

        lead_page = LeadPage(driver)
        lead_page.openCreateLeadDialog()

        create_lead_page= CreateLeadPage(driver)
        create_lead_page.createLead()


    



        