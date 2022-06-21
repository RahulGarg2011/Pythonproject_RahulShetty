import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# action = ActionChains(driver)
# mouse = driver.find_element(by=By.CSS_SELECTOR, value="#mousehover")
# action.move_to_element(mouse).perform()
# relo = driver.find_element(by=By.LINK_TEXT, value="Reload")
# # relo = driver.find_element(by=By.LINK_TEXT, value="Top")
# time.sleep(2)
# action.move_to_element(relo).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element(by=By.ID, value="double-click")).perform()  # to right-click

action.double_click(driver.find_element(by=By.ID, value="double-click")).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
