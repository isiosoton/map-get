import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def chiba_sewage(ku = "中央区", tyomei = "青葉町", tyoume = "丁目なし", gaiku = "３５９番地"):
    FILENAME = "./picture/image.png"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://s-page.tumsy.com/chibagesui/index.html")
    time.sleep(1)
    iframe = driver.find_element(By.TAG_NAME,"frame")
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH,'//*[@id="LinkButton1"]').click()
    time.sleep(1)
    element = driver.find_element(By.XPATH,'//*[@id="ELM_CMB_LEV1"]')
    element_select = Select(element)
    element_select.select_by_visible_text(ku)
    time.sleep(1)
    element = driver.find_element(By.XPATH,'//*[@id="ELM_CMB_LEV2"]')
    element_select = Select(element)
    element_select.select_by_visible_text(tyomei)
    time.sleep(1)
    element = driver.find_element(By.XPATH,'//*[@id="ELM_CMB_LEV3"]')
    element_select = Select(element)
    element_select.select_by_visible_text(tyoume)
    time.sleep(1)
    element = driver.find_element(By.XPATH,'//*[@id="ELM_CMB_LEV4"]')
    element_select = Select(element)
    element_select.select_by_visible_text(gaiku)
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="btnAddSchDlgOK"]').click()
    time.sleep(2)
    driver.save_screenshot(FILENAME)
    driver.quit()
    return True

# 動作確認用
# chiba_sewage("花見川区","天戸町","丁目なし","１番地")

# handle_array = driver.window_handles
# driver.switch_to.window(driver.window_handles[0])
# driver.get("http://s-page.tumsy.com/chibagesui/PrintPage.aspx")
# time.sleep(5)
# driver.find_element(By.XPATH,'//*[@id="btnA3L"]').click()
# time.sleep(5)
# driver.find_element(By.XPATH,'//*[@id="btnDownload"]').click()
# driver.find_element(By.XPATH,'//*[@id="OpenPrintPage"]').click()
# time.sleep(10)
# driver.quit()

