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

    searchBook = driver.find_element(By.NAME, "q")
    searchBook.send_keys("libro Los Miserables")

    clickSearch = driver.find_element(By.NAME, "btnK")
    clickSearch.click()

    time.sleep(20) # to click on I am not a robot

    clickShoping = driver.find_element(By.XPATH, "//span[normalize-space()='Shopping']")
    clickShoping.click()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--mode", action="store", default="headed", help="Choose browser mode")    
