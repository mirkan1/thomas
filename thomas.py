from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

# firefox lokasyionunu ver
#binary = FirefoxBinary('C://Program Files//Mozilla Firefox//firefox.exe')
#profile = webdriver.FirefoxProfile('C://Users//MBG//AppData//Local//Mozilla//Firefox//Profiles//0ej4htv6.default')#random.randint(0, len(listdir(profile_dic))) -1])
browser = webdriver.Firefox()#firefox_binary=binary, firefox_profile=profile)
actions = ActionChains(browser) #divsiz yazmak icin

USERNAME = 'tilaveryunus@gmail.com'
PASSWORD = 'mirkanbaba123'
MEMBER_LIB = []

def access_discord():
	browser.get('http://discord.com/login')
	sleep(15)
	email_input = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input')
	email_input.send_keys(USERNAME)
	password_input = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input')
	password_input.send_keys(PASSWORD)
	login_button = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/button[2]/div')
	login_button.click()
	invitation_pass()

def invitation_pass():
	sleep(15)
	browser.get('https://discordapp.com/invite/35vucQS')
	try:
		browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/section/div/button').click()
		browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/section/div/button').click()
	except:
		pass
	return group_members()
	#import pdb; pdb.set_trace()
	#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def create_account():
	pass

def bypass_reCaptcha():
	pass

def group_access():
	pass

def look_for_error():
	pass

def write_down():
	pass

def member_search(members):
	for member in members:
		print(member.text, member.text not in MEMBER_LIB)
		if member.text not in MEMBER_LIB:
			MEMBER_LIB.append(member.text)
			member.click()
			actions.send_keys("Do you know supremepumps? https://supremepumps.co")
			actions.perform()
			sleep(0.25)
			actions.send_keys(Keys.ENTER)
			actions.perform()
			sleep(random.randint(5, 25))
			return invitation_pass()
		else:
			print(member.text, "in MEMBER_LIB")

def group_members():
	sleep(15)
	import pdb; pdb.set_trace()
	scroll_div = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]')
	members = browser.find_elements_by_class_name('username-_4ZSMR')
	for i in range(80):
		scroll_div.send_keys(Keys.PAGE_UP)
	member_search(members)

	scroll_div = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]')
	members = browser.find_elements_by_class_name('username-_4ZSMR')
	for i in range(100):
		scroll_div.send_keys(Keys.PAGE_UP)
	member_search(members)
	print(MEMBER_LIB, "--NONE LEFT--")
			

		# try:
		# 	scroll_count = 0
		# 	for i in range(20):
		# 		member[i].click()
		# 		scroll_div = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]')
		# 		#scroll_div = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]')
		# 		for i in range(20):
		# 			scroll_div.send_keys(Keys.PAGE_DOWN)
		# 		for i in range(20):
		# 			scroll_div.send_keys(Keys.ARROW_DOWN)
		# 		print('SCROLL ', scroll_count)
		# 		scroll_count+=1
		# 	for i in range(len(member)):
		# 		member[i].click()
		# 		actions.send_keys("Do you know supremepumps? https://supremepumps.co")
		# 		actions.perform()
		# 		actions.send_keys(Keys.ENTER)
		# 		actions.perform()
		# 		sleep(random.randint(5, 25))
		# 		invitation_pass()

		# except:
		# 	for i in range(20):
		# 		scroll_div.send_keys(Keys.ARROW_DOWN)
		# 		sleep(0.25)


try:
	access_discord()
	group_members()
except:
	if browser.current_url == "https://discordapp.com/activity":
		mail = browse.get_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div[4]/div[1]")
		mail.click()
		print(mail)
		# Maile gidecek oradan maili onaylayacak, ya da telefondan yapacak bu isi 
	raise
# browser.get('https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python')
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")