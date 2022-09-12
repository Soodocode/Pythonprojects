from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

balik = 10
delay = 5 

PATH ="C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH) 

driver.get('https://beta-backoffice.oheavenly.com/')

emailField = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/div/article/div[2]/div/input')
emailField.send_keys('admin@oheavenly.com')

passwordField = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/div/article/div[3]/div/input')
passwordField.send_keys('admin@12345')

button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/div/article/div[4]/button')
button.send_keys(Keys.RETURN)
driver.implicitly_wait(0.5)
print (driver.page_source)
text = 'Something went wrong. Please contact the site admin.'   
if text in driver.page_source:
    print("Error Login');")
else:
    print("Success');")

    for x in range(balik):
        driver.get("https://beta-backoffice.oheavenly.com/merchants/add")
        print(driver.title)
        int_count = int (x) 
        print(int_count) 
        driver.implicitly_wait(1)
        fname = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[1]/div/input')
        fname.send_keys('Jhojie' + str(int_count))

        lname = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[2]/div/input')
        lname.send_keys('Jhojie' + str(int_count))

        email = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[3]/div/input')
        email.send_keys('jhojie' + str(int_count) + '@gmail.com')

        phone = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[4]/div[1]/input')
        phone.send_keys('09102258850')

        store = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[5]/div/input')
        store.send_keys('Jhojie' + str(int_count))

        Street = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[7]/div/input')
        Street.send_keys('Ecoland')

        City = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[8]/div/input')
        City.send_keys('Davao City')

        State = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[9]/div/input')
        State.send_keys('Davao Del sur')

        zip = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[10]/div/input')
        zip.send_keys('800' + str(int_count))
        
        button = driver.find_element_by_xpath('//*[@id="add-merchant"]/div/div/div/div/div/div[11]/button')
        driver.implicitly_wait(1)
        button.send_keys(Keys.RETURN)
    
        if x == balik: break
    else:
        driver.quit()
        print("Success") 
