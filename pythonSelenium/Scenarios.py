import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# To validate whether product displayed on page 1 is same as page2 which is checkout page.

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

list1 = []
list2 = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(by=By.CSS_SELECTOR, value=".search-keyword").send_keys("or")
time.sleep(3)

prod = len(driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']"))
# print(len(driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']")))
assert prod == 2
addProduct = driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']")

# //button[text()='ADD TO CART']/parent::div/parent::div/h4 - to traverse from child to parent and avoiding for loop

for add in addProduct:
    # print(add.find_element(by=By.XPATH, value="parent::div/parent::div/h4").text)
    list1.append(add.find_element(by=By.XPATH, value="parent::div/parent::div/h4").text)
    add.click()
print(list1)

driver.find_element(by=By.CSS_SELECTOR, value="img[alt='Cart']").click()
driver.find_element(by=By.XPATH, value="//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promocode")))
VegetableName = driver.find_elements(by=By.CSS_SELECTOR, value=".product-name")

for veg in VegetableName:
    list2.append(veg.text)
print(list2)
assert list1 == list2

driver.find_element(by=By.CSS_SELECTOR, value=".promocode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CLASS_NAME, value="promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element(by=By.CSS_SELECTOR, value="span.promoInfo").text)
