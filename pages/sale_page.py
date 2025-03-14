from pages.base_page import BasePage
from pages.locators import sale_locators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def click_to_the_women_sale_link(self):
        self.find(loc.women_sale_link).click()

    def click_to_the_mens_bargains_link(self):
        self.find(loc.mens_bargains).click()

    def check_t_shirts_block_title_text_is(self, text):
        assert self.find(loc.t_shirts_block_title).text == text
