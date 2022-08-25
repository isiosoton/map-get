import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def change_data(ku,tyoumei,tyoume,gaiku):
    gaiku = gaiku.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
    gaiku += "番"
    return chiba_sewage(ku,tyoumei,tyoume,gaiku)


def push_button(driver,ku,tyomei,tyoume,gaiku):
    try:
        # 街区ボタン選択
        element = driver.find_element(By.XPATH,'//*[@id="ELM_CMB_LEV1"]')
        element_select = Select(element)
        element_select.select_by_visible_text(ku)
        element = driver.find_element(By.XPATH,'//*[@id="ELM_CMB_LEV2"]')
        element_select = Select(element)
        element_select.select_by_visible_text(tyomei)
        element = driver.find_element(By.XPATH,'//*[@id="ELM_CMB_LEV3"]')
        element_select = Select(element)
        element_select.select_by_visible_text(tyoume)
        element = driver.find_element(By.XPATH,'//*[@id="ELM_CMB_LEV4"]')
        element_select = Select(element)
        element_select.select_by_visible_text(gaiku)
        return True
    except:
        return False

def chiba_sewage(ku = "中央区", tyomei = "青葉町", tyoume = "丁目なし", gaiku = "３５９番地"):
    object_return = {"spot":False,"picture":False,"ku":ku,"tyoumei":tyomei,"tyoume":tyoume,"gaiku":gaiku}
    FILENAME = "./picture/sewage.png"
    
    try:
        # ページ開くまで
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("http://s-page.tumsy.com/chibagesui/index.html")
        iframe = driver.find_element(By.TAG_NAME,"frame")
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH,'//*[@id="LinkButton1"]').click()
    except:
        return object_return

    if push_button(driver,ku,tyomei,tyoume,gaiku):
        object_return["spot"] = True
    else:
        gaiku = tyoume.replace("丁目", "番地")
        object_return["gaiku"] = gaiku
        tyoume = "丁目なし"
        object_return["tyoume"] = tyoume
        if push_button(driver,ku,tyomei,tyoume,gaiku):
            object_return["spot"] = True
        else:
            object_return["spot"] = False
            return object_return

    try:
        # ページ開けた後
        driver.find_element(By.XPATH,'//*[@id="btnAddSchDlgOK"]').click()
        time.sleep(4)
        driver.save_screenshot(FILENAME)
        driver.quit()
    except:
        object_return["picture"] = False
        return object_return

    object_return["picture"] = True
    return object_return

# 動作確認用
if __name__ == "__main__":
    # print(change_data("花見川区","朝日ケ丘","１丁目","1"))
    # print(change_data("花見川区","天戸町","１丁目","15"))
    # print(change_data("花見川区","天戸町","丁目なし","１番地"))
    print(change_data("稲毛区","稲毛","３丁目","7"))

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

