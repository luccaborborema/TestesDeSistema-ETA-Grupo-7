from time import sleep
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

class AddCustomers(BasePage):
    url_add_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    input_first_name = (By.CSS_SELECTOR, '[ng-model="fName"]')
    input_last_name = (By.CSS_SELECTOR, '[ng-model="lName"]')
    input_post_code = (By.CSS_SELECTOR, '[ng-model="postCd"]')
    btn_add_customer = (By.CSS_SELECTOR, '[type="submit"]')

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_add_customer(self):
        return self.is_url(self.url_add_customer)

    def click_add_customer(self):
        self.driver.find_element(*self.btn_add_customer).click()

    def add_customer(self, first_name='Amelie', last_name='Silva', post_code='50000-000'):
        self.driver.find_element(*self.input_first_name).send_keys(first_name)
        self.driver.find_element(*self.input_last_name).send_keys(last_name)
        self.driver.find_element(*self.input_post_code).send_keys(post_code)
        sleep(1)
        self.click_add_customer()

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