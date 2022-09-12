# https://sites.google.com/a/chromium.org/chromedriver/downloads
from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH ="C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

URLLive = 'https://we.deliv.ph/'
URLBETA = 'http://beta-we.deliv.ph/' 
driver.get(URLLive)

print(driver.title)
delay = 600 
 
search = driver.find_element_by_name("email")
search.send_keys("admin@deliv.ph")
search = driver.find_element_by_name("password")
search.send_keys("admin@123")
search.send_keys(Keys.RETURN) 
driver.execute_script("window.open('http://we.deliv.ph/groups/63');")
driver.execute_script("window.open('http://we.deliv.ph/groups/62');")
driver.execute_script("window.open('http://we.deliv.ph/groups/59');")
driver.execute_script("window.open('http://we.deliv.ph/groups/58');")
driver.execute_script("window.open('http://we.deliv.ph/groups/57');")
driver.execute_script("window.open('http://we.deliv.ph/groups/56');")
driver.execute_script("window.open('http://we.deliv.ph/groups/55');")
driver.execute_script("window.open('http://we.deliv.ph/groups/54');")
time.sleep(20)
driver.execute_script("window.open('http://we.deliv.ph/groups/53');")
driver.execute_script("window.open('http://we.deliv.ph/groups/52');")
driver.execute_script("window.open('http://we.deliv.ph/groups/51');")
driver.execute_script("window.open('http://we.deliv.ph/groups/49');")
driver.execute_script("window.open('http://we.deliv.ph/groups/48');")
driver.execute_script("window.open('http://we.deliv.ph/groups/47');")
driver.execute_script("window.open('http://we.deliv.ph/groups/46');")
driver.execute_script("window.open('http://we.deliv.ph/groups/45');")
time.sleep(20)
driver.execute_script("window.open('http://we.deliv.ph/groups/44');") 
driver.execute_script("window.open('http://we.deliv.ph/groups/36');") 
driver.execute_script("window.open('http://we.deliv.ph/groups/34');")
driver.execute_script("window.open('http://we.deliv.ph/groups/33');")
driver.execute_script("window.open('http://we.deliv.ph/groups/32');")
driver.execute_script("window.open('http://we.deliv.ph/groups/31');")
driver.execute_script("window.open('http://we.deliv.ph/groups/28');")
driver.execute_script("window.open('http://we.deliv.ph/groups/25');")
driver.execute_script("window.open('http://we.deliv.ph/groups/21');")
driver.execute_script("window.open('http://we.deliv.ph/groups/20');") 
# print(driver.title)
# time.sleep(20)
# driver.execute_script("window.open('https://dockoto.com/withdrawals');")
# print(driver.title)
# time.sleep(delay)
# driver.quit()
