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
        minPrice = self.driver.find_element(By.XPATH, "//input[@jsname='C7zBXb']")
        minPrice.send_keys("100")

        maxPrice = self.driver.find_element(By.XPATH, "//input[@jsname='TYdZhc']")
        maxPrice.send_keys("1500")

        clickGo = self.driver.find_element(By.CSS_SELECTOR, ".iTnSe")
        clickGo.click()
        time.sleep(1)

        n = 0
        stars = self.driver.find_elements(By.CSS_SELECTOR, ".yi40Hd")
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
