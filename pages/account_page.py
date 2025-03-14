from pages.base_page import BasePage
from pages.locators import account_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage(BasePage):
    page_url = '/customer/account'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        assert header_title.text == text

    def success_message_is(self, text):
        error_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.success_message))
        assert error_message.text == text
