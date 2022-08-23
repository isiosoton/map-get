from xml.dom.minidom import Element
import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def chiba_street(oojimei = "中央区", jityoumei = "青葉町", gaiku = "7"):
    FILENAME = "./picture/image.png"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://webgis.alandis.jp/chiba12/portal/nintei.html")
    time.sleep(1)
    # driver.find_element(By.ID,'agr_btn').click()
    driver.find_element(By.XPATH,'/html/body/main/div[2]/div[2]/div/div/map/area[1]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="sidemenu_tab_search"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="sidemenu_menu_search_drilldown_1"]').click()
    time.sleep(1)
    element = driver.find_element(By.XPATH,'//*[@id="srh_search_drilldown_1_attrvalue_1"]')
    element_select = Select(element)
    element_select.select_by_value(oojimei)
    time.sleep(5)
    element = driver.find_element(By.XPATH,'//*[@id="srh_search_drilldown_1_attrvalue_2"]')
    element_select = Select(element)
    element_select.select_by_value(jityoumei)
    time.sleep(5)
    element = driver.find_element(By.XPATH,'//*[@id="srh_search_drilldown_1_attrvalue_3"]')
    element_select = Select(element)
    element_select.select_by_value(gaiku)
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="sidemenu_tab_search"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="index_hidden"]').click()
    time.sleep(1)
    driver.save_screenshot(FILENAME)
    driver.quit()
    return True

# 動作確認用
# chiba_street("花見川区","朝日ケ丘１丁目","2")

