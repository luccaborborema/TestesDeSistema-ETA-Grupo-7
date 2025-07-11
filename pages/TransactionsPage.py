from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class TransactionsPage(BasePage):
    url_transactions = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    amount_column = (By.CSS_SELECTOR, 'tbody tr:nth-of-type(1) td:nth-of-type(2)')
    t_type_column = (By.CSS_SELECTOR, 'tbody tr:nth-of-type(1) td:nth-of-type(3)')
    btn_reset = (By.XPATH, "//button[contains(@class, 'btn') and text()='Reset']")
    btn_back = (By.XPATH, "//button[contains(@class, 'btn') and text()='Back']")

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_transactions(self):
        return self.is_url(self.url_transactions)

    def validate_transaction(self, amount, t_type):
        flag = False
        amount_element = self.wait_for_element(self.amount_column)
        amount_text = amount_element.text.strip()
        t_type_element = self.wait_for_element(self.t_type_column)
        t_type_text = t_type_element.text.strip()

        if amount == int(amount_text) and t_type == t_type_text:
            flag = True
        return flag


    def click_back(self):
        self.driver.find_element(*self.btn_back).click()

    def click_reset(self):
        self.driver.find_element(*self.btn_reset).click()

    def get_transaction_len(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        return len(rows)