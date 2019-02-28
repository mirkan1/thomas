from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import listdir
import random

# firefox lokasyionunu ver

class Thomas:
	binary = FirefoxBinary('C://Program Files//Mozilla Firefox//firefox.exe')
	profile = webdriver.FirefoxProfile('C://Users//MBG//AppData//Roaming//Mozilla//Firefox//Profiles//0ej4htv6.default')#random.randint(0, len(listdir(PROFILE_DIC))) -1])
	browser = webdriver.Firefox(firefox_binary=binary, firefox_profile=profile)
	actions = ActionChains(browser) #divsiz yazmak icin
	def __init__(self):
		self.PROFILE_DIC = 'C://Users//MBG//Desktop//hakan_isi//spam_bot2//new_profiles'
		self.PROFILE_NUM = 0
		self.ACCOUNT_COUNT = 0
		self.DISCORD_GROUPS_COUNT = 0
		self.ACCOUNTS = [
			['tilaveryunus@gmail.com', 'mirkanbaba123'],
		]
		self.DISCORD_GROUPS = ['https://discordapp.com/invite/35vucQS']
		self.MEMBER_LIB = []
		self.ACCOUNT_DIR = ''


	def prof_change(num):
		# banned_list = open("file_info.log", "a")
		# banned_list.write("\n" + str(num))
		# banned_list.close()

		try:
			# banned_list = open("file_info.log", "r").read().split("\n")
			# if str(num) in banned_list:
			# 	return True

			print("New account is {}".format(listdir(self.PROFILE_DIC)[num]))
			self.ACCOUNT_DIR = '%s//%s//' % (self.PROFILE_DIC, listdir(self.PROFILE_DIC)[num])
		except IndexError:
			PROFILE_NUM, num = 0, 0
			print("New account is {}".format(listdir(self.PROFILE_DIC)[num]))
			self.ACCOUNT_DIR = '%s//%s//' % (self.PROFILE_DIC, listdir(self.PROFILE_DIC)[num])

		browser.quit()
		new_profile = webdriver.FirefoxProfile(self.ACCOUNT_DIR)
		browser = webdriver.Firefox(firefox_binary=binary, firefox_profile=new_profile)
		sleep(1800)
		browser.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.spam_txt[random.randint(0, len(Spammer.spam_txt)) -1]))

	def access_discord():
		browser.get('http://discord.com/login')
		sleep(15)
		email_input = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input')
		email_input.send_keys(self.ACCOUNTS[self.ACCOUNT_COUNT][0])
		password_input = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input')
		password_input.send_keys(self.ACCOUNTS[self.ACCOUNT_COUNT][1])
		login_button = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/button[2]/div')
		login_button.click()
		invitation_pass()

	def invitation_pass():
		sleep(15)
		browser.get(self.DISCORD_GROUPS[self.DISCORD_GROUPS_COUNT])
		try:
			browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/section/div/button').click()
			browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/section/div/button').click()
		except:
			try:
				browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
				browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
			except:
				pass
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
			print(member.text, member.text not in self.MEMBER_LIB)
			if member.text not in MEMBER_LIB:
				print(member.text)
				self.MEMBER_LIB.append(member.text)
				member.click()
				actions.send_keys("Do you know supremepumps? https://supremepumps.co")
				actions.perform()
				sleep(0.25)
				actions.send_keys(Keys.ENTER)
				actions.perform()
				sleep(random.randint(5, 25))
				return invitation_pass()
			else:
				pass
				#print(member.text, "in MEMBER_LIB")

	def group_members():
		sleep(15)
		try:
			browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
		except:
			pass
		#import pdb; pdb.set_trace()
		scroll_div = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]')
		for i in range(random.randint(5, 500)):
			if i%100 == 0:
				sleep(3)
			scroll_div.send_keys(Keys.PAGE_UP)
			
		members = browser.find_elements_by_class_name('username-_4ZSMR')
		for member in members:
			if member.text not in MEMBER_LIB:
				print(member.text)
				self.MEMBER_LIB.append(member.text)
				member.click()
				sleep(1)
				actions.perform()
				sleep(random.randint(1, 30))
				return invitation_pass()
			else:
				print(member.text, "in MEMBER_LIB")

		#change discord-group
		print(self.MEMBER_LIB, "--NONE LEFT--")
		self.ACCOUNT_COUNT+=1
		self.DISCORD_GROUPS_COUNT+=1

#import pdb;pdb.set_trace()
while True:
	browser.get("https://discordapp.com/channels/@me")			
	sleep(15)
	mobile_verify_message = browser.find_elements_by_class_name("body-3ROqbj")
	for message in mobile_verify_message:
		if message.text == "VERIFY BY PHONE":
			print("yes")
			self.ACCOUNT_COUNT+=1
			prof_change(self.ACCOUNT_COUNT)
		else:
			print("no")
			prof_change(self.ACCOUNT_COUNT)

# try:
# 	actions.send_keys("Do you know supremepumps? https://supremepumps.co")
# 	actions.send_keys(Keys.ENTER)
# 	access_discord()
# 	group_members()
# except:
# 	if browser.current_url == "https://discordapp.com/activity":
# 		mail = browse.get_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div[4]/div[1]")
# 		mail.click()
# 		print(mail)
# 		# Maile gidecek oradan maili onaylayacak, ya da telefondan yapacak bu is 
	# mobile_verify_message = browser.get_elemets_by_class_name("body-3ROqbj")
	# for message in mobile_verify_message:
	# 	if message.text == "We've detected something out of the ordinary going on. To continue using Discord,":
	# 		print("yes")
	# 		ACCOUNT_COUNT+=1
	# 		return prof_change(ACCOUNT_COUNT)
# 	try:
# 		access_discord()
# 		group_members()
# 	except:
# 		import pdb; pdb.set_trace()
# 	raise
