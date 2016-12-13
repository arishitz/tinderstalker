import requests
import json

def location(URL_Tinder_API, header) :

	# location :
	latitude = raw_input("\n [->] New latitude : ")
	longitude = raw_input(" [->] New longitude : ")

	location_data = {
		"lat": latitude,
		"lon": longitude
	}

	try :
		location_response = requests.post(URL_Tinder_API + "user/ping", data=location_data, headers=header)
		if location_response.status_code == 200 :
			print "\n [+] Location Updated !"
		else :
			print " [x] Fail..."
	except requests.exceptions.RequestException as e :
		print 'Error : ' + e
		sys.exit(1)


