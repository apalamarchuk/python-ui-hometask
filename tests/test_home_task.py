import pytest
from resources.model.pages.main_page import MainPage
from resources.model.pages.main_page_object_rep import MainPageObjectRepository
from selenium import webdriver


class FixtureMeetsMainPage(object):
    meest_main_page = None
    driver = None

    @pytest.fixture
    def mp(self):
        if self.meest_main_page is None:
            self.meest_main_page = MainPage(self.driver, MainPageObjectRepository(self.driver))
            self.meest_main_page.open_main_page()
        return self.meest_main_page

    @pytest.fixture
    def teardown_mp(self):
        if self.meest_main_page.driver is None:
            return
        self.meest_main_page.driver.quit()


class TestMeetsMainPage(FixtureMeetsMainPage):

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.mp(cls)

    def setup_method(self, method):
        self.meest_main_page.refresh()
        self.meest_main_page.scroll_top()
        self.meest_main_page.object_rep.link.click()

    def test_required_fields_validation(self, mp):
        mp.object_rep.calculation_button.click()
        assert mp.object_rep.calculation_button.is_enabled()
        assert "0.00" in mp.object_rep.shipping_cost_field.get_text()
        assert "0.00" in mp.object_rep.total_cost_field.get_text()
        assert mp.object_rep.country_select.get_message() == 'This field can’t be blank'
        assert mp.object_rep.weight_field.get_message() == 'This field can’t be blank'
        assert mp.object_rep.shipping_method_select.get_message() == 'This field can’t be blank'

    def test_appearance_of_shipping_type_dropdown(self, mp):
        mp.object_rep.country_select.select_option("Ukraine")
        mp.object_rep.shipping_method_select.select_option("Air")
        assert mp.object_rep.shipping_type_select._is_visible()
        assert mp.object_rep.shipping_type_select.selected_options_number() == 1
        assert mp.object_rep.shipping_type_select.get_selected_option() == 'Select shipping type'
        assert mp.object_rep.shipping_type_select.get_options_list() == ['Select shipping type', 'Home delivery',
                                                                         'Branch']
        assert mp.object_rep.shipping_type_select.is_message_empty()

    def test_calculation_check(self, mp):
        mp.object_rep.country_select.select_option("Ukraine")
        mp.object_rep.shipping_method_select.select_option("Sea")
        mp.object_rep.shipping_type_select.select_option("Home delivery")
        mp.object_rep.weight_field.set_value("22")
        mp.object_rep.calculation_button.click()
        assert mp.object_rep.country_select.is_message_empty()
        assert mp.object_rep.shipping_method_select.is_message_empty()
        assert mp.object_rep.shipping_type_select.is_message_empty()
        assert mp.object_rep.weight_field.is_message_empty()
        assert "76.16" in mp.object_rep.shipping_cost_field.get_text()
        assert "76.16" in mp.object_rep.total_cost_field.get_text()

    @classmethod
    def teardown_class(cls):
        cls.teardown_mp(cls)
