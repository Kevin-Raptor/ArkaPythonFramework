from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time
class LeadPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    x_path_nav_button = "//a[@href='/leadmanagement']"
    x_path_search_input = "//input[@class='searchInput']"
    x_path_create_lead_button = "//span[normalize-space()='Create Lead']"

    def redirectToLeadManagement(self): 
        self.elementClick(self.x_path_nav_button,locatorType='xpath')
  

    def openCreateLeadDialog(self):
        self.redirectToLeadManagement()
        element = self.elementClick(self.x_path_create_lead_button,locatorType='xpath')

       

        