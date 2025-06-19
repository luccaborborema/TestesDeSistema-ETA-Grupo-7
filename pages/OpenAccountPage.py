from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

class OpenAccountPage(BasePage):
    url_open_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    btn_process = (By.CSS_SELECTOR, '[type="submit"]')
    customer_select = (By.CSS_SELECTOR, 'select#userSelect')
    currency_select = (By.CSS_SELECTOR, 'select#currency')

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_open_account(self):
        return self.is_url(self.url_open_account)

    def select_customer(self, customer):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.customer_select)
        )
        select_element = self.driver.find_element(*self.customer_select)
        Select(select_element).select_by_visible_text(customer)

    def select_currency(self, currency):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.currency_select)
        )
        select_element = self.driver.find_element(*self.currency_select)
        Select(select_element).select_by_visible_text(currency)

    def click_process(self):
        self.driver.find_element(*self.btn_process).click()

    def get_alert_text(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
            alert = Alert(self.driver)
            return alert.text
        except TimeoutException:
            return None

    def close_alert(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
            alert = Alert(self.driver)
            alert.accept()
        except TimeoutException:
            print("Nenhum alerta foi encontrado para fechar.")