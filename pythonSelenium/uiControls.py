from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(by=By.XPATH, value="//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    print(checkbox.get_attribute("value"))
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        #print("**********")

# print(checkbox.get_attribute("value"))
# driver.find_element(by=By.XPATH, value="//input[@value='radio3']").click() - to select radio button 3

radio = driver.find_elements(by=By.NAME, value="radioButton")
# radio[0].click()
radio[2].click()
assert radio[2].is_selected()

# radio[4].click()     - list index out of range error

# is_displayed() returns true/false
assert driver.find_element(by=By.CSS_SELECTOR, value="#displayed-text").is_displayed()
driver.find_element(by=By.ID, value="hide-textbox").click()
assert not driver.find_element(by=By.CSS_SELECTOR, value="#displayed-text").is_displayed()
