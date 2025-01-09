from selenium.webdriver.common.by import By

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "signupName")
        self.last_name_input = (By.ID, "signupLastName")
        self.email_input = (By.ID, "signupEmail")
        self.password_input = (By.ID, "signupPassword")
        self.repeat_password_input = (By.ID, "signupRepeatPassword")
        self.register_button = (By.XPATH, "//button[text()='Register']")

    def register(self, first_name, last_name, email, password, repeat_password):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.repeat_password_input).send_keys(password)
        self.driver.find_element(*self.register_button).click()
