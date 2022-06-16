import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(by=By.ID, value="autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(by=By.CSS_SELECTOR, value="li[class='ui-menu-item'] a")
print(len(countries))
for i in countries:
    if i.text == "India":
        i.click()
        break

print(driver.find_element(by=By.ID, value="autosuggest").text)  # won't print India in Output

assert driver.find_element(by=By.ID, value="autosuggest").get_attribute("value") == "India"





