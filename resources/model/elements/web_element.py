from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class WebElement(object):

    def __init__(self, xpath, driver):
        self.xpath = xpath
        self.driver = driver

    def _is_visible(self):
        sleep(1)
        return WebDriverWait(self.driver, 15) \
            .until(EC.visibility_of_element_located((By.XPATH, self.xpath)))

    def _return_visible_element_(self, xpath):
        sleep(1)
        return WebDriverWait(self.driver, 15) \
            .until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def _return_element_(self, xpath):
        sleep(1)
        return self.driver.find_element_by_xpath(xpath)
