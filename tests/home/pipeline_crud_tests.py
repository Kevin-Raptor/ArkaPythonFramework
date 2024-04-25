import unittest
from pages.home.pipeline_crud_pages import PipelinePage
from selenium import webdriver
from pages.home.login_page import LoginPage

class Pipeline(unittest.TestCase):

    # def classSetup(self, oneTimeSetUp):
    #     self.login_page = LoginPage(self.driver)


    def test_createPipeline(self):
        baseurl = "https://beta.arkaenergy.com/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)
        login_page = LoginPage(driver)
        login_page.login("CRM1beta@gmail.com", "CRM1beta@gmail.com")
        pipeline_crud_pages = PipelinePage(driver)
        pipeline_crud_pages.openCreatePipeline()
        # print(pipeline_crud_pages)