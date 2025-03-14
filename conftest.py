import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.sale_page import SalePage
from pages.create_account_page import CreateAccountPage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.women_sale_page import WomenSalePage
from pages.men_sale_page import MenSalePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def women_sale_page(driver):
    return WomenSalePage(driver)


@pytest.fixture()
def men_sale_page(driver):
    return MenSalePage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)