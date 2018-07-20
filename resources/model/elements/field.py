from resources.model.elements.web_element import WebElement
from time import sleep


class Field(WebElement):

    def __init__(self, xpath, driver):
        WebElement.__init__(self, xpath, driver)
        self.message_xpath = xpath + "/following-sibling::p"

    def set_value(self, value):
        self._return_visible_element_(self.xpath).send_keys(value)

    def is_displayed(self):
        self._return_visible_element_(self.xpath).is_displayed()

    def get_text(self):
        return self._return_visible_element_(self.xpath).text

    def get_message(self):
        return self._return_element_(self.message_xpath).text

    def is_message_empty(self):
        return self._return_element_(self.message_xpath).text == ''