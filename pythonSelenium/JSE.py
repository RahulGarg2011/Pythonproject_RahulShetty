# Javascript DOM can access any element on web page just like how selenium does
# Selenium have a method to execute javascript code in it
import time
from _ast import arguments

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element(by=By.NAME, value="name").send_keys("Infobeans")

print(driver.find_element(by=By.NAME, value="name").text)    # won't print as it is written by selenium
print(driver.find_element(by=By.NAME, value="name").get_attribute("value"))  # this method has been inherited from DOM
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopBtn = driver.find_element(by=By.XPATH, value="//a[contains(text(),'Shop')]")
driver.execute_script("arguments[0].click();", shopBtn)
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

