# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 

Imagepath = (r"C:\Users\jhojie\OneDrive\Desktop\jHOJIE\R.jpg")
PATH ="C:\Program Files\chromedriver.exe" 
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(executable_path=PATH,
desired_capabilities=dc)
#launch browser
driver.get('http://beta.ovvyapp.com/')


signupbtn = driver.find_element_by_xpath('//*[@id="app"]/section/div/div/div/div[1]/div/div/div/div/a').click()
# print("\033[1;32m Click \n")
fname = driver.find_element_by_xpath('//*[@id="inputFirstName"]')
fname.send_keys('Jhojie')

lname = driver.find_element_by_xpath('//*[@id="inputLastName"]')
lname.send_keys('Jhojie')

dob = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div/input')
dob.send_keys('09/07/1995')

mobileNumber = driver.find_element_by_xpath('//*[@id="inputMobileNumber"]')
mobileNumber.send_keys('+639103373780')

emailfield = driver.find_element_by_xpath('//*[@id="inputEmailReg"]')
emailfield.send_keys('jhojie@email.com')

password = driver.find_element_by_xpath('//*[@id="inputPasswordReg"]')
password.send_keys('qwerty123')

cpass = driver.find_element_by_xpath('//*[@id="inputRePassword"]')
cpass.send_keys('qwerty123')

pshow = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div[2]/div[2]/div/div/div/div[7]/div/div/span')
pshow.click()

ctabtn = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div[2]/div[2]/div/div/div/div[9]/div/div[1]/a')
ctabtn.send_keys(Keys.RETURN)

print('OTP SENT')
time.sleep(30)

verifybtn = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div[2]/div[2]/div/div/a')
verifybtn.send_keys(Keys.RETURN)

#selectservice
time.sleep(30)
selectservice = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[4]/div')
selectservice.click()

nextbtn = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div[4]/div[2]/div/div[3]/div/div[1]/a')
nextbtn.click()

#selectfreelance

selectfreelance = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div/div/div[3]/div[1]/div/div[2]/label/h3')
selectfreelance.click()

nric = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div/div/div[3]/div[3]/div/div/div[1]/div/div[1]/div/form/div/input')
nric.send_keys('1234578')

selectgender = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div/div/div[3]/div[3]/div/div/div[1]/div/div[2]/div/div/div[1]')
selectgender.click()

driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div/div/div[3]/div[3]/div/div/div[2]/div/a/div').send_keys(Imagepath)

nextbtn1 = driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div/div/div[3]/div[3]/div/div/div[3]/div/div[1]/a')
nextbtn1.click()
#obtain with get_log()
# for e in driver.get_log('browser'):
#    print(e)




 
