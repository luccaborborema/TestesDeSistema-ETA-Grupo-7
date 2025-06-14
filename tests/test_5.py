class Test5:
    def test_add_customer(self, open_manager_page):
        login_page, manager_page = open_manager_page

        manager_page.click_add_customer()