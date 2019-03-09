from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import inspect, os, random
from time import sleep
import getsmscode
from faker import Faker

# firefox lokasyionunu ver

binary = FirefoxBinary('C://Program Files//Mozilla Firefox//firefox.exe')
#windows_profile = webdriver.FirefoxProfile('C://Users//MBG//AppData//Roaming//Mozilla//Firefox//Profiles//0ej4htv6.default')#random.randint(0, len(os.listdir(PROFILE_DIC))) -1])
file_loc = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
lubuntu_prof = webdriver.FirefoxProfile(file_loc + "/profiles/banned_profiles/" + os.listdir(file_loc + "/profiles/banned_profiles")[0])
driver = webdriver.Firefox(firefox_profile=lubuntu_prof)#, firefox_binary=binary)
#actions = ActionChains(driver) #divsiz yazmak icin

class Thomas():
	# driveri buraya koy
	def __init__(self, driver=driver):
		self.DRIVER = driver
		self.ACTION = ActionChains(self.DRIVER) #calisiyor mu emin ol
		self.PROFILE_DIC = file_loc  + "/profiles/banned_profiles"
		#self.PROFILE_DIC = '//home//raq//Desktop//Others//hakan_is//new_profiles//'
		self.PROFILE_NUM = 0
		self.ACCOUNT_COUNT = 0
		self.DISCORD_GROUPS_COUNT = 0
		self.ACCOUNTS = [
			['tilaveryunus@gmail.com', 'mirkanbaba123'],
		]
		self.DISCORD_GROUPS = [
			'https://discordapp.com/invite/rcVXVab',
			'https://discordapp.com/invite/TXqGhed',
			'https://discordapp.com/invite/FMGAzwR',
		]
		self.MEMBER_LIB = []
		self.ACCOUNT_DIR = ''
	
	@property
	def driver(self):
		return self.DRIVER

	@driver.setter
	def DRIVER(self, value):
		self.DRIVER = value

	def prof_change(self, num):
		try:
			# banned_list = open("file_info.log", "r").read().split("\n")
			# if str(num) in banned_list:
			# 	return True

			print("New account is {}".format(os.listdir(self.PROFILE_DIC)[num]))
			self.ACCOUNT_DIR = '%s//%s' % (self.PROFILE_DIC, os.listdir(self.PROFILE_DIC)[num])
		except IndexError:
			PROFILE_NUM, num = 0, 0
			print("New account is {}".format(os.listdir(self.PROFILE_DIC)[num]))
			self.ACCOUNT_DIR = '%s//%s' % (self.PROFILE_DIC, os.listdir(self.PROFILE_DIC)[num])
		print(self.DRIVER)
		self.DRIVER.quit()
		#print(self.ACCOUNT_DIR)
		new_profile = webdriver.FirefoxProfile(self.ACCOUNT_DIR)
		self.DRIVER = webdriver.Firefox(firefox_profile=new_profile)#firefox_binary=binary,
		print(self.DRIVER)
		self.DRIVER.get('http://www.facebook.com')
		sleep(15)
		self.DRIVER.get("https://web.telegram.org/")
		return Thomas().mk()
		return Thomas().invitation_pass()

	def mk(self):
		print(self.DRIVER)
		self.DRIVER.get('http://www.google.com')

	def access_discord(self, ):
		self.DRIVER.get('http://discord.com/login')
		sleep(15)
		email_input = self.DRIVER.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input')
		email_input.send_keys(self.ACCOUNTS[self.ACCOUNT_COUNT][0])
		password_input = self.DRIVER.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input')
		password_input.send_keys(self.ACCOUNTS[self.ACCOUNT_COUNT][1])
		login_button = self.DRIVER.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/button[2]/div')
		login_button.click()
		Thomas().look_for_error()
		return Thomas().invitation_pass()

	def invitation_pass(self, ):
		print(self.DISCORD_GROUPS[self.DISCORD_GROUPS_COUNT])
		self.DRIVER.get(self.DISCORD_GROUPS[self.DISCORD_GROUPS_COUNT])
		sleep(15)
		try:
			self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/section/div/button').click()
			self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div/div/section/div/button').click()
		except:
			try:
				self.DRIVER.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
				self.DRIVER.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
			except:
				Thomas().look_for_error()
			Thomas().look_for_error()
		return Thomas().find_member_message()
		#import pdb; pdb.set_trace()
		#self.DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# put in another file
	def getnada(self, ):
		self.DRIVER.get("https://getnada.com/")
		sleep(2)
		self.DRIVER.find_element_by_css_selector(".icon-plus").click()
		sleep(2)
		self.DRIVER.find_element_by_xpath("/html/body/div/div[1]/footer/a[2]").click()	
		sleep(2)
		address = self.DRIVER.find_element_by_css_selector(".address").text
		print(address.split("@")[1])
		# if address.split("@")[1] == "undefined":
		# 	return Thomas().getnada()
		return Thomas().create_account(address)

	def look_for_error(self,):
		#recaptha_class = ['rc-anchor', 'rc-anchor-normal', 'rc-anchor-dark']
		if len(self.DRIVER.find_elements('xpath', "//div[@class='body-3ROqbj']")) != 0:
			print("found verify")
			self.ACCOUNT_COUNT += 1
			return Thomas().prof_change(self.ACCOUNT_COUNT)
			#change account
		elif len(self.DRIVER.find_elements('xpath', "//div[@class='g-recaptcha']")) != 0:
			print("found reCaptha")
			self.ACCOUNT_COUNT += 1
			return Thomas().prof_change(num=self.ACCOUNT_COUNT)
			#change account
			# profil degistir return Thomas().prof_change()

	def create_account(self, address):
		try:
			myUsername = Faker().user_name()
			self.DRIVER.get('http://discord.com/register')
			sleep(5)
			email_input = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[1]/div/input')
			email_input.send_keys(address)
			username = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[2]/div/input')
			username.send_keys(myUsername)
			password_input = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div/input')
			password_input.send_keys("supremePump123456789")
			login_button = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[4]/button')
			login_button.click()
			sleep(5)
			username = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[1]/div/input')
			username.send_keys(myUsername)
			username_button = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[2]/button')
			username_button.click()
		except:
			# Profil zaten acik ya da internet yoktur demek
			pass
		Thomas().look_for_error()
		return Thomas().invitation_pass()

	# def member_search(self, members):
	# 	for member in members:
	# 		print(member.text, member.text not in self.MEMBER_LIB)
	# 		if member.text not in MEMBER_LIB:
	# 			print(member.text)
	# 			self.MEMBER_LIB.append(member.text)
	# 			member.click()
	# 			self.ACTION.send_keys("Do you know supremepumps? https://supremepumps.co")
	# 			self.ACTION.perform()
	# 			sleep(0.25)
	# 			self.ACTION.send_keys(Keys.ENTER)
	# 			self.ACTION.perform()
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
			self.DRIVER.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
		except:
			pass
		#import pdb; pdb.set_trace()
		scroll_div = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]')
		for i in range(500):
			if i%100 == 0:
				sleep(3)
			scroll_div.send_keys(Keys.PAGE_UP)
			
		members = self.DRIVER.find_elements_by_class_name('username-_4ZSMR')
		for member in members:
			if member.text not in self.MEMBER_LIB:
				print(member.text, self.MEMBER_LIB)
				self.MEMBER_LIB.append(member.text)
				member.click()
				self.ACTION.send_keys("Do you know supremepumps? https://supremepumps.co")
				self.ACTION.perform()
				sleep(0.25)
				self.ACTION.send_keys(Keys.ENTER)
				self.ACTION.perform()
				sleep(random.randint(5, 25))
				return Thomas().invitation_pass()
			else:
				#delete else after test
				print(member.text, "in MEMBER_LIB")

		#change discord-group
		print(self.MEMBER_LIB, "--NONE LEFT--")
		self.ACCOUNT_COUNT+=1
		self.DISCORD_GROUPS_COUNT+=1
		return Thomas().invitation_pass()

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
				mobile_verify_message = self.DRIVER.find_elements_by_class_name("body-3ROqbj")
				for message in mobile_verify_message:
					print(message.text)
					if message.text == "VERIFY BY PHONE" or message.text == "We've detected something out of the ordinary going on. To continue using Discord, we will need you to verify your account.":
						print("yes")
						self.ACCOUNT_COUNT+=1
						getsmscode.verify_by_phone(self.DRIVER)
						return Thomas().invitation_pass()
						# import pdb; pdb.set_trace()
						# # verify button
						# self.DRIVER.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div[4]/div").click()
						# self.DRIVER.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/input").send_keys("123") #send phone numberfrom get_china_num
						# self.DRIVER.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/div").click()
						# self.ACTION.send_keys("86") #china
						# self.ACTION.perform()
						# Thomas().prof_change(self.ACCOUNT_COUNT)
					else:
						print("no")
						Thomas().prof_change(self.ACCOUNT_COUNT)


Thomas().getnada()
	#import pdb;pdb.set_trace()
#import pdb;pdb.set_trace()

# try:
# 	self.ACTION.send_keys("Do you know supremepumps? https://supremepumps.co")
# 	self.ACTION.send_keys(Keys.ENTER)
# 	access_discord()
# 	find_member_message()
# except:
# 	if self.DRIVER.current_url == "https://discordapp.com/activity":
# 		mail = browse.get_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div[4]/div[1]")
# 		mail.click()
# 		print(mail)
# 		# Maile gidecek oradan maili onaylayacak, ya da telefondan yapacak bu is 
	# mobile_verify_message = self.DRIVER.get_elemets_by_class_name("body-3ROqbj")
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
