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
    x_path_sorting_filter="//div[contains(text(),'Sort')]"
    x_path_sorting_filter2="//div[normalize-space()='Amount']"
    x_path_sorting_filter3="//div[@x-placement='right-start']//li[@value='Descending'][normalize-space()='Descending']"

    def redirectToLeadManagement(self): 
        self.elementClick(self.x_path_nav_button,locatorType='xpath')
  

    def openCreateLeadDialog(self):
        self.redirectToLeadManagement()
        element = self.elementClick(self.x_path_create_lead_button,locatorType='xpath')

    def sortByName(self):
        self.elementClick(self.x_path_sorting_filter,'xpath')
        # time.sleep(1)
        element = self.waitForElement(self.x_path_sorting_filter2,'xpath')
        
        # element.click()
        # time.sleep(1)
        # self.elementClick(self.x_path_sorting_filter3,'xpath')

       

        