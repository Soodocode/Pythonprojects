# https://sites.google.com/a/chromium.org/chromedriver/downloads
from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


Imagepath = (r"C:\Users\jhojie\Desktop\ideahub\R.png")
PATH ="C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.execute_script("window.open('https://beta-we.deliv.ph/login")

print(driver.title)
#Searching
search = driver.find_element_by_name("email")
search.send_keys("demo@gmail.com")
search = driver.find_element_by_name("password")
search.send_keys("qwerty123")
search.send_keys(Keys.RETURN)
driver.execute_script("window.open('https://beta-we.deliv.ph/customer/add")
print(driver.title)
search = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[1]/form/div[1]/input")
search.send_keys("Nancy Lopez")
search = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[1]/form/div[2]/input")
search.send_keys("nacylopez@demo.com")
driver.find_element_by_name('telephone').clear()
search = driver.find_element_by_name("telephone")
search.send_keys("09102256940")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div/input').send_keys(Imagepath)
search = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[1]/form/div[6]/div[2]/div[1]/input")
search.send_keys("Matina")
search = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[1]/form/div[6]/div[2]/div[2]/input")
search.send_keys("Davao City")
search = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[1]/form/div[6]/div[2]/div[3]/input")
search.send_keys("8000")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/button').click()
time.sleep(10) 
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div[6]/div[2]/button').click() 
webapplink = driver.find_element_by_id("app-link")  
print("Value of input box: " + webapplink.get_attribute('value'))
driver.quit()
