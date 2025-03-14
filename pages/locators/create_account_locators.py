from selenium.webdriver.common.by import By

header_title_loc = (By.TAG_NAME, 'h1')

first_name_field = (By.ID, 'firstname')

last_name_field = (By.ID, 'lastname')

email_field = (By.ID, 'email_address')

password_field = (By.ID, 'password')

confirm_password_field = (By.ID, 'password-confirmation')

create_an_account_button = (By.XPATH, '//*[@title="Create an Account"]')

error_message = (By.XPATH, '//*[@data-ui-id="message-error"]')

password_confirmation_error = (By.ID, 'password-confirmation-error')