from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class CustomerPage(BasePage):
    url_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'

    def __init__(self, browser):
        super().__init__(driver=None, browser=browser)

    def is_url_customer(self):
        return self.is_url(self.url_customer)