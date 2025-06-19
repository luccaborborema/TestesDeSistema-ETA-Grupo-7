from pages.OpenAccountPage import OpenAccountPage
from pages.CustomersListPage import CustomersList

class Test9:
    def test_add_new_account_with_same_currency(self, create_customer_with_dollar):
        manager_page = create_customer_with_dollar

        manager_page.click_open_account()
        open_account_page = OpenAccountPage(manager_page.driver)
        assert open_account_page.is_url_open_account(), 'Página Open Account não encontrada!'

        open_account_page.select_customer("Amelie Silva")
        open_account_page.select_currency("Dollar")
        open_account_page.click_process()
        open_account_alert_text = open_account_page.get_alert_text()
        assert 'Account created successfully with account Number :' in open_account_alert_text, 'Texto inesperado no alerta'
        open_account_page.close_alert()

        manager_page.click_customers()
        customers_list_page = CustomersList(manager_page.driver)

        assert customers_list_page.is_url_customers_list(), 'Página Customers List não encontrada!'

        customers_list_page.type_customer('Amelie')
        assert customers_list_page.get_search_len() == 1, 'Cliente cadastrado não encontrado!'
        new_account = open_account_alert_text.split(":")[1].strip()
        assert customers_list_page.validate_account_number(new_account), 'Conta não encontrada'