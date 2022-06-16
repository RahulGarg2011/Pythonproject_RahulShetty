from selenium import webdriver

# browser exposes an executable files
# Through selenium test we need to invoke the executable file which will then invoke actual browser
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://rahulshettyacademy.com/")    # To hit URL on the browser

driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://courses.rahulshettyacademy.com/courses")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()

