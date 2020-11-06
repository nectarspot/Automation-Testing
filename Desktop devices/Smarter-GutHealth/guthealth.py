import sys
from datetime import time
# from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('driver')
class TestLink:

    def test_click_menu_buy_button(self, driver):
        driver.get('https://smarterguthealth.com/')
        driver.find_element_by_name("gut-buy-nm-four").click()
        #driver.find_element_by_id('ll_buy_btn_id').click()
        driver.implicitly_wait(20)
        driver.find_element_by_name("ll_buy_btn").click()
        driver.implicitly_wait(20)
        driver.find_element_by_id("firstName").send_keys("Test")
        driver.find_element_by_id("lastName").send_keys("Test")
        driver.find_element_by_id("shippingAddress1").send_keys("Test")
        driver.find_element_by_id("shippingAprt").send_keys("Test")
        driver.find_element_by_id("locality").send_keys("Test")
        select = Select(driver.find_element_by_id('country'))
        select.select_by_visible_text('Canada')
        select = Select(driver.find_element_by_id('administrative_area_level_1'))
        select.select_by_visible_text('Alberta')
        driver.find_element_by_id("postal_code").send_keys("56147")
        driver.find_element_by_id("user_email").send_keys("test@test.com")
        driver.find_element_by_id("user_phone_number").send_keys("1234567890")
        driver.find_element_by_id('create_prospect').click()

        driver.implicitly_wait(10)
        # Billing page
        driver.find_element_by_id("creditcardNumber").send_keys("12XXX2")
        driver.find_element_by_id("creditcardCvv").send_keys("123")
        select = Select(driver.find_element_by_id('expiry_month'))
        select.select_by_visible_text('(02) February')
        select = Select(driver.find_element_by_id('expiry_year'))
        select.select_by_visible_text('2022')
        driver.find_element_by_id('split_offer').click()
        driver.find_element_by_id('create_order').click()
        driver.implicitly_wait(10)
        # oto1
        driver.find_element_by_id('upsell').click()
        driver.implicitly_wait(10)
        driver.find_element_by_id('upsell2').click()

        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

