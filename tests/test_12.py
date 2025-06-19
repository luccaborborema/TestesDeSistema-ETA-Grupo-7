from time import sleep

from pages.CustomerPage import CustomerPage
from pages.LoginPage import LoginPage
from pages.AccountPage import AccountPage

class Test9:
    def test_login_with_no_account(self, create_customer_without_account):
        login_page, manager_page = create_customer_without_account

        manager_page.click_home()
        assert login_page.is_url_login(), 'Página Login não encontrada'

        login_page.click_customer_login()
        customer_page = CustomerPage(login_page.driver)

        customer_page.select_your_name('Amelie Silva')
        assert customer_page.validate_login_is_visible(), 'Botão de Login não encontrado'
        customer_page.click_login()

        account_page = AccountPage(customer_page.driver)
        assert account_page.get_customer_name() == 'Amelie Silva', 'Nome não bate com nome do cliente'
        assert account_page.get_no_account_message(), "Mensagem 'Please open an account with us.' não encontrada"