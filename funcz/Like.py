import requests
import json

def like(URL_Tinder_API, header) :

	# Like a profile :
	like_id = raw_input("\n [->] Enter id of a profile to like : ")

        try :
                like_response = requests.get(URL_Tinder_API + "like/" + like_id, headers=header)
                if like_response.status_code == 200 :
                        print "\n [+] Profile liked !"
                else :
                        print " [x] Fail..."
        except requests.exceptions.RequestException as e :
                print 'Error : ' + e
                sys.exit(1)


	# Print like information
	like_data = like_response.json()
	print json.dumps(like_data, indent=4)


def likes(URL_Tinder_API, header) :

	# Like all recommandations :
	try :
		reco_response = requests.post(URL_Tinder_API + "recs", headers=header)
		if reco_response.status_code == 200 :
			print "\n [+] Got recommandations !\n"
		else :
			print " [x] Fail..."
	except requests.exceptions.RequestException as e :
		print 'Error : ' + e
		sys.exit(1)


	# Print updates information
	#reco_data = reco_response.json()
	reco_data = reco_response.json()
	#print json.dumps(reco_data, indent=4)

	i = 0
	j = 0
	while i < len(reco_data["results"]) :
		profile_id = reco_data["results"][i]["user"]["_id"]
                #print "id : " + profile_id
                #print json.dumps(profile_id, indent=4)
		try :
			like_response = requests.get(URL_Tinder_API + "like/" + profile_id, headers=header)
			if like_response.status_code == 200 :
				print "  [x] Profile id " + profile_id + " of " + reco_data["results"][i]["user"]["name"] + " liked !"
				j += 1
			else :
				print " [x] Fail..."
		except requests.exceptions.RequestException as e :
			print 'Error : ' + e
		
		#raw_input()
		i += 1


	print "\n [+] " + str(j) + " recommandations liked"
