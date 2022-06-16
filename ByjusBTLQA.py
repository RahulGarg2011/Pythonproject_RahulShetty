from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://crm-byjus.goave.ga/")    # To hit URL on the browser

driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.refresh()


