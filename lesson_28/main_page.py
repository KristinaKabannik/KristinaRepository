from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_button = (By.XPATH, "//button[contains(@class, 'hero-descriptor_btn') and contains(@class, "
                                        "'btn') and contains(@class, 'btn-primary')]")


    def go_to_signup_page(self):
        self.driver.find_element(*self.signup_button).click()
