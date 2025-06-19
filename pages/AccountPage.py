from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class AccountPage(BasePage):
    url_account_page = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    customer_name = (By.CSS_SELECTOR, "span.fontBig")
    no_account_message = (By.CSS_SELECTOR, "span[ng-show='noAccount']")

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_account_page(self):
        return self.is_url(self.url_account_page)

    def get_customer_name(self):
        welcome_message_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.customer_name)
        )
        return welcome_message_element.text if welcome_message_element.is_displayed() else None

    def get_no_account_message(self):
        welcome_message_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.no_account_message)
        )
        return welcome_message_element.text if welcome_message_element.is_displayed() else None