from resources.model.pages.object_rep import ObjectRepository
from resources.model.elements.button import Button
from resources.model.elements.link import Link
from resources.model.elements.field import Field
from resources.model.elements.select_field import SelectField


class MainPageObjectRepository(ObjectRepository):
    calculate_link_xpath = '//a[@href="#calculation"]'

    calculate_button_xpath = '//table[@class="table-calculation table"]/following-sibling::div/button'
    total_cost_xpath = '//td[@class="summary-calculation"]'
    shipping_cost_xpath = '//td[@class="cost-of-delivery"]'

    shipping_message_xpath = '//select[@id="calculatedeliveryform-shipping_method"]/following-sibling::p'
    country_message_xpath = '//select[@id="calculatedeliveryform-country"]/following-sibling::p'
    weight_message_xpath = '//input[@id="calculatedeliveryform-weight"]/following-sibling::p'

    select_country_xpath = '//select[@id="calculatedeliveryform-country"]'
    select_shipping_method_xpath = '//select[@id="calculatedeliveryform-shipping_method"]'
    select_shipping_type_xpath = '//select[@id="calculatedeliveryform-shipping_type"]'

    weight_field_xpath = '//input[@id="calculatedeliveryform-weight"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.calculation_button = Button(self.calculate_button_xpath, driver)
        self.link = Link(self.calculate_link_xpath, driver)
        self.total_cost_field = Field(self.total_cost_xpath, driver)
        self.shipping_cost_field = Field(self.shipping_cost_xpath, driver)
        self.weight_field = Field(self.weight_field_xpath, driver)
        self.country_select = SelectField(self.select_country_xpath, driver)
        self.shipping_method_select = SelectField(self.select_shipping_method_xpath, driver)
        self.shipping_type_select = SelectField(self.select_shipping_type_xpath, driver)
