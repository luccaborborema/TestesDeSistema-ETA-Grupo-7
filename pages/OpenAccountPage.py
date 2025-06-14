from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class OpenAccountPage(BasePage):
    url_open_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_open_account(self):
        return self.is_url(self.url_open_account)