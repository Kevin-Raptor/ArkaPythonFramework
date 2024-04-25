from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time
class PipelinePage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    x_path_nav_button = "//li[@id='sublistOne']//a[@href='#']"
    x_path_sub_nav_button="//a[normalize-space()='- Pipelines']"
    x_path_create_pipeline="//body/div[@id='app']/div[@id='leadManagement']/div[@id='container']/section[@class='right_section containerCRM']/div[@class='content_section']/section/div[@id='scroll-bar']/div[@class='cardDetails']/div[@class='cardDetails-inner']/div[4]/div[1]//*[name()='svg']"
    x_path_pipeline_input="//input[@placeholder='Enter Pipeline Name']"
    x_path_create_pipeline_button="//button[@class='el-button el-button--primary']"


    def redirectToPipelines(self): 
        print('working')
        self.elementClick(self.x_path_nav_button,locatorType='xpath')
        self.elementClick(self.x_path_sub_nav_button,locatorType='xpath')
  
    def openCreatePipeline(self):
        self.redirectToPipelines()
        element = self.elementClick(self.x_path_create_pipeline,locatorType='xpath')
        self.sendKeys('rrrrgwetwe', self.x_path_pipeline_input, locatorType="xpath")
        # time.sleep(5)
        create_data=self.elementClick(self.x_path_create_pipeline_button,locatorType='xpath')
        time.sleep(5)
        
    