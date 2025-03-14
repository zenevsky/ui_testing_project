from selenium.webdriver.common.by import By

header_title_loc = (By.TAG_NAME, 'h1')

items = (By.XPATH, '//*[contains(@data-container, "product-grid")]')

size_28 = (By.ID, 'option-label-size-143-item-171')

color_black = (By.ID, 'option-label-color-93-item-49')

add_to_cart_button = (By.XPATH, '//*[text()="Add to Cart"]')

add_to_wishlist_button = (By.XPATH, '//*[@title="Add to Wish List"]')

price = (By.CSS_SELECTOR, '.product-item .price:not(.hidden)')

cart_counter = (By.XPATH, '//*[@class="counter-number"]')

sort_by_selector = (By.ID, 'sorter')