import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

map_spots = {"spots":["千葉県","埼玉県"], "items":["道路","下水"]}

# driver = webdriver.Chrome()

# driver.get("https://www.google.co.jp/maps")
# driver.find_element(By.XPATH,'//*[@id="searchboxinput"]').send_keys("GINZA SIX")
# driver.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]').click()
# time.sleep(10)

driver = webdriver.Chrome()
driver.get("http://s-page.tumsy.com/chibagesui/index.html")

# time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="LinkButton2"]').click()
driver.find_element(By.XPATH,'//*[@id="main-contents"]/section/article/div[4]/div/p[3]/select').send_keys("中央区")
# driver.find_element(By.XPATH,'//*[@id="searchboxinput"]').send_keys("GINZA SIX")
# Select(driver.find_element_by_id('dropdown')).select_by_visible_text('3番目')
# time.sleep(10)

# 1.操作するブラウザ
driver = webdriver.Chrome()

# 2.操作するページを開く（ブログのこのページ）
driver.get('https://prcmyself.com/how-to-select-from-list-or-pull-down-selenium')

# 年度を指定
driver.find_element(By.XPATH,'//*[@id="main-contents"]/section/article/div[4]/div/p[3]/select').send_keys("2021")

FILENAME = "test_selenium.png"
driver.save_screenshot(FILENAME)
# driver.quit()
