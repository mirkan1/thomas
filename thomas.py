import time
from os import listdir
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# PROFILE_DIR = 'C://Users//Raq//AppData//Local//Mozilla//Firefox'
# profile = webdriver.FirefoxProfile(PROFILE_DIR + '//%s//' % listdir(PROFILE_DIR)[0])

## driver doest work for some reason
driver = webdriver.Firefox()
time.sleep(10)
print('slept')
driver.get("https://www.discord.com")