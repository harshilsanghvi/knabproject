import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HelperFunc(object):
    __TIMEOUT = 20

    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def maximize(self):
        self._driver.maximize_window()

    def close(self):
        self._driver.quit()

    # Helper functions that are used to identify the web locators in Selenium Python tutorial

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_xpath_clickable(self, xpath):
        return self._driver_wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def find_and_select_by_xpath(self, xpath, value):
        self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
        time.sleep(2)
        select_element = self._driver.find_element(By.XPATH, xpath + "/select")
        for option in select_element.find_elements(By.TAG_NAME, 'option'):
            if option.text == value:
                option.click()  # select() in earlier versions of webdriver
                break

    def find_and_choose_by_xpath(self, xpath, value, option_att):
        self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
        time.sleep(2)
        for option in self._driver.find_elements(By.XPATH, xpath+'/div[2]/div'):
            if value == option.get_attribute(option_att):
                option.click()
                time.sleep(1)
                break

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def verify_by_xpath(self, xpath):
        self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return self._driver.find_element(By.XPATH, xpath)

    def switch_to_iframe(self, identifier, value):
        if identifier.lower() == "xpath":
            return self._driver_wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, value)))
        if identifier.lower() == "id":
            return self._driver_wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, value)))

    def switch_to_main(self):
        self._driver.switch_to.default_content()
