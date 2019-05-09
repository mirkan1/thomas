import os, time, re

# profile = webdriver.FirefoxProfile(profile_dic + '//%s//' % listdir(profile_dic)[random.randint(0, len(listdir(profile_dic))) -1])

# # lists a dir
# os.listdir("C://Users//Raq//AppData//Local//Temp")

# #makes directory
# os.mkdir("C://Users//Raq//Desktop//test_dir")

# #removes dic
# os.rmdir("C://Users//Raq//Desktop//test_dir")

# #deletes and replace new file also moves files
# os.rename("C://Users//Raq//Desktop//test_dir", "C://Users//Raq//Desktop//test_dir2")

def doc_replacer():
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
                        os.rename(temp + "//" + i + "//webdriver-py-profilecopy//" + j, new_location + "//" + str(len(os.listdir(new_location))) + "//" + j)
                        #os.rmdir(temp + "//" + i)
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
                        os.rename(temp + "//" + i + "//" + j, new_location + "//" + str(len(os.listdir(new_location))) + "//" + j)
                        #os.rmdir(temp + "//" + i)
                    else:
                        pass
#doc_replacer()