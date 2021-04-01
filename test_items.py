import pytest
from selenium import webdriver
import time

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button_available(browser):
    browser.get(url)
    time.sleep(30)
    button = len(browser.find_elements_by_class_name('btn-add-to-basket'))
    assert button == 1 , f"There is no Add to basket button"
