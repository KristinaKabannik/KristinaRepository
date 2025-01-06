from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class NovaPoshta:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open_np_site(self):   # Відкриваємо веб-сторінку сайту Нової пошти
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)

    def input_tr_number(self, tracking_number):  # Вводимо номер накладної
        search_box = self.driver.find_element(By.ID, "en")
        search_box.send_keys(tracking_number)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

    def get_status(self):   # Отримуємо статус посилки
        try:
            status_element = self.driver.find_element(By.XPATH, "//div[contains(@class, 'track__form-message') and contains(@class, 'track__form-error')]")
            return status_element.text
        except:
            return None

    def close(self):
        self.driver.quit()
