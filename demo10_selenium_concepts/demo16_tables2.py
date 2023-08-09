import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://datatables.net/extensions/select/examples/initialisation/checkbox.html")

#row count
web_elements=driver.find_elements(By.XPATH,"//table[@id='example']/tbody/tr")
print(len(web_elements))

for i in range(1, len(web_elements)):
    name = driver.find_element(By.XPATH, f"//table[@id='example']/tbody/tr[{i}]/td[2]").text
    print(name)
    # write logic to click on checkbox when name is Brenden Wagner
    if name == "Brenden Wagner":
        driver.find_element(By.XPATH, f"//table[@id='example']/tbody/tr[{i}]/td[1]").click()
        break

time.sleep(5)
driver.quit()
