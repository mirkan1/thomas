from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search, match
from selenium.webdriver.common.action_chains import ActionChains
import random, requests, sys, os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from os import listdir
import random

info = {
	'login': 'http://www.getsmscode.com/do.php?action=login&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70',
	'getmobile': 'http://www.getsmscode.com/do.php?action=getmobile&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70&pid=10',
	'getsms': 'http://www.getsmscode.com/do.php?action=getsms&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70&pid=10&mobile=%s&author=seleniumcrypt@gmail.com',
	'addblack': 'http://www.getsmscode.com/do.php?action=addblack&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70&pid=10&mobile=%s',
	'mobilelist': 'http://www.getsmscode.com/do.php?action=mobilelist&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70'
	}

def get_key(sms, driver):
	"""Waits for code to appear via API. If the code is not recieved restarts whole program"""
	print(sms)
	count = 0
	while True:
		reply = requests.get(info['getsms'] % (sms)).text
		print(count, reply)
		if reply[-5:].isdigit():
			reply = reply[-5:]
			break
		# if reply != 'Message|not receive':
		# elif reply == "Message|mobile number not found!":
		if count > 15:
			import pdb; pdb.set_trace()
			# give driver here to driver
			driver.quit()
			print("%s is blacklisted" % (sms))
			requests.get(info['addblack'] % (sms))
			return get_key(str(requests.get(info['getmobile']).text))
		count += 1
		sleep(11)
	import pdb; pdb.set_trace()
	actions = ActionChains(driver) #divsiz yazmak icin
	actions.send_keys(reply)
	actions.perform()
	#bozuk
	return
	return we_done(reply, driver)

def verify_by_phone(driver):
	actions = ActionChains(driver) #divsiz yazmak icin
	driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div[4]/div").click()
	driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/div").click()
	actions.send_keys("china") #china
	actions.perform()
	driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/div[2]/div[3]/div[1]/div[1]").click()
	driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/button").click()
	sleep(1)
	sms = requests.get(info['getmobile']).text
	driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/input").send_keys(str(sms)[2:]) #send phone numberfrom get_china_num
	return get_key(sms, driver)
	#sleep(180)
	#print("I hope you done, cuz im done")

def replace_file():
	"""If we_done is succeded this function creates new file on desired location and replace webappstore.sqlite from temp location to desired location"""
	for i in os.listdir(temp):
		if match("rust", i):
			if os.path.isdir(temp + "//" + i):
				print("passed isdir")
				for j in os.listdir(temp + "//" + i):
					if match("webappsstore", j):
						print("passeed webapp")
						os.mkdir(new_location + "//" + str(len(os.listdir(new_location)) + 1))
						os.rename(temp + "//" + i + "//" + j, new_location + "//" + str(len(os.listdir(new_location))) + "//" + j)
	sys.exit()

def look_for_error(driver, sms, **kwargs):
	sleep(10)
	for error_might_be in driver.find_elements_by_xpath("//h4[@class]"):
			if error_might_be.get_attribute("class") == "md_simple_header":
				# try:
					driver.find_element_by_xpath("//a[@class='error_modal_details_link']").click()
					sleep(2)
					whole_message = driver.find_element_by_css_selector(".error_modal_details").text#"/html/body/div[5]/div[2]/div/div/div[1]/div[2]/textarea").text   .error_modal_details
					error_message = search('"error_message":"', whole_message)
					wait_time = whole_message[error_message.end():].split("_")[-1].split('"')[0]
					print(wait_time)
					if wait_time == "PRIVATE" or wait_time == "FORBIDDEN":
						count = 0
						while True:
							count += 1
							reply = requests.get(info['getsms'] % (sms)).text
							print(count, reply)
						break
					elif wait_time == "BANNED":
						print("%s is blacklisted" % (sms))
						requests.get(info['addblack'] % (sms))
						driver.quit()
						return create_account(requests.get(info['getmobile']).text)
					elif wait_time == "MUCH" or  wait_time == "CHANNEL":
						# profile_num += 1
						# prof_change(profile_num)
						# log_it()
						break
					# try:
					# 	if int(wait_time).__class__ == int:
					# 		# profile_num += 1
					# 		# prof_change(profile_num)
					# 		break
					# 	else:
					# 		break
					# 	# print("Waiting {} mins".format(round(int(wait_time) / 60)))
					# 	# sleep(int(wait_time) + 5)
					# except:
					# 	break
					else:
						continue
				# except:
				# 	print("passed")
				# 	pass
	return get_key(driver, sms)


# create_account(str(requests.get(info['getmobile']).text))





num = requests.get(info['getmobile']).text
#print(num)

def run(num):
	print(requests.get(info['login']).text, num[3:])
	while True:
		try:
			sms = requests.get(info['getsms'] % (num)).text
			print(sms)
			if sms != 'Message|not receive':
				print("yap bakam bi, sonra duzeltirsin")
			sleep(10)
		except:
			print("banned")
			requests.get(info['addblack'] % (num)).text
			return run(requests.get(info['getmobile']).text)
#print(requests.get(info['getmobile']).text)
#run(requests.get(info['getmobile']).text)
