import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# implicit wait
# explicit wait
# pause the test for few seconds using Time class

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)

# wait until 5 sec if the object is not displayed
# Global wait
# 1.5 sec to reach next page - execution will resume in 1.5 sec
# if object do not show up at all, then max time test will wait is 5 sec

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(by=By.CSS_SELECTOR, value=".search-keyword").send_keys("or")
time.sleep(3)
# prod = driver.find_elements(by=By.XPATH, value="//div[@class='product-action']/button")
prod = len(driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']"))
# print(len(driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']")))
assert prod == 2

addProduct = driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']")

for add in addProduct:
    add.click()

# addProduct[0].click()      - another way to add items in the cart
# addProduct[1].click()

driver.find_element(by=By.CSS_SELECTOR, value="img[alt='Cart']").click()
driver.find_element(by=By.XPATH, value="//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(by=By.CSS_SELECTOR, value=".promocode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CLASS_NAME, value="promoBtn").click()
print(driver.find_element(by=By.CSS_SELECTOR, value="span.promoInfo").text)