import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


options=webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-notifications")
options.add_argument("start-maximized")
# options.add_experimental_option("prefs",{"download.default_directory":"C:\\"})
driver = webdriver.Chrome(options)
driver.maximize_window()
# driver.implicitly_wait(30)

driver.get("https://www.irctc.co.in/nget/train-search")


print(driver.title)
driver.quit()