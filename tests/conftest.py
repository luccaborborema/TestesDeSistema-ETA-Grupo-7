import pytest
from pages.LoginPage import LoginPage
from pages.ManagerPage import ManagerPage

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
