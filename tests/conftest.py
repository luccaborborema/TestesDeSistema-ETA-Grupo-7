import pytest
from pages.LoginPage import LoginPage
from pages.ManagerPage import ManagerPage
from pages.AddCustomerPage import AddCustomers
from pages.OpenAccountPage import OpenAccountPage

def pytest_addoption(parser):
    parser.addoption('--browser_selenium', default='chrome')

@pytest.fixture
def run_all_browser(all_browser):
    login_page = LoginPage(browser=all_browser)
    login_page.open_page()
    yield login_page
    login_page.close()

@pytest.fixture
def open_xyz_bank(request):
    selected_browser = request.config.getoption('browser_selenium').lower()
    login_page = LoginPage(browser=selected_browser)
    login_page.open_page()
    yield login_page
    login_page.close()

@pytest.fixture
def open_manager_page(open_xyz_bank):
    login_page = open_xyz_bank
    if login_page.is_url_login():
        login_page.click_bank_manager_login()
    manager_page = ManagerPage(login_page.driver)
    assert manager_page.is_url_manager(), 'Página de Manager não encontrada!'
    yield login_page, manager_page

@pytest.fixture
def create_customer_with_dollar(open_manager_page):
    login_page, manager_page = open_manager_page

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
    assert 'Account created successfully with account Number :' in open_account_page.get_alert_text(), 'Texto inesperado no alerta'
    open_account_page.close_alert()

    yield manager_page










