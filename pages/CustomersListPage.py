from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class CustomersList(BasePage):
    url_customers_list = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    input_search = (By.CSS_SELECTOR, '[ng-model="searchCustomer"]')
    accounts_column = (By.CSS_SELECTOR, 'tbody tr:nth-of-type(1) td:nth-of-type(4)')
    scroll_container = (By.CSS_SELECTOR, "div.marTop[style*='overflow: scroll']")
    delete_btn = (By.CSS_SELECTOR, '[ng-click="deleteCust(cust)"]')




    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_customers_list(self):
        return self.is_url(self.url_customers_list)

    def type_customer(self, customer):
        self.driver.find_element(*self.input_search).send_keys(customer)

    def delete(self):
        self.driver.find_element(*self.delete_btn).click()

    def get_search_len(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        return len(rows)

    def validate_account_number(self, account_number):
        flag = False
        accounts = self.driver.find_element(*self.accounts_column)
        spans = accounts.find_elements(By.TAG_NAME, 'span')
        span_texts = [span.text for span in spans]
        if account_number in span_texts:
            flag = True
        return flag

    def has_scroll(self):

        scroll_container = self.driver.find_element(*self.scroll_container)

        # Check if the element has vertical scroll
        has_scroll = self.driver.execute_script(
            "return arguments[0].scrollHeight > arguments[0].clientHeight;", scroll_container
        )

        print("Customer table has vertical scroll:", has_scroll)

        return has_scroll
