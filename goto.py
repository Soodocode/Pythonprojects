# https://sites.google.com/a/chromium.org/chromedriver/downloads
from os import link
from platform import python_version_tuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

delay5 = 50
delay1 = 20
delay3 = 30
# delay5 = 5
# delay1 = 1
# delay3 = 3


print('1. Cancel Orders in Admin\n2. Create Orders\n3. Create new Group')
str1 = input() 

if str1 == '1':
    PATH ="C:\Program Files\chromedriver.exe"
    driver = webdriver.Chrome(PATH) 
    driver.execute_script("window.open('https://beta-we.deliv.ph/login');")
    print(driver.title)
    #Searching
    search = driver.find_element_by_name("email');")
    search.send_keys("demo@gmail.com');")
    search = driver.find_element_by_name("password');")
    search.send_keys("qwerty123');")
    search.send_keys(Keys.RETURN)
    print(driver.title)
    time.sleep(delay5)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[1]/input');").click()
    time.sleep(delay5) 
    # driver.find_element_by_link_text('Show Available Drivers').click()
    # time.sleep(delay5)
    # driver.find_element_by_xpath("//*[@id='availableDriversModals']/div/button');").click()
    # time.sleep(delay5) 
    count = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/span');").text
    int_count = int (count) 
    print(int_count) 
    for x in range(int_count):
        time.sleep(delay5)
        driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div');").click()
        time.sleep(delay5)
        driver.find_element_by_xpath("//*[@id='__BVID__20']/tbody/tr[1]/td[9]/a');").click() 
        time.sleep(delay1) 
        driver.find_element_by_xpath("//*[@id='items-modal']/div/div[4]/div[1]/div/form/div[2]/button');").click()
        time.sleep(delay3)
        count = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/span');").text
        int_count = int (count) 
        print(int_count) 
        if x == count: break
    else:
     print("Finally finished!');")
     driver.quit()
elif str1 == '2':
    print("How many order you want to add?');")
    input_num = input()
    balik = int(input_num)
    PATH ="C:\Program Files\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.execute_script("window.open('https://beta-webapp.deliv.ph/log/?user_id=eyJpdiI6IkRpb3BQMFdaQ245R2RWT2RDaW9uVmc9PSIsInZhbHVlIjoicDNMQjk0YW1jYTNwRGpJdUpmOWtCQT09IiwibWFjIjoiZDZjMjg1ODA2NjY1NTcyMzFkZGUyNzU3YWZlMmIyYmY5MDQwMDgzMGY2YzI0Nzk1MjI4Y2YyNzgwMGU0MGZhNiJ9&group_id=28');")
    # driver.execute_script("window.open('https://webapp.deliv.ph/log/?user_id=eyJpdiI6IkR4cGJvclNiRVJvNEZScmxTYkJuWEE9PSIsInZhbHVlIjoiYTJLblRtOGU5dHAwb0ZEcnlzK3JzQT09IiwibWFjIjoiYTUxMmFhMzJlMDBmNDhmZTQ5ODY0OTRkNWNhYzVhYmFjYjk0NWM3ZGJkYjFkNWE1MjBjN2IxMWU4YzlmMzlkZiJ9&group_id=17');")
    
    print(driver.title)
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
        time.sleep(delay3)
        driver.find_element_by_class_name('btn-next').click()
        time.sleep(delay3)
        driver.find_element_by_xpath("//*[@id='display']/div[2]/div[2]/div[4]/div/div[4]/div/label/input');").click()
        time.sleep(delay1)
        driver.find_element_by_xpath("//*[@id='display']/div[2]/div[2]/div[4]/div/div[5]/button[2]');").click()
        time.sleep(delay1)
        driver.execute_script("window.open('https://beta-webapp.deliv.ph/bookaservice');")
        
        if x == balik: break
    else:
        print("Success');") 
        driver.quit()

elif str1 == '3':
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

else:
    print('run again')  


# NHA Bangkal, Cordillera, Talomo, Davao City, Davao del Sur, Philippines
# Matina Aplaya, Talomo, Davao City, Davao del Sur, Philippines
# Bucana, Talomo, Davao City, Davao del Sur, Philippines
# Matina Crossing, Talomo, Davao City, Davao del Sur, Philippines
# Matina Pangi Road, Talomo, Davao City, Davao del Sur, Philippines
