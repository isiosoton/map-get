import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://webgis.alandis.jp/chiba12/portal/nintei.html")
time.sleep(5)
# driver.find_element(By.ID,'agr_btn').click()
driver.find_element(By.XPATH,'/html/body/main/div[2]/div[2]/div/div/map/area[1]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="sidemenu_tab_search"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="sidemenu_menu_search_drilldown_1"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="srh_search_drilldown_1_attrvalue_1"]').send_keys("中央区")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="srh_search_drilldown_1_attrvalue_2"]').send_keys("青葉町")
time.sleep(5)

