import requests


# Authentication
def auth(URL_Tinder_API, auth_credz) : 
	print " [+] Trying to authenticate you..."
	try :
		connexion_response = requests.post(URL_Tinder_API + "auth", data=auth_credz)
		if  connexion_response.status_code ==  200 :
			#print connexion_response.json()["token"]
			print " [+] Good Authentication"
			return connexion_response.json()["token"]
		else :
			print " [x] Authentication faillure, bad facebook id or bad facebook token"
	except requests.exceptions.RequestException as e :
		print 'Error : ' + e
		sys.exit(1)



