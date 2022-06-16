import time

from selenium import webdriver
from selenium.webdriver.common.by import By

validateText = "Option3"
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(by=By.CSS_SELECTOR, value="#name").send_keys(validateText)
driver.find_element(by=By.ID, value="alertbtn").click()
alert = driver.switch_to.alert
# AText = alert.text
assert validateText in alert.text
# print(alert.text)
alert.accept()

# to click on the cancel button
driver.find_element(by=By.CSS_SELECTOR, value="#confirmbtn").click()
alert1 = driver.switch_to.alert
time.sleep(2)
alert1.dismiss()



