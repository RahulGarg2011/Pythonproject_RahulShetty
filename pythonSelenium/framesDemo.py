from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element(by=By.TAG_NAME, value="p").clear()
driver.find_element(by=By.TAG_NAME, value="p").send_keys("I am able to write my code now")

driver.switch_to.default_content()
titletext = driver.find_element(by=By.TAG_NAME, value="h3").text
print(titletext)

