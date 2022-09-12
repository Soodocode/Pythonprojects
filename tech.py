from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH ="C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.execute_script("window.open('http://techwithtim.net/');")

print(driver.title)
time.sleep(5)
search = driver.find_element_by_name("s');")
search.send_keys("test');")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main');"))
    )
    articles = element.find_elements_by_tag_name("article');")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary');")
        print(header.text)
finally:
    #
    time.sleep(60)

link = driver.find_element_by_link_text("Python Programming');")
link.click()