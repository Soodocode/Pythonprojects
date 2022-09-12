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
driver.execute_script("window.open('https://beta.basicbros.ph/login?type=0');")
