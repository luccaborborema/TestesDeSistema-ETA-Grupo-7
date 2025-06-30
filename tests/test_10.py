from pages.AddCustomerPage import AddCustomers
from pages.CustomerPage import CustomerPage
from pages.AccountPage import AccountPage
from pages.CustomersListPage import CustomersList
from pages.OpenAccountPage import OpenAccountPage
from pages.TransactionsPage import TransactionsPage

class Test10:
    def test_multiple_client_view(self, open_manager_page):
        login_page, manager_page = open_manager_page

        manager_page.click_customers()

        customers_list_page = CustomersList(manager_page.driver)
        assert customers_list_page.is_url_customers_list(), 'Página Customers List não encontrada!'

        assert customers_list_page.get_search_len() == 5, "Número de clientes mínimo não encontrado"

        assert customers_list_page.has_scroll() == False, "Página com scroll ativo."

        manager_page.click_add_customer()
        add_customer_page = AddCustomers(manager_page.driver)
        assert add_customer_page.is_url_add_customer(), 'Página Add Customer não encontrada!'
        add_customer_page.add_customer(first_name='Amelie', last_name="Silva")
        assert 'Customer added successfully with customer id :' in add_customer_page.get_alert_text(), 'Texto inesperado no alerta'
        add_customer_page.close_alert()

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
        assert customers_list_page.get_search_len() == 6, "Número de clientes mínimo não encontrado"

        assert customers_list_page.has_scroll(), "Página com scroll desativo."