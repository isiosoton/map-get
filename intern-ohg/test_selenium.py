import chromedriver_binary
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# File Name
#FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")
FILENAME = "image.png"
# set driver and url
driver = webdriver.Chrome()
url = 'https://www.google.co.jp/maps/place/GINZA+SIX/@35.6696559,139.7617989,17z/data=!3m2!4b1!5s0x60188be649ab2755:0x641a401ce3acec60!4m5!3m4!1s0x60188bef472c0001:0xcfcb0363f18109fc!8m2!3d35.6696559!4d139.7639876?hl=ja&authuser=0'
driver.get(url)

# get width and height of the page
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# set window size
driver.set_window_size(w,h)

# Get Screen Shot
driver.save_screenshot(FILENAME)

# Close Web Browser
driver.quit()