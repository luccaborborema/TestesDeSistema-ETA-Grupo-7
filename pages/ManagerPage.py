from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class ManagerPage(BasePage):
    url_login = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    btn_add_customer = (By.CSS_SELECTOR, '[ng-class="btnClass1"]')
    btn_open_account = (By.CSS_SELECTOR, '[ng-class="btnClass2"]')
    btn_customers = (By.CSS_SELECTOR, '[ng-class="btnClass3"]')

    def __init__(self, browser):
        super().__init__(driver=None, browser=browser)

    def open_page(self):
        self.driver.get(self.url_login)

    def is_url_manager(self):
        return self.is_url(self.url_login)

    def click_add_customer(self):
        self.driver.find_element(*self.btn_add_customer).click()

    def click_open_account(self):
        self.driver.find_element(*self.btn_open_account).click()

    def click_customers(self):
        self.driver.find_element(*self.btn_customers).click()