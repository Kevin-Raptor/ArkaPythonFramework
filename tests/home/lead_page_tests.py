from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.home.lead_page import LeadPage
import unittest

class LeadPage(unittest.TestCase):

    def test_redirect_to_leadManagement(self):
        print(a)