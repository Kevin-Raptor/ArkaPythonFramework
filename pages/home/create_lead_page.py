from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class CreateLeadPage(SeleniumDriver):
     
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    x_path_name_input="//input[@placeholder='Enter Name']"
    x_path_email_input="//input[@placeholder='Enter Email ID']"
    x_path_phone_number_input="//input[@placeholder='Enter phone number']"
    x_path_probability_input="//input[@placeholder='Probabilty']"

    x_path_owner_select="//input[@placeholder='Select an Owner']"
    x_path_owner_select_list="//div[@x-placement='bottom-start']//li[1]"

    x_path_property_type_select="//input[@placeholder='Select a property type']"
    x_path_property_type_select_list="//div[@x-placement='bottom-start']//li[@class='el-select-dropdown__item']"

    x_path_lead_source_select="//input[@placeholder='Select a lead source type']"
    x_path_lead_source_select_list="//div[@x-placement='bottom-start']//li[@class='el-select-dropdown__item']"

    x_path_pipeline_select="//input[@placeholder='Select a Pipeline']"
    x_path_pipeline_select_list="//div[@x-placement='bottom-start']//li[@class='el-select-dropdown__item']"

    x_path_stage_select="//input[@placeholder='Select a Stage']"
    x_path_stage_select_list="//div[@x-placement='bottom-start']//li[@class='el-select-dropdown__item']"
    
    x_path_region_select="//input[@placeholder='Select a Reion']"
    x_path_region_select_list="//div[@x-placement='bottom-start']//li[@class='el-select-dropdown__item']"
    
    x_path_map_select="//input[@placeholder='Enter the property address']"
    x_path_map_select_list="//body[1]/div[8]/div[1]"

    x_path_close_date="//input[@placeholder='Select Date']"
    x_path_close_date_forward_button="//button[@aria-label='Next Month']"
    x_path_close_date_item="//span[normalize-space()='16']"

    x_path_deal_value="//input[@placeholder='Enter potential deal value']"

    x_path_tag_select="//button[@class='el-button el-button--default fixButton0']"
    x_path_tag_select_plus="//i[@class='el-icon-plus']"
    x_path_tag_select_item="//body/div[@class='el-select-dropdown el-popper']/div[@class='el-scrollbar']/div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]"

    x_path_create_button="//button[@class='el-button leadBtn el-button--primary']"
    x_path_cancel_button="//span[@class='cross']"


    def createLead(self):

        self.selectFirstItemOfDropDown(self.x_path_tag_select,self.x_path_tag_select_item,locatorType="xpath")
        time.sleep(2)

        self.sendKeys('Autobots2', self.x_path_name_input, locatorType="xpath")
        self.sendKeys('auto1@bots.com', self.x_path_email_input, locatorType="xpath")
        self.sendKeys('8310992030', self.x_path_phone_number_input, locatorType="xpath")
        self.sendKeys('98', self.x_path_probability_input, locatorType="xpath")
        self.selectFirstItemOfDropDown(self.x_path_owner_select,self.x_path_owner_select_list,locatorType="xpath")
        time.sleep(0.5)
        self.selectFirstItemOfDropDown(self.x_path_property_type_select,self.x_path_property_type_select_list,locatorType="xpath")
        time.sleep(0.5)
        self.selectFirstItemOfDropDown(self.x_path_lead_source_select,self.x_path_lead_source_select_list,locatorType="xpath")
        time.sleep(0.5)
        self.selectFirstItemOfDropDown(self.x_path_pipeline_select,self.x_path_pipeline_select_list,locatorType="xpath")
        time.sleep(0.5)
        self.selectFirstItemOfDropDown(self.x_path_stage_select,self.x_path_stage_select_list,locatorType="xpath")   
        
        # time.sleep(0.5)
        # self.selectFirstItemOfDropDown(self.x_path_region_select,self.x_path_region_select_list,locatorType="xpath")
        
        self.sendKeys('1111',self.x_path_map_select,locatorType="xpath")
        self.selectFirstItemOfDropDown(self.x_path_map_select,self.x_path_map_select_list,locatorType="xpath")


        # self.sendKeys('2023-11-11',self.x_path_close_date,locatorType="xpath")
        # self.elementClick(self.x_path_close_date,locatorType="xpath")
        # time.sleep(2)
        # self.elementClick(self.x_path_close_date_forward_button,locatorType="xpath")

        # input_field = self.driver.find_elements(By.CLASS_NAME, "available")
        # print(len(input_field))
        # input_field[len(input_field)-1].click()

       

        # self.elementClick(self.x_path_tag_select_item,locatorType="xpath")
        # items = self.driver.find_elements(By.CLASS_NAME,'available')
        # print(len(items))
        # items.click()
        # type=self.getByType(locatorType)
        # print(items)


        # self.selectFirstItemOfDropDown(self.x_path_tag_select,self.x_path_tag_select_item,locatorType="xpath")
        # time.sleep(0.5)

        self.sendKeys('20000',self.x_path_deal_value,locatorType="xpath")
        

        
        self.elementClick(self.x_path_create_button,locatorType='xpath')

        time.sleep(20)


        # owner_select.send_keys(" and some", Keys.ARROW_DOWN)
      


    