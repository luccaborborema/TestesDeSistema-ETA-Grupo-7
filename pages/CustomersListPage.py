from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class CustomersList(BasePage):
    url_customers_list = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    input_search = (By.CSS_SELECTOR, '[ng-model="searchCustomer"]')

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_customers_list(self):
        return self.is_url(self.url_customers_list)

    def type_customer(self, customer):
        self.driver.find_element(*self.input_search).send_keys(customer)

    def get_search_len(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        print(f'len(rows): {len(rows)}')
        return len(rows)