from resources.model.elements.web_element import WebElement
from time import sleep


class Button(WebElement):

    def __init__(self, xpath, driver):
        WebElement.__init__(self, xpath, driver)

    def click(self):
        self._return_visible_element_(self.xpath).click()

    def is_enabled(self):
        return self._return_visible_element_(self.xpath).is_enabled()
