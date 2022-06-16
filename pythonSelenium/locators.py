from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Rahul")       - deprecated
# driver.find_element(by=By.NAME, value="name").send_keys("Rahul")
# driver.find_element_by_css_selector("input[name='name']").send_keys("Garg")  - deprecated

driver.find_element(by=By.CSS_SELECTOR, value="input[name='name']").send_keys("RAHUL")
driver.find_element(by=By.NAME, value="email").send_keys("rahul123@yopmail.com")

# driver.find_element_by_id("exampleCheck1").click()           - deprecated

driver.find_element(by=By.ID, value="exampleCheck1").click()

# Select class provides the method to handle the options in dropdown.
# This way we can handle static dropdown in Selenium.
drop1 = Select(driver.find_element(by=By.ID, value="exampleFormControlSelect1"))
drop1.select_by_index(1)
drop1.select_by_visible_text("Male")
# drop1.select_by_value("Male")   - if value is present in the HTML

driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
# print(driver.find_element(by=By.CLASS_NAME, value="alert-success").text)

Msg = driver.find_element(by=By.CLASS_NAME, value="alert-success").text

assert "Success" in Msg      # Pass
# assert "Successess" in Msg   # Fail
# assert "Success! The Form has been submitted successfully!." in Msg

# [class*='alert-success']  - CSS regular expression
# //*[contains(@class, 'alert-success')]  - xpath regular expression

