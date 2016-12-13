import requests
import json

def message(URL_Tinder_API, my_id, header) :

	# Send message to a profile :
	profile_id = raw_input("\n [->] Enter id of a match to send a message : ")
	match_id = my_id + profile_id
	match_id_2 = my_id + profile_id
	match_id_1 = profile_id + my_id

	message_text = raw_input("\n [->] Message : ")
	try :
		message_response = requests.post(URL_Tinder_API + "user/matches/" + match_id_1, data = {'message': message_text}, headers=header)
		if message_response.status_code == 200 :
			print "\n [+] Message sent !"
		elif message_response.status_code == 500 :
			try :
				message_response = requests.post(URL_Tinder_API + "user/matches/" + match_id_2, data = {'message': message_text}, headers=header)
				if message_response.status_code == 200 :
					print "\n [+] Message sent !"
				else :
		                        print " [x] Fail..."
        		except requests.exceptions.RequestException as e :
                		print 'Error : ' + e
                		sys.exit(1)

		else :
			print " [x] Fail..."
	except requests.exceptions.RequestException as e :
		print 'Error : ' + e
		sys.exit(1)


	# Print message's information
        message_data = message_response.json()
        print json.dumps(message_data, indent=4)
