from selenium.webdriver.support.select import Select
from resources.model.elements.field import Field
from time import sleep


class SelectField(Field):

    def __init__(self, xpath, driver):
        Field.__init__(self, xpath, driver)

    def select_option(self, option):
        Select(self._return_visible_element_(self.xpath)).select_by_visible_text(option)

    def selected_options_number(self):
        return len(Select(self._return_visible_element_(self.xpath)).all_selected_options)

    def get_selected_option(self):
        return Select(self._return_visible_element_(self.xpath)).first_selected_option.text

    def selected_options(self):
        selected_options = Select(self._return_visible_element_(self.xpath)).all_selected_options
        for p in selected_options:
            print(p)
        print(len(selected_options))
        return selected_options[0].text

    def get_options_list(self):
        options = Select(self._return_visible_element_(self.xpath)).options
        options_list = []
        for p in options:
            options_list.append(p.text)
        return options_list