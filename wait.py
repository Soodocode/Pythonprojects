from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

PATH ="C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.execute_script("window.open('https://beta-webapp.deliv.ph/log/?user_id=eyJpdiI6IjBGWVc1T1RYNjdNb0ZYR0JLcFBoNUE9PSIsInZhbHVlIjoiWm9aekdMZzdVQ1cvdU1rUGJWSGJGdz09IiwibWFjIjoiZmNlN2Q3NWFlMGQ5NDIzZDg4MDZlNGU2YzBiOGYxN2NiMWFkOTUyODFlMTFmZjJjNzc5MGEwYWVkOGJjNTVlYSJ9&group_id=28');")
delay = 3 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="display"]/div[2]/div[2]/div[4]/div/div[2]/div[2]/div[2]/div[3]/textarea')))
    print ("Page is ready!');")
except TimeoutException:
    print ("Loading took too much time!');")