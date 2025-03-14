from pages.base_page import BasePage
from pages.locators import men_sale_locators as loc


class MenSalePage(BasePage):
    page_url = '/promotions/men-sale.html'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        assert header_title.text == text
