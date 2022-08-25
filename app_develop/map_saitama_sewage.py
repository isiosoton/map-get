import chromedriver_binary
import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep



def road(longitude, latitude):
    url = "https://www.sonicweb-asp.jp/saitama_g/map?theme=th_90#pos=" + longitude + "," + latitude
    FILENAME = "./picture/sewage.png"
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(url)
        iframe = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, "//*[@id='agree_btn_area']/ul/li[1]/a").click() 
        time.sleep(4)

        # w = driver.execute_script("return document.body.scrollWidth;")
        # h = driver.execute_script("return document.body.scrollHeight;")
        # driver.set_window_size(w,h)
        driver.save_screenshot(FILENAME)
        driver.quit()
    except:
        return False

    return True

if __name__ == "__main__":
    road("139.645462", "35.861665")