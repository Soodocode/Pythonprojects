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

driver.execute_script("window.open('https://beta-webapp.deliv.ph/log/?user_id=eyJpdiI6IjBGWVc1T1RYNjdNb0ZYR0JLcFBoNUE9PSIsInZhbHVlIjoiWm9aekdMZzdVQ1cvdU1rUGJWSGJGdz09IiwibWFjIjoiZmNlN2Q3NWFlMGQ5NDIzZDg4MDZlNGU2YzBiOGYxN2NiMWFkOTUyODFlMTFmZjJjNzc5MGEwYWVkOGJjNTVlYSJ9&group_id=28');")

print(driver.title)
delay5 = 5
delay1 = 1
delay3 = 3
balik = 3
#Searching
for x in range(balik):
    time.sleep(10)
    search = driver.find_element_by_xpath("//*[@id='display']/div[2]/div[2]/div[4]/div/div[2]/div[2]/div[2]/div[3]/textarea');")
    search.send_keys("Please call me for the instruction');")
    search = driver.find_element_by_id("dest0');")
    search.send_keys("NHA Bangkal, Cordillera, Talomo, Davao City, Davao del Sur, Philippines');")
    search.send_keys(Keys.RETURN)
    time.sleep(delay3)
    search = driver.find_element_by_name("recieverContact');")
    search.send_keys("09103373785');")
    search = driver.find_element_by_id("multReceiver0');")
    search.send_keys("James Bond');")
    search = driver.find_element_by_id("dropoffNote0');")
    search.send_keys("Please call me for the instruction');")
    driver.find_element_by_id('estCost0').clear()
    search = driver.find_element_by_id("estCost0');")
    search.send_keys("200');")
    driver.implicitly_wait(2) 
    driver.find_element_by_xpath("//*[@id='display']/div[2]/div[2]/div[5]/div/div[2]/div[10]/button');").click()
    time.sleep(delay3)
    driver.find_element_by_xpath("//*[@id='display']/div[2]/div[2]/div[4]/div/div[4]/div/label/input');").click()
    time.sleep(delay1)
    driver.find_element_by_xpath("//*[@id='display']/div[2]/div[2]/div[4]/div/div[5]/button[2]');").click()
    time.sleep(delay1)
    driver.execute_script("window.open('https://beta-webapp.deliv.ph/bookaservice');")
    
    if x == balik: break
else: 
 driver.quit()
