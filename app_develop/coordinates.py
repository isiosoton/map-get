from xml.dom.minidom import Element
import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def coordinates(jusyo):
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(2)
        driver.get("https://www.geocoding.jp/?q="+jusyo)
        ido = driver.find_element(By.XPATH,'//*[@id="result"]/span[2]/b[1]').text
        keido = driver.find_element(By.XPATH,'//*[@id="result"]/span[2]/b[2]').text
    except:
        return {"accept":False,"ido":None,"keido":None}
    return {"accept":True,"ido":ido,"keido":keido}

if __name__ == "__main__":
    coordinates("埼玉県さいたま市浦和区高砂3丁目15−1")