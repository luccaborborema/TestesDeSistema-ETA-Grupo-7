from pages.OpenAccountPage import OpenAccountPage
from pages.CustomersListPage import CustomersList

import time
import re

class Test7:
    def test_add_new_account_client_without_account(self, create_customer_without_account):
        login_page, manager_page = create_customer_without_account

        manager_page.click_open_account()
        open_account_page = OpenAccountPage(manager_page.driver)
        assert open_account_page.is_url_open_account(), 'Página Open Account não encontrada!'

        open_account_page.select_customer("Amelie Silva")
        open_account_page.select_currency("Dollar")
        open_account_page.click_process()
        open_account_alert_text = open_account_page.get_alert_text()

        match = re.search(r'\d+', open_account_alert_text)

        account_number = 0
        if match:
            account_number = int(match.group())
            assert isinstance(account_number, int), "The extracted value is not an integer"

        assert 'Account created successfully with account Number :' in open_account_alert_text, 'Texto inesperado no alerta'
        open_account_page.close_alert()

        manager_page.click_customers()
        customers_list_page = CustomersList(manager_page.driver)
        customers_list_page.type_customer('Amelie')
        assert customers_list_page.get_search_len() == 1, 'Cliente cadastrado não encontrado!'
        assert customers_list_page.validate_account_number(str(account_number)), 'Conta não encontrada'
