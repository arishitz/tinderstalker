import requests
import json

def friends(URL_Tinder_API, header) :

	# Requesting facebook friends informations
	print " [+] Trying to request informations of facebook friends..."
	try :
		request_response = requests.get(URL_Tinder_API + "group/friends", headers=header)
		if request_response.status_code == 200 :
			print " [+] Good request of Friends datas"
			data_response = request_response.json()
			data_response_indent = json.dumps(data_response, indent=4)
			save_result = open('result.json', 'w')
			save_result.write(str(data_response_indent))
			save_result.close()
		else :
			print " [x] Fail..."
	except requests.exceptions.RequestException as e :
		print 'Error : ' + e
		sys.exit(1)

	# Print facebook friends name who are on Tinder
	print " [+] List of your " + str(len(data_response["results"])) + " facebook friends who are on tinder :\n"

	friends_list = []
	for friend in data_response["results"] :
		name = friend["name"]
		tinder_id = friend["user_id"]
		friends_list.append("    - " + name + " , id : " + tinder_id)

	friends_list = sorted(friends_list)
	i = 0
	while i < len(friends_list) :
		print friends_list[i]
		i += 1

