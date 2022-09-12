# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

balik = 20
delay = 60 

for x in range(balik):
    PATH ="C:\Program Files\chromedriver.exe"
    driver = webdriver.Chrome(PATH) 

    driver.get('https://dockoto.com/login')

    emailField = driver.find_element_by_xpath('//*[@id="email"]')
    emailField.send_keys('admin@dockoto.com')

    passwordField = driver.find_element_by_xpath('//*[@id="sidebar-body"]/div[1]/div/div/div/form/fieldset/div[2]/div/input')
    passwordField.send_keys('7yjJcXiiWA')
    
    button = driver.find_element_by_xpath('//*[@id="sidebar-body"]/div[1]/div/div/div/form/fieldset/button')
    button.send_keys(Keys.RETURN)

    driver.execute_script("window.open('https://dockoto.com/transactions')")
    print(driver.title)
    time.sleep(20)
    driver.execute_script("window.open('https://dockoto.com/withdrawals')")
    print(driver.title)

    time.sleep(delay)
    driver.quit()
    if x == balik: break
else:
    print("Success")