from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element(by=By.LINK_TEXT, value="Shop").click()

prodName = driver.find_elements(by=By.XPATH, value="//h4[@class='card-title']")

# 2 ways to select blackberry product
# child-parent-child traversing

# for prod in prodName:
#     itemName = prod.text
#     if itemName == "Blackberry":
#         prod.find_element(by=By.XPATH, value="parent::div/parent::div/div/button").click()

products = driver.find_elements(by=By.XPATH, value="//*[@class='card h-100']")

for product in products:
    prodName = product.find_element(by=By.XPATH, value="div/h4").text
    if prodName == "Blackberry":
        product.find_element(by=By.XPATH, value="div/button").click()

driver.find_element(by=By.CSS_SELECTOR, value="a[class*='btn-primary']").click()
driver.find_element(by=By.CSS_SELECTOR, value="[class='btn btn-success']").click()
driver.find_element(by=By.CSS_SELECTOR, value="#country").send_keys("ind")

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(by=By.LINK_TEXT, value="India").click()
driver.find_element(by=By.XPATH, value="//label[@for='checkbox2']").click()
driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
successMsg = driver.find_element(by=By.CSS_SELECTOR, value="[class*='alert alert-success']").text

assert "Success! Thank you" in successMsg

driver.get_screenshot_as_file("screenshot.png")
