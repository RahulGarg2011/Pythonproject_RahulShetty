import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(by=By.XPATH, value="//input[@type='search']").send_keys("ca")
# time.sleep(1)
# plusbtn = driver.find_elements(by=By.XPATH, value="//a[text()='+']")

plusbtn = driver.find_elements(by=By.XPATH, value="//a[@class='increment']")

try:
    for plusbutton in plusbtn:  # not working without time.sleep
        plusbutton.click()
except Exception as e:
    plusbtn = driver.find_elements(by=By.XPATH, value="//a[@class='increment']")
    for plusbutton in plusbtn:  # not working without time.sleep
        plusbutton.click()


addtoCart = driver.find_elements(by=By.XPATH, value="//button[text()='ADD TO CART']")
for add in addtoCart:
    add.click()

driver.find_element(by=By.CSS_SELECTOR, value="a.cart-icon").click()
driver.find_element(by=By.XPATH, value="(//a[@class='product-remove'])[2]").click()
driver.find_element(by=By.XPATH, value="//button[text()='PROCEED TO CHECKOUT']").click()

# iteminCart = driver.find_elements(by=By.XPATH, value="//table[@id='productCartTables']/tbody/tr/td[2]/p")
productsinCart = driver.find_elements(by=By.CSS_SELECTOR, value=".product-name")
# print(productsinCart[0].text)
# print(productsinCart[1].text)
# print(productsinCart[2].text)
# print(productsinCart[3].text)

for i in productsinCart:
    print(i.text)






