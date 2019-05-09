from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search, match
from selenium.webdriver.common.action_chains import ActionChains
import random, requests, sys, os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import inspect, random
from os import listdir
from threading import Thread
from faker import Faker

info = {
	'login': 'http://www.getsmscode.com/do.php?action=login&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70',
	'getmobile': 'http://www.getsmscode.com/do.php?action=getmobile&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70&pid=10',
	'getsms': 'http://www.getsmscode.com/do.php?action=getsms&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70&pid=10&mobile=%s&author=seleniumcrypt@gmail.com',
	'addblack': 'http://www.getsmscode.com/do.php?action=addblack&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70&pid=10&mobile=%s',
	'mobilelist': 'http://www.getsmscode.com/do.php?action=mobilelist&username=seleniumcrypt@gmail.com&token=8cdfe60f332b6496073d1a2c97a6ae70'
	}

binary = FirefoxBinary('C://Program Files//Mozilla Firefox//firefox.exe')
windows_profile = webdriver.FirefoxProfile('C://Users//Raq//AppData//Roaming//Mozilla//Firefox//Profiles//pw3c48y8.default') # Use your own file for, will make it autochoose
file_loc = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#lubuntu_prof = webdriver.FirefoxProfile(file_loc + "/profiles/banned_profiles/" + os.listdir(file_loc + "/profiles/banned_profiles")[0])

class AccountCreator:
    DRIVER = webdriver.Firefox(firefox_binary=binary)#firefox_profile=windows_profile, firefox_binary=binary)
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

    def getNada(self, ):
        self.DRIVER.maximize_window()
        self.DRIVER.get("https://getnada.com/")
        sleep(2)
        self.DRIVER.find_element_by_css_selector(".icon-plus").click()
        sleep(2)
        self.DRIVER.find_element_by_xpath("/html/body/div/div[1]/footer/a[2]").click()	
        sleep(2)
        address = self.DRIVER.find_element_by_css_selector(".address").text
        if address.split("@")[1] == "undefined":
            return self.getNada()
        return self.create_account(address)
        
    def create_account(self, address):
        #try:
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
        try:
            username = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[1]/div/input')
            username.send_keys(myUsername)
            username_button = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[2]/button')
            username_button.click()
        except:
            pass

        answer = None
        def check():
            # CALISIYOR MU SONRADAN CHECK ET
            # hic bir print olmamamsi lazim galiba
            sleep(10) # 5 dakika yap
            if answer != None:
                return self.doc_replacer()
                self.DRIVER.quit()
                return self.getNada()
            self.DRIVER.quit()
            self.DRIVER = webdriver.Firefox(firefox_binary=binary)
            return self.getNada()
        Thread(target = check).start()
        answer = input("Click any button if you passed Recaptha")
        #TODO
        #save your temp file to location of desired
        #works
        return
        #self.look_for_error()
        #except:
        #    # Profil zaten acik ya da internet yoktur demek
        #    pass

    def doc_replacer(self, ):
        new_location = "C://Users//Raq//Desktop//Others//thomas-the-discord-bot//profiles//new_profiles"#C://Users//Raq//Desktop//Others//hakan_picinin_isi//spam_bot2//new_profiles"
        temp = "C://Users//Raq//AppData//Local//Temp"

        for i in os.listdir(temp):
            if i.startswith("tmp"):
                if os.path.isdir(temp + "//" + i):
                    for j in os.listdir(temp + "//" + i + "//webdriver-py-profilecopy//"):
                        #import pdb;pdb.set_trace()
                        if j.startswith("webappsstore"):
                            # TODO
                            # pick a good location for profiles
                            os.mkdir(new_location + "//" + str(len(os.listdir(new_location)) + 1))
                            self.DRIVER.quit()
                            self.DRIVER = webdriver.Firefox(firefox_binary=binary)
                            sleep(5)
                            os.rename(temp + "//" + i + "//webdriver-py-profilecopy//" + j, new_location + "//" + str(len(os.listdir(new_location))) + "//" + j)
                            os.rmdir(temp + "//" + i)
                        else:
                            pass
            elif i.startswith("rust"):
                if os.path.isdir(temp + "//" + i):
                    for j in os.listdir(temp + "//" + i):
                        #import pdb;pdb.set_trace()
                        if j.startswith("webappsstore"):
                            # TODO
                            # pick a good location for profiles
                            os.mkdir(new_location + "//" + str(len(os.listdir(new_location)) + 1))
                            self.DRIVER.quit()
                            self.DRIVER = webdriver.Firefox(firefox_binary=binary)
                            sleep(5)
                            os.rename(temp + "//" + i + "//" + j, new_location + "//" + str(len(os.listdir(new_location))) + "//" + j)
                            os.rmdir(temp + "//" + i)
                        else:
                            pass

    def look_for_error(self,):
        # TODO
        # ADD MORE ERROR CODES
        # recaptha_class = ['rc-anchor', 'rc-anchor-normal', 'rc-anchor-dark']
        if len(self.DRIVER.find_elements('xpath', "//div[@class='body-3ROqbj']")) != 0:
            print("found verify")
            self.ACCOUNT_COUNT += 1
            # TODO 
            # verify function
            answer = None
            def check():
                sleep(10)
                if answer != None:
                    print(None)
                    pass
                return True#self.getNada(self)
            Thread(target = check).start()
            answer = input("Click any button if you passed Recaptha")
            # save the file
            
            # self.verify_with_phone()
            #return self.prof_change(self.ACCOUNT_COUNT)
        elif len(self.DRIVER.find_elements('xpath', "//div[@class='g-recaptcha']")) != 0:
            print("found reCaptha")
            self.ACCOUNT_COUNT += 1
            return True#self.prof_change(num=self.ACCOUNT_COUNT)
        elif len(self.DRIVER.find_elements('xpath', "//input[@class='inputDefault-_djjkz input-cIJ7To size16-14cGz5']")) != 0:
            # Username koymadiysan bu error cikiyor
            print("username demands")
            myUsername = Faker().user_name()
            username = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[1]/div/input')
            username.send_keys(myUsername)
            username_button = self.DRIVER.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[5]/div[2]/button')
            username_button.click()
            sleep(5)
            self.look_for_error()
            #change account
            # profil degistir return self.prof_change()
            
    def get_key(self, sms):#, DRIVER):
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
                #import pdb; pdb.set_trace()
                # give DRIVER here to DRIVER
                #DRIVER.quit()
                print("%s is blacklisted" % (sms))
                requests.get(info['addblack'] % (sms))
                return get_key(str(requests.get(info['getmobile']).text))
            count += 1
            sleep(11)
        return

    def verify_by_phone(self, ):
        """Waits for code to appear via API. If the code is not recieved restarts whole program"""
        sms = requests.get(info['getmobile']).text
        print(sms)
        count = 0
        while True:
            reply = requests.get(info['getsms'] % (sms)).text
            print(count, reply)
            if reply[-5:].isdigit():
                reply = reply[-5:]
                break
            import pdb; pdb.set_trace()
            # if reply != 'Message|not receive':
            # elif reply == "Message|mobile number not found!":
            if count > 15:
                # give DRIVER here to DRIVER
                #DRIVER.quit()
                print("%s is blacklisted" % (sms))
                requests.get(info['addblack'] % (sms))
                return get_key(str(requests.get(info['getmobile']).text))
            count += 1
            sleep(11)
        return

    def replace_file(self, ):
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
""" 
    def look_for_error(self, DRIVER, sms, **kwargs):
        sleep(10)
        for error_might_be in DRIVER.find_elements_by_xpath("//h4[@class]"):
                if error_might_be.get_attribute("class") == "md_simple_header":
                    # try:
                        DRIVER.find_element_by_xpath("//a[@class='error_modal_details_link']").click()
                        sleep(2)
                        whole_message = DRIVER.find_element_by_css_selector(".error_modal_details").text#"/html/body/div[5]/div[2]/div/div/div[1]/div[2]/textarea").text   .error_modal_details
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
                            DRIVER.quit()
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
        return get_key(DRIVER, sms)
 """

    # create_account(str(requests.get(info['getmobile']).text))




 
    #num = requests.get(info['getmobile']).text
    ##print(num)
#
    #def run(num):
    #    print(requests.get(info['login']).text, num[3:])
    #    while True:
    #        try:
    #            sms = requests.get(info['getsms'] % (num)).text
    #            print(sms)
    #            if sms != 'Message|not receive':
    #                print("yap bakam bi, sonra duzeltirsin")
    #            sleep(10)
    #        except:
    #            print("banned")
    #            requests.get(info['addblack'] % (num)).text
    #            return run(requests.get(info['getmobile']).text) 

    #print(requests.get(info['getmobile']).text)
    #run(requests.get(info['getmobile']).text)

if __name__ == "__main__":
	AccountCreator().getNada()