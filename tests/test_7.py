from pages.OpenAccountPage import OpenAccountPage
from pages.CustomersListPage import CustomersList

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
        assert 'Account created successfully with account Number :' in open_account_alert_text, 'Texto inesperado no alerta'
        open_account_page.close_alert()
