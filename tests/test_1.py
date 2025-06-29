from pages.AccountPage import AccountPage
from pages.CustomerPage import CustomerPage


class Test1:
    def test_deposit_successful(self, create_customer_with_dollar):
        login_page, manager_page  = create_customer_with_dollar

        manager_page.click_home()
        assert login_page.is_url_login(), 'Página Login não encontrada'

        login_page.click_customer_login()
        customer_page = CustomerPage(login_page.driver)

        customer_page.select_your_name('Amelie Silva')
        assert customer_page.validate_login_is_visible(), 'Botão de Login não encontrado'
        customer_page.click_login()

        account_page = AccountPage(customer_page.driver)
        assert account_page.get_customer_name() == 'Amelie Silva', 'Nome não bate com nome do cliente'
        account_page.make_deposit(1000)
        assert account_page.get_deposit_message() == 'Deposit Successful', 'Erro no depósito'
