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

realamt = driver.find_element(by=By.CSS_SELECTOR, value="span.discountAmt").text
print(realamt)

driver.find_element(by=By.CSS_SELECTOR, value=".promocode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CLASS_NAME, value="promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountedamt = driver.find_element(by=By.CSS_SELECTOR, value=".discountAmt").text
print(discountedamt)

assert discountedamt < realamt      # verify if price decreases after applying coupon
# assert float(discountedamt) < int(realamt) - in case values are in decimal

print(driver.find_element(by=By.CSS_SELECTOR, value="span.promoInfo").text)
print("******")

amount = driver.find_elements(by=By.XPATH, value="//tr/td[5]/p")
total = 0
for amt in amount:
    total = total + int(amt.text)    # 75+75=150

print(total)

totalAmount = int(driver.find_element(by=By.CSS_SELECTOR, value=".totAmt").text)
assert total == totalAmount
# assert total == int(totalAmount)
