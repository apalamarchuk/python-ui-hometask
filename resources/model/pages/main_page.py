from selenium.webdriver.common.keys import Keys
from resources.model.pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver, main_page_object_repository):
        super().__init__(driver, main_page_object_repository)

    def refresh(self):
        self.driver.refresh()

    def open_main_page(self):
        self.driver.get('https://my.meest.us/en')

    def scroll_top(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
