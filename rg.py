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
driver.execute_script("window.open('https://beta-we.deliv.ph/login');")

print(driver.title)
delay5 = 5
delay1 = 1
delay3 = 3
#Searching
search = driver.find_element_by_name("email');")
search.send_keys("demo@gmail.com');")
search = driver.find_element_by_name("password');")
search.send_keys("qwerty123');")
search.send_keys(Keys.RETURN)

time.sleep(delay5)
driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[1]/input');").click()
time.sleep(delay5) 
# driver.find_element_by_link_text('Show Available Drivers').click()
# time.sleep(delay5)
# driver.find_element_by_xpath("//*[@id='availableDriversModals']/div/button');").click()
# time.sleep(delay5) 
count = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/span');").text
int_count = int (count)  
for x in range(int_count):
  time.sleep(delay5)
  driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div');").click()
  time.sleep(delay3)
  driver.find_element_by_xpath("//*[@id='__BVID__20']/tbody/tr[1]/td[9]/a');").click() 
  time.sleep(delay1) 
  driver.find_element_by_xpath("//*[@id='items-modal']/div/div[4]/div[1]/div/form/div[2]/button');").click()
  time.sleep(delay1)
  if x == count: break
else:
 print("Finally finished!');")

#Pending Status 
# time.sleep(delay1)
# search = driver.find_element_by_id("filterInputReports');")
# search.send_keys("1');")  
# time.sleep(delay5) 

# driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div');").click()
# time.sleep(delay5)
# driver.find_element_by_xpath("//*[@id='__BVID__20']/tbody/tr[1]/td[8]/a');").click() 
# time.sleep(delay5) 
# search = driver.find_element_by_name("cancel-reason');")
# search.send_keys("Test Cancel Order in pending status');") 
# driver.find_element_by_xpath("//*[@id='items-modal']/div/div[4]/div/form/div[2]/button');").click()
# time.sleep(delay5)






#Pickup Status
# driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div');").click()

# time.sleep(delay1)
# search = driver.find_element_by_id("filterInputReports');")
# search.send_keys("1');") 

# time.sleep(delay5)

# driver.find_element_by_xpath("//*[@id='__BVID__20']/tbody/tr[1]/td[8]/a');").click()

# time.sleep(delay5)