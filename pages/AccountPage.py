from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class AccountPage(BasePage):
    url_account_page = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    customer_name = (By.CSS_SELECTOR, "span.fontBig")
    no_account_message = (By.CSS_SELECTOR, "span[ng-show='noAccount']")
    btn_transactions_menu = (By.CSS_SELECTOR, '[ng-class="btnClass1"]')
    btn_deposit_menu = (By.CSS_SELECTOR, '[ng-class="btnClass2"]')
    btn_withdraw_menu = (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
    btn_confirm = (By.CSS_SELECTOR, "button[type='submit']")
    input_amount = (By.CSS_SELECTOR, '[ng-model="amount"]')
    deposit_message = (By.CSS_SELECTOR, 'span[ng-show="message"]')
    account_info = (By.CSS_SELECTOR, "div.center strong.ng-binding")


    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_account_page(self):
        return self.is_url(self.url_account_page)

    def get_customer_name(self):
        welcome_message_element = self.wait_for_element(self.customer_name)
        return welcome_message_element.text if welcome_message_element.is_displayed() else None

    def get_no_account_message(self):
        welcome_message_element = self.wait_for_element(self.no_account_message)
        return welcome_message_element.text if welcome_message_element.is_displayed() else None

    def click_transactions_menu(self):
        self.driver.find_element(*self.btn_transactions_menu).click()

    def click_deposit_menu(self):
        self.driver.find_element(*self.btn_deposit_menu).click()

    def click_withdraw_menu(self):
        self.driver.find_element(*self.btn_withdraw_menu).click()

    def click_confirm(self):
        self.driver.find_element(*self.btn_confirm).click()

    def make_deposit(self, value):
        self.click_deposit_menu()
        amount_element = self.wait_for_element(self.input_amount)
        amount_element.send_keys(value)
        self.click_confirm()

     def make_withdraw(self, value):
        self.click_withdraw_menu()
        amount_element = self.wait_for_element(self.input_amount)
        amount_element.send_keys(value)
        self.click_confirm()

    def get_deposit_message(self):
        welcome_message_element = self.wait_for_element(self.deposit_message)
        return welcome_message_element.text if welcome_message_element.is_displayed() else None

    def get_withdraw_message(self):
        welcome_message_element = self.wait_for_element(self.withdraw_message)
        return welcome_message_element.text if welcome_message_element.is_displayed() else None

    def get_balance(self):
        self.wait_for_element((By.CSS_SELECTOR, "div.center"))
        account_elements = self.driver.find_elements(By.CSS_SELECTOR, "div.center strong.ng-binding")
        return int(account_elements[1].text.strip())
