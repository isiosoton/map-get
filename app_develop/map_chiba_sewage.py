import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://s-page.tumsy.com/chibagesui/index.html")
time.sleep(5)
# driver.find_element(By.ID,'agr_btn').click()
driver.find_element(By.XPATH,'//*[@id="LinkButton1"]').click()
