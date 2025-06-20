from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPage(BasePage):
    url_login = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    btn_selector = (By.CSS_SELECTOR, '.btn-lg')

    def __init__(self, browser):
        super().__init__(driver=None, browser=browser)

    def open_page(self):
        self.driver.get(self.url_login)

    def is_url_login(self):
        return self.is_url(self.url_login)

    def get_login_buttons(self):
        self.wait_for_element(self.btn_selector)
        return self.driver.find_elements(*self.btn_selector)

    def click_customer_login(self):
        self.get_login_buttons()[0].click()

    def click_bank_manager_login(self):
        self.get_login_buttons()[1].click()
