import requests
import json

def stalker(URL_Tinder_API, header) :

	# Profile Tinder Request
	friend_id = raw_input("\n [->] Enter id of the Tinder Profile : ")

	try :
		friend_response = requests.get(URL_Tinder_API + "user/" + friend_id, headers=header)
		if friend_response.status_code == 200 :
			print "\n [+] Profile's information recuperation"
		else :
			print " [x] Fail..."
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
	try :
		bio = friend_data["bio"]
	except :
		bio = ""

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

	# Number of common friends
	try :
		common_friend_count = str(friend_data["common_friend_count"])
	except :
		common_friend_count = ""

	# Number of common likes
	try :
		common_likes = friend_data["common_likes"]
	except :
		common_likes = ""

	# Common interest count
	try :
		common_interest_count = friend_data["common_interest_count"]
	except :
		common_interest_count = ""

	# Common interests with your friend
	common_interests = ""
	i = 0
	try :
		while i < len(friend_data["common_interests"]) :
			common_interests += friend_data["common_interests"][i]["name"] + ", "
			i += 1
	except :
		common_interests = ""

	# Common connection with your friend
	common_connections = ""
	i = 0
	try :
		while i < len(friend_data["common_connections"]) :
			common_connections += friend_data["common_connections"][i]["name"] + ", "
			i += 1
	except :
		common_connections = ""

	# Friend's number of connection	
	connection_count = str(friend_data["connection_count"])


	# Information Printer

	print "\n - name : " + name
	print " - id : " + str(id)
	print " - Last online : " + str(date) + " at " + str(hour) + " GMT"
	print " - Gender : " + gender
	print " - Birthday : " + birth_date
	print " - Distance : " + str(distance) + " miles / " + str(round(distance*1.60934,1)) + " km"
	print " - Bio : " + bio
	print " - Instagram : " + instagram
	print " - School : " + school
	print " - Job : " + job + " at " + company
	print " - Common friend count : " + common_friend_count
	print " - Common likes : " + str(common_likes)
	print " - Common interest count : " + str(common_interest_count)
	print " - Common interests : " + str(common_interests)
	#print " - Common connections : " + common_connections
	print " - connection count : " + connection_count

