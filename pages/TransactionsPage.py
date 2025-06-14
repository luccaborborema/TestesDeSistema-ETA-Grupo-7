from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class TransactionsPage(BasePage):
    url_transactions = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_transactions(self):
        return self.is_url(self.url_transactions)