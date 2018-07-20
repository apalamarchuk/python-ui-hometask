from resources.model.elements.web_element import WebElement
from time import sleep


class Link(WebElement):

    def __init__(self, xpath, driver):
        WebElement.__init__(self, xpath, driver)

    def click(self):
        self._return_visible_element_(self.xpath).click()
        sleep(3)
