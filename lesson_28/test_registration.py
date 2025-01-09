from datetime import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import init_driver
from main_page import MainPage
from signup_page import SignupPage
import time

@pytest.mark.usefixtures("init_driver", "main_page", "signup_page")
class TestRegistration:

#    def __init__(self):
#        self.driver = None

    def test_user_registration(self, main_page, signup_page):
        # Переходимо на сторінку реєстрації
        main_page.go_to_signup_page()

        # Дані для реєстрації
        first_name = "ddaLllqw"
        last_name = "ddaHhhqw"
        email = "ddalllhhhqw@example.com"
        password = "SecurePas123"
        repeat_password = "SecurePas123"


        # Виконуємо реєстрацію
        signup_page.register(first_name, last_name, email, password, repeat_password)
        time.sleep(3)

        # Перевіряємо, чи успішна реєстрація (залежно від UI після реєстрації)
        success_message = self.driver.find_element(By.CLASS_NAME, "btn.btn-primary").text
        assert "Успішна реєстрація" in success_message, "Реєстрація не виконана успішно"
