from pages.CustomerPage import CustomerPage
from pages.AccountPage import AccountPage
from pages.TransactionsPage import TransactionsPage

class Test4:
    def test_verify_transaction(self, create_customer_with_dollar):
        login_page, manager_page = create_customer_with_dollar

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
        assert account_page.get_balance() == 1000, 'Saldo inválido'

        account_page.click_transactions_menu()
        transaction_page = TransactionsPage(account_page.driver)

        assert transaction_page.is_url_transactions(), 'Página Transactions não encontrada'
        assert transaction_page.validate_transaction(amount=1000, t_type='Credit'), 'Transação listada é inválida'
