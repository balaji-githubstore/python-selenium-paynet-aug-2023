import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://google.com")

action=ActionChains(driver)

action.key_down(Keys.SHIFT).send_keys("hello world").key_up(Keys.UP).pause(1)\
    .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).pause(1)\
    .send_keys(Keys.ENTER).perform()


time.sleep(5)
driver.quit()
