import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

# implicit wait
# explicit wait
# pause the test for few seconds using Time class
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(by=By.CSS_SELECTOR, value=".search-keyword").send_keys("or")
time.sleep(3)
# prod = driver.find_elements(by=By.XPATH, value="//div[@class='product-action']/button")
prod = len(driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']"))
# print(len(driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']")))
assert prod == 2

addProduct = driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']")

# for add in addProduct:
#     add.click()

# //button[text()='ADD TO CART']/parent::div/parent::div/h4 - to traverse from child to parent and avoiding for loop

for add in addProduct:   # To compare the listing of products on page1 and page2
    print(add.find_element(by=By.XPATH, value="parent::div/parent::div/h4").text)
    add.click()

# addProduct[0].click()      - another way to add items in the cart
# addProduct[1].click()

driver.find_element(by=By.CSS_SELECTOR, value="img[alt='Cart']").click()
driver.find_element(by=By.XPATH, value="//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promocode")))

driver.find_element(by=By.CSS_SELECTOR, value=".promocode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CLASS_NAME, value="promoBtn").click()

# doubt on line no 39 abt multiple brackets
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element(by=By.CSS_SELECTOR, value="span.promoInfo").text)
