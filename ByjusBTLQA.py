import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(30)
driver.get("https://crm-byjus.goave.ga/")    # To hit URL on the browser

# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
driver.find_element(by=By.CSS_SELECTOR, value="#email").send_keys("admin@example.com")
driver.find_element(by=By.ID, value="password").send_keys("marketing")
driver.find_element(by=By.XPATH, value="//span[text()='Login']").click()
# wait = WebDriverWait(driver, 15)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@href='leads?']")))

print(driver.find_element(by=By.XPATH, value="//h5[contains(text(), 'Dashboard')]").text)
button = driver.find_element(by=By.XPATH, value="//a[@href='leads?']")
# driver.execute_script("arguments[0].click();", button)
button.click()
driver.find_element(By.XPATH, '//a[text()="Other Details"]').click()

button1 = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Advanced Search')]")
# driver.execute_script("arguments[0].click();", button1)
button1.click()
# driver.find_element(by=By.XPATH, value="//span[text()='Franchise']").click()

