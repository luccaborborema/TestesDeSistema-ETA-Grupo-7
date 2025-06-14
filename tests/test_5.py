from pages.AddCustomerPage import AddCustomers
from pages.CustomersListPage import CustomersList

class Test5:
    def test_add_customer(self, open_manager_page):
        login_page, manager_page = open_manager_page

        manager_page.click_add_customer()
        add_customer_page = AddCustomers(manager_page.driver)

        assert add_customer_page.is_url_add_customer(), 'Página Add Customer não encontrada!'
        add_customer_page.add_customer(first_name='Amelie')

        assert 'Customer added successfully with customer id :' in add_customer_page.get_alert_text(), 'Texto inesperado no alerta'
        add_customer_page.close_alert()

        manager_page.click_customers()
        customers_list_page = CustomersList(manager_page.driver)

        assert customers_list_page.is_url_customers_list(), 'Página Customers List não encontrada!'

        customers_list_page.type_customer('Amelie')
        assert customers_list_page.get_search_len() == 1, 'Cliente cadastrado não encontrado!'