from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        assert header_title.text == text

    def choose_the_size_28(self, item_number):
        items = self.find_all(loc.items)
        if item_number >= len(items):
            raise ValueError(f"Item number {item_number} is out of range. Total items: {len(items)}")
        item = items[item_number]
        self.actions.move_to_element(item).perform()
        item.find_element(*loc.size_28).click()

    def choose_color_black(self, item_number):
        items = self.find_all(loc.items)
        if item_number >= len(items):
            raise ValueError(f"Item number {item_number} is out of range. Total items: {len(items)}")
        item = items[item_number]
        self.actions.move_to_element(item).perform()
        item.find_element(*loc.color_black).click()

    def click_to_the_add_to_cart_button(self, item_number):
        items = self.find_all(loc.items)
        if item_number >= len(items):
            raise ValueError(f"Item number {item_number} is out of range. Total items: {len(items)}")
        item = items[item_number]
        self.actions.move_to_element(item).perform()
        add_to_cart_button = item.find_element(*loc.add_to_cart_button)
        self.actions.move_to_element(add_to_cart_button).click().perform()

    def click_to_the_add_to_wishlist_button(self, item_number):
        items = self.find_all(loc.items)
        if item_number >= len(items):
            raise ValueError(f"Item number {item_number} is out of range. Total items: {len(items)}")
        item = items[item_number]
        self.actions.move_to_element(item).perform()
        add_to_wishlist_button = item.find_element(*loc.add_to_wishlist_button)
        self.actions.move_to_element(add_to_wishlist_button).click().perform()

    def check_that_product_is_added_to_cart(self):
        assert WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(loc.cart_counter, "1"))

    def choose_sorting_by_price(self):
        select = Select(self.find(loc.sort_by_selector))
        select.select_by_visible_text('Price')

    def check_sorting_by_price(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(loc.items))
        items = self.find_all(loc.items)
        prices = []
        for item in items:
            price_element = WebDriverWait(item, 10).until(
                EC.visibility_of_element_located(loc.price)
            )
            prices.append(price_element.text)
        price_nums = [float(i.strip('$')) for i in prices]
        assert price_nums == sorted(price_nums)
