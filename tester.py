from selenium import webdriver
import time
import random
import essentials
import pandas as pd
import numpy as np

driver = webdriver.Chrome() # Target browser
driver.get('https://pypi.org/')
timeout = 1

def testfunctionality():
    print('Start thinking')
    essentials.think(1,2)
    print("Finished thinking")

    print('Id:', essentials.check_exists_by_id(driver,'user-indicator'))

    print('Name:', essentials.check_exists_by_name(driver,'q'))

    print('Xpath:', essentials.check_exists_by_xpath(driver, '//*[@id="search"]'))

    print('Link text:', essentials.check_exists_by_link_text(driver,'Help'))

    print('partial link text:', essentials.check_exists_by_partial_link_text(driver, 'He'))

    print('Tag name:', essentials.check_exists_by_tag_name(driver, 'ul'))

    print('Class_name:', essentials.check_exists_by_class_name(driver, 'horizontal-menu'))

    print('css_selector:', essentials.check_exists_by_css_selector(driver, '.dropdown.dropdown--on-menu.hidden.show-on-tablet'))


    print('Wait for Id:', essentials.wait_till_exists(driver, 'id', 'user-indicator', timeout))

    print('Wait for Name:', essentials.wait_till_exists(driver, 'name', 'q', timeout))

    print('Wait for Xpath:', essentials.wait_till_exists(driver, 'xpath', '//*[@id="search"]', timeout))

    print('Wait for Link text:', essentials.wait_till_exists(driver, 'link_text', 'Help', timeout))

    print('Wait for partial link text:', essentials.wait_till_exists(driver, 'partial_link_text', 'He', timeout))

    print('Wait for Tag name:', essentials.wait_till_exists(driver, 'tag_name', 'ul', timeout))

    print('Wait for Class_name:', essentials.wait_till_exists(driver, 'class_name', 'horizontal-menu', timeout))

    print('Wait for css_selector:', essentials.wait_till_exists(driver, 'css_selector', '.dropdown.dropdown--on-menu.hidden.show-on-tablet', timeout))

    print('Wait for wrong type', essentials.wait_till_exists(driver, 'WrongType', 'tag', timeout))

    print('Wait for nonexistent element', essentials.wait_till_exists(driver, 'id', 'fake element', timeout))

    if essentials.check_exists_by_link_text(driver, 'Help'):
        essentials.click(driver.find_element_by_link_text('Help'))
        if essentials.wait_till_exists(driver, 'link_text', 'Reset your password', 5):
            essentials.scroll_to_element(driver, driver.find_element_by_link_text('Reset your password'))
            essentials.right_click(driver, driver.find_element_by_link_text('Reset your password'))

testfunctionality()