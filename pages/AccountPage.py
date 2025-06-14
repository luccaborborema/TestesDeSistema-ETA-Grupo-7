from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class AccountPage(BasePage):
    url_account_page = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_account_page(self):
        return self.is_url(self.url_account_page)