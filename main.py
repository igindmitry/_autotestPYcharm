import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('F:/Auto_test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login") #open site
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("19id87@list.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("10916145")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(5)
#fill pasport
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Пукич")
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Микас")
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Милославович")
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("4747")
