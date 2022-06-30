# This code is written to handle StaleElementReferenceException
import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(15)
driver.get('https://classic.freecrm.com/index.html')
driver.maximize_window()
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys('Rahul')
password.send_keys('Rahul123')
print(id(username))
print(id(password))
time.sleep(5)
driver.refresh()
print(id(username))
print(id(password))

try:
    username.send_keys('Rahul')
    password.send_keys('Rahul123')
except StaleElementReferenceException:
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    username.send_keys('Rahul')
    password.send_keys('Rahul123')



