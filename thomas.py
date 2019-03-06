from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import listdir
import random
import getsmscode
from faker import Faker

# firefox lokasyionunu ver

class Thomas():
	binary = FirefoxBinary('C://Program Files//Mozilla Firefox//firefox.exe')
	#windows_profile = webdriver.FirefoxProfile('C://Users//MBG//AppData//Roaming//Mozilla//Firefox//Profiles//0ej4htv6.default')#random.randint(0, len(listdir(PROFILE_DIC))) -1])
	lubuntu_prof = webdriver.FirefoxProfile('//home//raq//Desktop//Others//hakan_is//new_profiles//1')#random.randint(0, len(listdir(PROFILE_DIC))) -1])
	driver = webdriver.Firefox(firefox_profile=lubuntu_profile)#, firefox_binary=binary)
	actions = ActionChains(driver) #divsiz yazmak icin

	def __init__(self):
		#self.PROFILE_DIC = 'C://Users//MBG//Desktop//hakan_isi//spam_bot2//new_profiles'
		self.PROFILE_DIC = '//home//raq//Desktop//Others//hakan_is//new_profiles//'
		self.PROFILE_NUM = 0
		self.ACCOUNT_COUNT = 0
		self.DISCORD_GROUPS_COUNT = 0
		self.ACCOUNTS = [
			['tilaveryunus@gmail.com', 'mirkanbaba123'],
		]
		self.DISCORD_GROUPS = [
			'https://discordapp.com/invite/35vucQS',
			'https://discordapp.com/invite/rcVXVab',
			'https://discordapp.com/invite/TXqGhed',
			'https://discordapp.com/invite/FMGAzwR',
		]
		self.MEMBER_LIB = []
		self.ACCOUNT_DIR = ''
			
	def prof_change(self, num):
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

		Thomas().driver.quit()
		new_profile = webdriver.FirefoxProfile(self.ACCOUNT_DIR)
		Thomas().driver = webdriver.Firefox(firefox_binary=Thomas().binary, firefox_profile=new_profile)
		sleep(1800)
		#Thomas().driver.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.spam_txt[random.randint(0, len(Spammer.spam_txt)) -1]))
		return

	def access_discord(self, ):
		Thomas().driver.get('http://discord.com/login')
		sleep(15)
		email_input = Thomas().driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input')
		email_input.send_keys(self.ACCOUNTS[self.ACCOUNT_COUNT][0])
		password_input = Thomas().driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input')
		password_input.send_keys(self.ACCOUNTS[self.ACCOUNT_COUNT][1])
		login_button = Thomas().driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/button[2]/div')
		login_button.click()
		Thomas().invitation_pass()

	def invitation_pass(self, ):
		sleep(15)
		Thomas().driver.get(self.DISCORD_GROUPS[self.DISCORD_GROUPS_COUNT])
		try:
			Thomas().driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/section/div/button').click()
			Thomas().driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/section/div/button').click()
		except:
			try:
				Thomas().driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
				Thomas().driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
			except:
				pass
			pass
		return Thomas().find_member_message()
		#import pdb; pdb.set_trace()
		#Thomas().driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# put in another file
	def getnada(self, ):
		Thomas().driver.get("https://getnada.com/")
		sleep(2)
		Thomas().driver.find_element_by_css_selector(".icon-plus").click()
		sleep(2)
		Thomas().driver.find_element_by_xpath("/html/body/div/div[1]/footer/a[2]").click()	
		sleep(2)
		address = Thomas().driver.find_element_by_css_selector(".address").text
		print(address.split("@")[1])
		# if address.split("@")[1] == "undefined":
		# 	return Thomas().getnada()
		return Thomas().create_account(address)

	def create_account(self, address):
		Thomas().driver.get('http://discord.com/register')
		sleep(5)
		email_input = Thomas().driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[1]/div/input')
		email_input.send_keys(address)
		username = Thomas().driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[2]/div/input')
		username.send_keys(Faker().user_name())
		password_input = Thomas().driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div/input')
		password_input.send_keys("supremePump123456789")
		login_button = Thomas().driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[4]/button')
		login_button.click()
		return#Thomas().invitation_pass()

	# def member_search(self, members):
	# 	for member in members:
	# 		print(member.text, member.text not in self.MEMBER_LIB)
	# 		if member.text not in MEMBER_LIB:
	# 			print(member.text)
	# 			self.MEMBER_LIB.append(member.text)
	# 			member.click()
	# 			Thomas().actions.send_keys("Do you know supremepumps? https://supremepumps.co")
	# 			Thomas().actions.perform()
	# 			sleep(0.25)
	# 			Thomas().actions.send_keys(Keys.ENTER)
	# 			Thomas().actions.perform()
	# 			sleep(random.randint(5, 25))
	# 			return Thomas().invitation_pass()
	# 		else:
	# 			pass
	# 			#print(member.text, "in MEMBER_LIB")

	def find_member_message(self, ):
		"""
			finds chat div, scrolls up, picks member and check if it sdid not send him any message yet, sends message
			Looks on chat area and sends people private messages
		"""
		sleep(15)
		try:
			Thomas().driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
		except:
			pass
		#import pdb; pdb.set_trace()
		scroll_div = Thomas().driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]')
		for i in range(500):
			if i%100 == 0:
				sleep(3)
			scroll_div.send_keys(Keys.PAGE_UP)
			
		members = Thomas().driver.find_elements_by_class_name('username-_4ZSMR')
		for member in members:
			if member.text not in MEMBER_LIB:
				print(member.text)
				self.MEMBER_LIB.append(member.text)
				member.click()
				sleep(1)
				Thomas().actions.perform()
				sleep(random.randint(1, 30))
				return Thomas().invitation_pass()
			else:
				#delete else after test
				print(member.text, "in MEMBER_LIB")

		#change discord-group
		print(self.MEMBER_LIB, "--NONE LEFT--")
		self.ACCOUNT_COUNT+=1
		self.DISCORD_GROUPS_COUNT+=1

	def event(self):
		while True:
			#Thomas().getnada()
			try:
				# Her sey bittikten sonra bunu calistir
				# bir hata oldugu zaman recaptha ya da ban mi diye baksin
				# degilse hatayi versin
				Thomas().getnada()
			except:
				print("except")
				mobile_verify_message = Thomas().driver.find_elements_by_class_name("body-3ROqbj")
				for message in mobile_verify_message:
					print(message.text)
					if message.text == "VERIFY BY PHONE" or message.text == "We've detected something out of the ordinary going on. To continue using Discord, we will need you to verify your account.":
						print("yes")
						self.ACCOUNT_COUNT+=1
						getsmscode.verify_by_phone(Thomas().driver)
						return Thomas().invitation_pass()
						# import pdb; pdb.set_trace()
						# # verify button
						# Thomas().driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div[4]/div").click()
						# Thomas().driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/input").send_keys("123") #send phone numberfrom get_china_num
						# Thomas().driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/div").click()
						# Thomas().actions.send_keys("86") #china
						# Thomas().actions.perform()
						# Thomas().prof_change(self.ACCOUNT_COUNT)
					else:
						print("no")
						Thomas().prof_change(self.ACCOUNT_COUNT)

Thomas().getnada()
#import pdb;pdb.set_trace()

# try:
# 	Thomas().actions.send_keys("Do you know supremepumps? https://supremepumps.co")
# 	Thomas().actions.send_keys(Keys.ENTER)
# 	access_discord()
# 	find_member_message()
# except:
# 	if Thomas().driver.current_url == "https://discordapp.com/activity":
# 		mail = browse.get_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div[4]/div[1]")
# 		mail.click()
# 		print(mail)
# 		# Maile gidecek oradan maili onaylayacak, ya da telefondan yapacak bu is 
	# mobile_verify_message = Thomas().driver.get_elemets_by_class_name("body-3ROqbj")
	# for message in mobile_verify_message:
	# 	if message.text == "We've detected something out of the ordinary going on. To continue using Discord,":
	# 		print("yes")
	# 		ACCOUNT_COUNT+=1
	# 		return prof_change(ACCOUNT_COUNT)
# 	try:
# 		access_discord()
# 		find_member_message()
# 	except:
# 		import pdb; pdb.set_trace()
# 	raise
