import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_addcard_button(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_xpath ('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')

