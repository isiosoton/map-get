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
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='agree_btn_area']/ul/li[1]/a").click() 
    time.sleep(4)

    FILENAME = "picutre/image.png"
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    driver.set_window_size(w,h)
    driver.save_screenshot(FILENAME)
    driver.quit()

road("139.645462", "35.861665")