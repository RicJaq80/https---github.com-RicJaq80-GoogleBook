from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import pytest
from tests.util import Util

@pytest.mark.usefixtures("ClassSetUp")
class TestBook(unittest.TestCase):
    def setUp(self):
        self.utilities = Util(self.driver)

    def test_search_book(self):
        time.sleep(3)
        locator_minPrice = "//input[@jsname='C7zBXb']"
        locator_maxPrice = "//input[@jsname='TYdZhc']"
        locator_go = ".iTnSe"
        locator_rating = ".yi40Hd"
        min_price = "100"
        max_price = "1500"

        minPrice = self.driver.find_element(By.XPATH, locator_minPrice)
        minPrice.send_keys(min_price)

        maxPrice = self.driver.find_element(By.XPATH, locator_maxPrice)
        maxPrice.send_keys(max_price)

        clickGo = self.driver.find_element(By.CSS_SELECTOR, locator_go)
        clickGo.click()
        time.sleep(1)

        n = 0
        stars = self.driver.find_elements(By.CSS_SELECTOR, locator_rating)
        for star in stars:
            note_txt = star.text
            if note_txt != '':
                float_note_txt= float(note_txt)
            n += 1
            if n == 2:
                if float_note_txt >= 4.5:
                    print("Second option has a rating above 4.5 stars")
                else:
                    print("Second option doesn't have a rating above 4.5 stars")
                    resultMessage = "Rating Not Expected"
                    self.utilities.screenShot(resultMessage)
                break
