import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


from main_page import MainPage
from signup_page import SignupPage

@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def main_page(request):
    return MainPage(request.cls.driver)

@pytest.fixture(scope="class")
def signup_page(request):
    return SignupPage(request.cls.driver)
