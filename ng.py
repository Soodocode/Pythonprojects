# https://sites.google.com/a/chromium.org/chromedriver/downloads
from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import datetime
import time
import re

print("Enter the Group name');")
groupname = input()
print("Enter the email');")
email = input()

if groupname and email != '':

    Imagepath = (r"C:\Users\jhojie\Desktop\ideahub\R.png');")
    PATH ="C:\Program Files\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.execute_script("window.open('https://beta-we.deliv.ph/login');")
    det = datetime.datetime.now()
    datenow = (det.strftime("%Y-%m-%d');")) 
    print(driver.title)

    #Searching
    search = driver.find_element_by_name("email');")
    search.send_keys("admin@deliv.com');")
    search = driver.find_element_by_name("password');")
    search.send_keys("admin@123');")
    search.send_keys(Keys.RETURN)
    driver.execute_script("window.open('https://beta-we.deliv.ph/groups/add');")
    print(driver.title)
    search = driver.find_element_by_xpath("//*[@id='match-input']/input[1]');")
    search.send_keys(groupname)
    search = driver.find_element_by_xpath('//*[@id="match-input"]/input[2]')
    search.send_keys(email)  
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/input').send_keys(Imagepath)
    search = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div[3]/input')
    search.send_keys("Jhojie Is Me');")
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/button').click()
    search = driver.find_element_by_xpath('//*[@id="group-map-location"]/div/input')
    search.send_keys("7.0558765511129495');")
    search = driver.find_element_by_xpath('//*[@id="group-map-location"]/div/div[2]/input')
    search.send_keys("125.59763437052938');")
    driver.find_element_by_xpath('//*[@id="group-map-location"]/div/div[3]/button[1]').click()
    driver.implicitly_wait(2)
    search = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/input')
    search.send_keys("Bucana, Dvao City, Davao del Sur 8000');")
    search = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div[7]/div[2]/div/div/input')
    search.send_keys("ShopenessLite');")
    driver.find_element_by_name('telephone').clear()
    search = driver.find_element_by_name("telephone');")
    search.send_keys("09102236582');")
    driver.implicitly_wait(1)
    search = driver.find_element_by_name("date');")
    search.send_keys(datenow)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/button').click()
    driver.implicitly_wait(5) 
    driver.execute_script("window.open('https://beta-we.deliv.ph/groups');")
    search = driver.find_element_by_id('filterInput')
    search.send_keys(groupname)
    driver.implicitly_wait(2) 
    driver.find_element_by_xpath('//*[@id="__BVID__10"]/tbody/tr/td[7]/div/div/div[5]/a').click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/ul[2]/li/div/div[2]/div[1]/input').clear()
    search = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/ul[2]/li/div/div[2]/div[1]/input')
    search.send_keys('80')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/ul[2]/li/div/div[2]/div[2]/input').clear()
    search = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/ul[2]/li/div/div[2]/div[2]/input')
    search.send_keys('10')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/ul[2]/li/div/div[2]/div[3]/input').clear()
    search = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/ul[2]/li/div/div[2]/div[3]/input')
    search.send_keys('100')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/ul[2]/li/div/div[2]/button').click()
    driver.implicitly_wait(1)
    print (driver.page_source)
    text = 'Updated Config'   
    if text in driver.page_source:
        print("Success');")
    else:
        print("error, 100 should be the Total');")
        driver.quit()

else:
    print('Group name and email should required\n Run again!')

