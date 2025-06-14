from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasePage:
    def __init__(self, driver, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                options = Options()
                options.add_argument("--incognito")
                self.driver = webdriver.Chrome(options=options)
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise Exception('Browser não suportado!')

    def is_url(self, url):
        return self.driver.current_url == url

    def close(self):
        sleep(2)
        self.driver.quit()