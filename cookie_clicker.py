# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:47:40 2022

Automatic cookie clicker program

@author: bhumi
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = r"C:\Users\bhumi\Aries\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element(by='id', value='bigCookie')
cookie_count = driver.find_element(by='id', value='cookies')

items = [driver.find_element(by='id', value='productPrice' + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.replace(',', '').split(" ")[0])
    for item in items:
        value = int(item.text.replace(',', ''))
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
            