from xml.dom.minidom import Element
import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def chiba_street(tiba_object):
    oojimei = tiba_object["ku"]
    tyoumei = tiba_object["tyoumei"]
    tyoume = tiba_object["tyoume"]
    if tyoume == "丁目なし":
        tyoume = ""
    jityoumei = tyoumei + tyoume
    gaiku = tiba_object["gaiku"].replace("番地", "").replace("番", "").translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))

    # oojimei = "中央区", jityoumei = "青葉町", gaiku = "7"
    FILENAME = "./picture/street.png"
    
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(200)
        driver.maximize_window()
        driver.get("https://webgis.alandis.jp/chiba12/portal/nintei.html")
        driver.find_element(By.XPATH,'/html/body/main/div[2]/div[2]/div/div/map/area[1]').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="sidemenu_tab_search"]').click()
        # time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="sidemenu_menu_search_drilldown_1"]').click()
        # time.sleep(1)
        element = driver.find_element(By.XPATH,'//*[@id="srh_search_drilldown_1_attrvalue_1"]')
        element_select = Select(element)
        element_select.select_by_value(oojimei)
        # time.sleep(5)
        element = driver.find_element(By.XPATH,'//*[@id="srh_search_drilldown_1_attrvalue_2"]')
        element_select = Select(element)
        element_select.select_by_value(jityoumei)
        # time.sleep(5)
        element = driver.find_element(By.XPATH,'//*[@id="srh_search_drilldown_1_attrvalue_3"]')
        element_select = Select(element)
        element_select.select_by_value(gaiku)
        # time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="sidemenu_tab_search"]').click()
        # time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="index_hidden"]').click()
        time.sleep(4)
        driver.save_screenshot(FILENAME)
        driver.quit()
    except:
        return False

    return True

if __name__ == "__main__":
    chiba_street({'spot': True, 'picture': True, 'ku': '花見川区', 'tyoumei': '朝日ケ丘', 'tyoume': '１丁目', 'gaiku': '１番'})
    chiba_street({'spot': True, 'picture': True, 'ku': '花見川区', 'tyoumei': '天戸町', 'tyoume': '丁目なし', 'gaiku': '１番地'})

