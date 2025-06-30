from pages.AddCustomerPage import AddCustomers
from pages.CustomersListPage import CustomersList

class Test6:
    def test_delete_client(self, open_manager_page):
        login_page, manager_page = open_manager_page

        manager_page.click_customers()

        customers_list_page = CustomersList(manager_page.driver)
        assert customers_list_page.is_url_customers_list(), 'Página Customers List não encontrada!'

        n_clients = customers_list_page.get_search_len()

        customers_list_page.type_customer("Harry Potter")
        customers_list_page.delete()

        assert customers_list_page.get_search_len() == 0
