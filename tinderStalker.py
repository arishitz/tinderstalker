#!/usr/bin/python
# -*-coding:Utf-8 -*"


import requests
import json
import sys

print ""
print "  _______ \           _              _____ _        _ _             "
print " |__   __/_\         | |            / ____| |      | | |            "
print "    | |   _ _ __   __| | ___ _ __  | (___ | |_ __ _| | | _____ _ __ "
print "    | |  | | '_ \ / _` |/ _ \ '__|  \___ \| __/ _` | | |/ / _ \ '__|"
print "    | |  | | | | | (_| |  __/ |     ____) | || (_| | |   <  __/ |   "
print "    |_|  |_|_| |_|\__,_|\___|_|    |_____/ \__\__,_|_|_|\_\___|_|   "
print "                                                                    by ari_\n"


URLTinderAPI = "https://api.gotinder.com/"

facebook_id = ""
facebook_token = ""

if facebook_id == "" or facebook_token == "" :
	facebook_id = raw_input("Facebook ID : ")
	facebook_token = raw_input("facebook token : ")


header = {
	"platform" : "android",
#	"User-Agent" : "Tinder Android Version 5.3.3",
        "User-Agent" : "Tinder Android Version 5.2.0",
	"os-version" : "23",
#        "app-version" : "1623",
	"app-version" : "1546",
#	"Content-Type" : "application/json; charset=utf-8",
	"host" : "api.gotinder.com",
	"Connection" : "Keep-Alive",
	"Accept-Language": "en",
	"If-None-Match": 'W/"1630244057"'
}

auth_data = {
        "facebook_id": facebook_id,
        "facebook_token": facebook_token
}


# Authentication
print "[+] Trying to authenticate you..."
try :
	connexion_response = requests.post(URLTinderAPI + "auth", data=auth_data)
	if  connexion_response.status_code ==  200 :
		#print connexion_response.json()
		#print connexion_response.json()["token"]
		header["X-Auth-Token"] = connexion_response.json()["token"]
		print "[+] Good Authentication"
	else :
		print "[o] Authentication faillure, bad id or bad token"
except requests.exceptions.RequestException as e :
	print 'Error : ' + e
	sys.exit(1)


# Requesting facebook friends informations
print "[+] Trying to request informations of facebook friends..."
try :
	request_response = requests.get(URLTinderAPI + "group/friends", headers=header)
	if request_response.status_code == 200 :
		print "[+] Good request of Friends datas" 
	else :
		print "[o] Fail..."
except requests.exceptions.RequestException as e :
	print 'Error : ' + e
	sys.exit(1)


# Print facebook friends name who are on Tinder
data_response = request_response.json()
print "[+] List of your " + str(len(data_response["results"])) + " facebook friends who are on tinder :\n"

friends_list = []
for friend in data_response["results"] :
	name = friend["name"]
	tinder_id = friend["user_id"]
	friends_list.append(" - " + name + " , id : " + tinder_id)

friends_list = sorted(friends_list)
i = 0
while i < len(friends_list) :
	print friends_list[i]
	i += 1

# Profile Tinder Request
print "\n[+] We can now request more informations of Friends"

stalk = True
while stalk is True : 
	friend_id = raw_input("\n[->] Enter id of one friends : ")
	if friend_id == "q" :
		sys.exit(1)

	try :
		friend_response = requests.get(URLTinderAPI + "user/" + friend_id, headers=header)
		if friend_response.status_code == 200 :
			print "\n[+] Friend's information recuperation"
		else :
			print "Fail..."
	except requests.exceptions.RequestException as e :
		print 'Error : ' + e
		sys.exit(1)


	# Print friend's information
	friend_data = friend_response.json()["results"]

# For debug
	#print friend_data
	#print json.dumps(friend_data, indent=4)

# Informations Extraction 

	# Firstname
	name = friend_data["name"]

	# Tinder ID
	id = friend_data["_id"]

	# Friend's last connexion 
	last_online = str(friend_data["ping_time"])
	last_online = last_online.split("T", 1) # + " " + last_online.split("T", 2)
	date = last_online[0]
	hour = last_online[1].split(".", 1)
	hour = hour[0]

	# Friend's gender
	gender = friend_data["gender"]
	if gender == 1 :
		gender = "woman"
	else :
		gender = "man"

	# Friend's birthdate
	birth_date = friend_data["birth_date"]
	birth_date = birth_date.split("T", 1)
	birth_date = birth_date[0]

	# Friend's distance from you
	distance = friend_data["distance_mi"]

	# Friend's biography
	bio = friend_data["bio"]

	# Friend's school
	try :
		school = friend_data["schools"][0]["name"]
	except :
		school = ""

	# Friend's job
	try :
		job = friend_data["jobs"][0]["title"]["name"]
	except :
		job = ""

	# Friend's company
	try : 
		company = friend_data["jobs"][0]["company"]["name"]
	except :
		company = ""

	# Friend's instagram account
	try :
		instagram = friend_data["instagram"]["username"]
	except :
		instagram = ""
	common_friends = str(friend_data["common_friends"])
	common_likes = friend_data["common_likes"]

	# Common interests with your friend
	common_interests = ""
	i = 0
	while i < len(friend_data["common_interests"]) :
		common_interests += friend_data["common_interests"][i]["name"] + ", "
		i += 1

	# Common connection with your friend
	common_connections = ""
	i = 0
	while i < len(friend_data["common_connections"]) :
		common_connections += friend_data["common_connections"][i]["name"] + ", "
		i += 1 

	# Friend's number of connection
	connection_count = str(friend_data["connection_count"])

	# ?
#	? = friend_data["?"]


# Information Printer

	print "\n - name : " + name
	print " - id : " + str(id)
	print " - Last online : " + str(date) + " at " + str(hour)
	print " - Gender : " + gender
	print " - Birthday : " + birth_date
	print " - Distance : " + str(distance) + " miles"
	print " - Bio : " + bio
	print " - Instagram : " + instagram
	print " - School : " + school
	print " - Job : " + job + " at " + company
	print " - Common friends : " + common_friends
	print " - Common likes : " + str(common_likes)
	print " - Common interests : " + common_interests
	#print " - Common connections : " + common_connections
	print " - connection count : " + connection_count
#	print " - ? : " + ?



	







