from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture(scope="class")
def ClassSetUp(request):
    mode = request.config.getoption("--mode")
    baseUrl = "https://www.google.com/"
    options = webdriver.ChromeOptions()

    if mode == "headless":
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()

    driver.implicitly_wait(2)
    driver.get(baseUrl)

    BOOK_NAME = "Los Miserables"
    locator_search = "q"
    locator_click = "btnK"
    locator_shopping = "//span[normalize-space()='Shopping']"

    searchBook = driver.find_element(By.NAME, locator_search)
    searchBook.send_keys(f"libro {BOOK_NAME}")

    clickSearch = driver.find_element(By.NAME, locator_click)
    clickSearch.click()

    time.sleep(20) # to solve the captcha

    clickShoping = driver.find_element(By.XPATH, locator_shopping)
    clickShoping.click()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--mode", action="store", default="headed", help="Choose browser mode")    
