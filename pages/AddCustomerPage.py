from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class AddCustomers(BasePage):
    url_add_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_login(self):
        return self.is_url(self.url_add_customer)

    def add_customer(self):
        return