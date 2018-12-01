import time
from os import listdir
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Discord scroll table that includes people in it
scroll_div_class = "scroller-2FKFPG firefoxFixScrollFlex-cnI2ix members-1998pB"
user_div_class = "nameTag-3p0yK- nameTag-m8r81H"
span_class = "usernameOnline-3jr_0Y username-1cB_5E"

# PROFILE_DIR = 'C://Users//Raq//AppData//Local//Mozilla//Firefox'
# profile = webdriver.FirefoxProfile(PROFILE_DIR + '//%s//' % listdir(PROFILE_DIR)[0])

## driver doest work for some reason
driver = webdriver.Firefox()
time.sleep(10)
print('slept')
driver.get("https://www.discord.com")
