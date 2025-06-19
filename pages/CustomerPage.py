from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class CustomerPage(BasePage):
    url_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    name_select = (By.CSS_SELECTOR, 'select#userSelect')
    btn_login = (By.CSS_SELECTOR, "[type='submit']")

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_customer(self):
        return self.is_url(self.url_customer)

    def select_your_name(self, name):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.name_select)
        )
        select_element = self.driver.find_element(*self.name_select)
        Select(select_element).select_by_visible_text(name)

    def validate_login_is_visible(self):
        flag = False
        login_btn = self.driver.find_element(*self.btn_login)
        if login_btn.is_displayed():
            flag = True
        return flag

    def click_login(self):
        self.driver.find_element(*self.btn_login).click()