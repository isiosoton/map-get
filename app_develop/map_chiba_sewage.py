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
# time.sleep(5)
# driver.find_elements(By.XPATH,'//*[@id="title"]').click()

# driver.find_element(By.XPATH,'//*[@id="title"]').send_keys(Keys.PAGE_DOWN) 

time.sleep(5)
# driver.find_element(By.XPATH,'//*[@id="LinkButton1"]').click()

# element = driver.find_element(By.XPATH,'//*[@id="LinkButton1"]')

# 要素を表示するようスクロール
# ActionChains(driver).move_to_element(element).perform()

# driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)

# クリック
# element.click()

# element = driver.find_element(By.ID,'#LinkButton1')
# driver.execute_script('arguments[0].click();', element)
# driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL, '0')
# driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)

# consoleでは下記JSコードが動く。
# document.querySelector("#LinkButton1").click();

# driver.execute_script("window.scrollTo(0, document.querySelector('#form1').scrollHeight);")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script('document.querySelector("#LinkButton1").click();')

# driver.find_element(By.CLASS_NAME,'agr_btn').click()
# driver.find_element(By.ID,'LinkButton1').click()
# element = driver.find_elements(By.XPATH,'//*[@id="LinkButton1"]')
# driver.execute_script('doPostBack("LinkButton1",'')', element)
# driver.execute_script('document.getElementById("LinkButton1").click();')
# driver.execute_script('document.getElementById("#LinkButton1").onclick();')
# element = driver.execute_script('document.querySelector("#LinkButton1").onclick();')
# element
# driver.execute_script('#LinkButton1.click();', element)
# driver.execute_script('LinkButton1[0].click();', element)
# <a id="LinkButton1" href="javascript:__doPostBack('LinkButton1','')"></a>
# print(element.text)
# driver.switch_to.frame(element)
# driver.switch_to.frame("element")
time.sleep(10)
# driver.quit()

