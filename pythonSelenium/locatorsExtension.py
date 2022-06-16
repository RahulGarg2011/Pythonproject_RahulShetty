from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")

driver.find_element(by=By.CSS_SELECTOR, value="#username").send_keys("Rahul")
driver.find_element(by=By.CSS_SELECTOR, value=".password").send_keys("Garg")
driver.find_element(by=By.CSS_SELECTOR, value=".password").clear()

driver.find_element(by=By.LINK_TEXT, value="Forgot Your Password?").click()
# driver.find_element(by=By.XPATH, value="//a[text()='Forgot Your Password?']").click() -//tagName[text()='xxx']
# driver.find_element(by=By.XPATH, value="//input[@value='Cancel']").click()  - xpath to click on Cancel button

driver.find_element(by=By.CSS_SELECTOR, value="[value='Cancel']").click()  # CSS to click on Cancel button

# //tagName[text()='xxx']
print(driver.find_element(by=By.XPATH, value="//label[text()='Remember me']").text)

# traversing from parent to child
print(driver.find_element(by=By.XPATH, value="//form[@name='login']/div[1]/label").text)
print(driver.find_element(by=By.CSS_SELECTOR, value="form[name='login'] label:nth-child(4)").text)


