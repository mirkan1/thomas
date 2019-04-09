from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import inspect, os, random, getsmscode
from time import sleep
from faker import Faker
from mouseMove import moveNscroll # kullan scroll down yerine

# firefox lokasyionunu ver

binary = FirefoxBinary('C://Program Files//Mozilla Firefox//firefox.exe')
windows_profile = webdriver.FirefoxProfile('C://Users//Raq//AppData//Roaming//Mozilla//Firefox//Profiles//pw3c48y8.default') # Use your own file for, will make it autochoose
file_loc = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#lubuntu_prof = webdriver.FirefoxProfile(file_loc + "/profiles/banned_profiles/" + os.listdir(file_loc + "/profiles/banned_profiles")[0])

class Thomas():
	driver = webdriver.Firefox(firefox_profile=windows_profile, firefox_binary=binary)
	PROFILE_LOC = file_loc  + "/profiles/banned_profiles"
	#PROFILE_LOC = '//home//raq//Desktop//Others//hakan_is//new_profiles//'
	PROFILE_NUM = 0
	ACCOUNT_COUNT = 0
	DISCORD_GROUPS_COUNT = 0
	ACCOUNTS = [
		['tilaveryunus@gmail.com', 'mirkanbaba123'],
	]
	DISCORD_GROUPS = [
		'https://discordapp.com/channels/395316379353612288/402273167617556480', # megapump
	#	'https://discordapp.com/channels/393088095840370689/481193721560432670',
		'https://discordapp.com/invite/rcVXVab',
		'https://discordapp.com/invite/TXqGhed',
		'https://discordapp.com/invite/FMGAzwR',
	]
	MEMBER_LIB = []
	ACCOUNT_DIR = ''

	def prof_change(self, num):
		try:
			# banned_list = open("file_info.log", "r").read().split("\n")
			# if str(num) in banned_list:
			# 	return True

			print("New account is {}".format(os.listdir(Thomas.PROFILE_LOC)[num]))
			Thomas.ACCOUNT_DIR = '%s//%s' % (Thomas.PROFILE_LOC, os.listdir(Thomas.PROFILE_LOC)[num])
		except IndexError:
			PROFILE_NUM, num = 0, 0
			print("New account is {}".format(os.listdir(Thomas.PROFILE_LOC)[num]))
			Thomas.ACCOUNT_DIR = '%s//%s' % (Thomas.PROFILE_LOC, os.listdir(Thomas.PROFILE_LOC)[num])
		Thomas.driver.quit()
		new_profile = webdriver.FirefoxProfile(Thomas.ACCOUNT_DIR)
		new_driver = webdriver.Firefox(firefox_profile=new_profile, firefox_binary=binary)
		Thomas.driver = new_driver #driveri degistiriyor
		return Thomas().invitation_pass()

	def access_discord(self, ):
		Thomas.driver.get('http://discord.com/login')
		sleep(15)
		email_input = Thomas.driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input')
		email_input.send_keys(Thomas.ACCOUNTS[Thomas.ACCOUNT_COUNT][0])
		password_input = Thomas.driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input')
		password_input.send_keys(Thomas.ACCOUNTS[Thomas.ACCOUNT_COUNT][1])
		login_button = Thomas.driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/button[2]/div')
		login_button.click()
		Thomas().look_for_error()
		return Thomas().invitation_pass()

	def invitation_pass(self, ):
		print(Thomas.DISCORD_GROUPS[Thomas.DISCORD_GROUPS_COUNT])
		Thomas.driver.get(Thomas.DISCORD_GROUPS[Thomas.DISCORD_GROUPS_COUNT])
		sleep(15)
		try:
			Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/section/div/button').click()
			Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/section/div/button').click()
		except:
			try:
				Thomas.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
				Thomas.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
			except:
				Thomas().look_for_error()
			Thomas().look_for_error()
		return Thomas().find_member_message()
		#import pdb; pdb.set_trace()
		#Thomas.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# put in another file
	def getnada(self, ):
		Thomas.driver.get("https://getnada.com/")
		sleep(2)
		Thomas.driver.find_element_by_css_selector(".icon-plus").click()
		sleep(2)
		Thomas.driver.find_element_by_xpath("/html/body/div/div[1]/footer/a[2]").click()	
		sleep(2)
		address = Thomas.driver.find_element_by_css_selector(".address").text
		print(address.split("@")[1])
		# if address.split("@")[1] == "undefined":
		# 	return Thomas().getnada()
		return Thomas().create_account(address)

	def look_for_error(self,):
		# TODO
		# ADD MORE ERROR CODES
		#recaptha_class = ['rc-anchor', 'rc-anchor-normal', 'rc-anchor-dark']
		if len(Thomas.driver.find_elements('xpath', "//div[@class='body-3ROqbj']")) != 0:
			print("found verify")
			Thomas.ACCOUNT_COUNT += 1
			return Thomas().prof_change(Thomas.ACCOUNT_COUNT)
			#change account
		elif len(Thomas.driver.find_elements('xpath', "//div[@class='g-recaptcha']")) != 0:
			print("found reCaptha")
			Thomas.ACCOUNT_COUNT += 1
			return Thomas().prof_change(num=Thomas.ACCOUNT_COUNT)
		elif len(Thomas.driver.find_elements('xpath', "//input[@class='inputDefault-_djjkz input-cIJ7To size16-14cGz5']")) != 0:
			# Username koymadiysan bu error cikiyor
			print("username demands")
			myUsername = Faker().user_name()
			username = Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[1]/div/input')
			username.send_keys(myUsername)
			username_button = Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[2]/button')
			username_button.click()
			sleep(5)
			Thomas().look_for_error()
			#change account
			# profil degistir return Thomas().prof_change()

	def create_account(self, address):
		try:
			myUsername = Faker().user_name()
			Thomas.driver.get('http://discord.com/register')
			sleep(5)
			email_input = Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[1]/div/input')
			email_input.send_keys(address)
			username = Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[2]/div/input')
			username.send_keys(myUsername)
			password_input = Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div/input')
			password_input.send_keys("supremePump123456789")
			login_button = Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div/div[2]/div[4]/button')
			login_button.click()
			sleep(5)
			username = Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[1]/div/input')
			username.send_keys(myUsername)
			username_button = Thomas.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[2]/button')
			username_button.click()
		except:
			# Profil zaten acik ya da internet yoktur demek
			pass
		#input("createacount bekliyor")
		Thomas().look_for_error()
		return Thomas().invitation_pass()

	def find_member_message(self, ):
		# TODO
		# sometimes clicks somewhere it should not, make main window on top on that case (it might be fixed)
		# Add random messages on random times, more randomness
		# Change groups on random times

		"""
			finds chat div, scrolls up, picks member and check if it sdid not send him any message yet, sends message
			Looks on chat area and sends people private messages
		"""
		contentClass = "content-OzHfo4"
		ACTION = ActionChains(Thomas().driver)
		Thomas().look_for_error()
		try:
			Thomas.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/section/div/button").click()
		except:
			pass

		for j in range(random.randint(4,10)): moveNscroll(random.randint(-5000, -500)); sleep(random.randint(1,4+j))
		members = Thomas.driver.find_elements_by_class_name(contentClass)
		for member in members:
			if member.text not in Thomas.MEMBER_LIB:
				#print(member.text, Thomas.MEMBER_LIB)
				#Thomas.MEMBER_LIB.append(member.text)
				try:
					member.click()
					sleep(random.randint(3,7))
					ACTION.send_keys(Faker().user_name())#"Do you know supremepumps? https://supremepumps.co " + str([random.choice(['a','b','c','d']) for i in range(6)]))
					ACTION.send_keys(Keys.ENTER)
					ACTION.perform()
					ACTION.reset_actions()
					sleep(random.randint(5, 25))
					Thomas().look_for_error()
					Thomas.driver.maximize_window()
				except:
					Thomas.driver.maximize_window()
					pass
				return Thomas().invitation_pass()
			else:
				#delete else after test
				print(member.text, "in MEMBER_LIB")

		#change discord-group
		print(Thomas.MEMBER_LIB, "--NONE LEFT--")
		Thomas.ACCOUNT_COUNT+=1
		Thomas.DISCORD_GROUPS_COUNT+=1
		return Thomas().invitation_pass()

	def event(self):
		# TODO
		# I have no idea what is doing what here
		while True:
			#Thomas().getnada()
			try:
				# Her sey bittikten sonra bunu calistir
				# bir hata oldugu zaman recaptha ya da ban mi diye baksin
				# degilse hatayi versin
				Thomas().getnada()
			except:
				print("except")
				mobile_verify_message = Thomas.driver.find_elements_by_class_name("body-3ROqbj")
				for message in mobile_verify_message:
					print(message.text)
					if message.text == "VERIFY BY PHONE" or message.text == "We've detected something out of the ordinary going on. To continue using Discord, we will need you to verify your account.":
						print("yes")
						Thomas.ACCOUNT_COUNT+=1
						getsmscode.verify_by_phone(Thomas.driver)
						return Thomas().invitation_pass()
						# import pdb; pdb.set_trace()
						# # verify button
						# Thomas.driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div[4]/div").click()
						# Thomas.driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/input").send_keys("123") #send phone numberfrom get_china_num
						# Thomas.driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div[4]/div").click()
						# ACTION.send_keys("86") #china
						# ACTION.perform()
						# Thomas().prof_change(Thomas.ACCOUNT_COUNT)
					else:
						print("no")
						Thomas().prof_change(Thomas.ACCOUNT_COUNT)

if __name__ == "__main__":
	Thomas().getnada()
#Thomas().driver.get("https://discordapp.com/channels/393088095840370689/481193721560432670")

# Thomas.driver.execute_script("""var element = document.querySelector(".membersWrap-2h-GB4");if (element)  element.parentNode.removeChild(element);""")
