from selenium import webdriver
from helper.helper_base import HelperFunc


def get_browser(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        # driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
        # return HelperFunc(driver)
        return HelperFunc(webdriver.Chrome())
