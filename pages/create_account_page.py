from random import random, randint

from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create/'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        assert header_title.text == text

    def fill_login_form(self, first_name, last_name, password, email=None):
        email = email if email else f'test{randint(10000000000, 9999999999999)}@test.com'
        first_name_field = self.find(loc.first_name_field)
        last_name_field = self.find(loc.last_name_field)
        email_field = self.find(loc.email_field)
        password_field = self.find(loc.password_field)
        confirm_password_field = self.find(loc.confirm_password_field)
        create_an_account_button = self.find(loc.create_an_account_button)

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        create_an_account_button.click()

    def fill_first_name_field(self, first_name):
        first_name_field = self.find(loc.first_name_field)
        first_name_field.send_keys(first_name)

    def fill_last_name_field(self, last_name):
        last_name_field = self.find(loc.first_name_field)
        last_name_field.send_keys(last_name)

    def fill_email_field_with_random_value(self):
        email = f'test{randint(10000000000, 9999999999999)}@test.com'
        email_field = self.find(loc.email_field)
        email_field.send_keys(email)

    def fill_password_field(self, password):
        password_field = self.find(loc.password_field)
        password_field.send_keys(password)

    def fill_confirm_password_field(self, password):
        confirm_password_field = self.find(loc.confirm_password_field)
        confirm_password_field.send_keys(password)

    def click_to_the_create_an_account_button(self):
        self.find(loc.create_an_account_button).click()

    def error_message_is(self, text):
        error_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.error_message))
        assert error_message.text == text

    def password_confirmation_error_is(self, text):
        password_confirmation_error = WebDriverWait(
            self.driver, 10).until(EC.presence_of_element_located(loc.password_confirmation_error)
                                   )
        assert password_confirmation_error.text == text
