#!/usr/bin/python
# -*-coding:Utf-8 -*"

import requests
import json
import sys
#sys.path.append('funcz')
from funcz import Auth
from funcz import Friends
from funcz import Stalker
from funcz import Like
from funcz import Message
from funcz import Location
from funcz import Updates
from funcz import Report

def main() :

	print ""
	print "  _______ \           _              _____ _        _ _             "
	print " |__   __/_\         | |            / ____| |      | | |            "
	print "    | |   _ _ __   __| | ___ _ __  | (___ | |_ __ _| | | _____ _ __ "
	print "    | |  | | '_ \ / _` |/ _ \ '__|  \___ \| __/ _` | | |/ / _ \ '__|"
	print "    | |  | | | | | (_| |  __/ |     ____) | || (_| | |   <  __/ |   "
	print "    |_|  |_|_| |_|\__,_|\___|_|    |_____/ \__\__,_|_|_|\_\___|_|   "
	print "                                                                    by ari_\n"


	URL_Tinder_API = "https://api.gotinder.com/"

	# header for talk with the server
	header = {
		"User-Agent": "Tinder Android Version 5.2.0",
		"Accept-Language": "en",
		"host": "api.gotinder.com",
		"Conection": "Keep-Alive",
		"app-version": "1546",
		"os-version": "23",
		"platforms": "android"
	}


	with open('credz.json') as credz :
		auth_credz = json.load(credz)
	header["X-Auth-Token"] = Auth.auth(URL_Tinder_API, auth_credz)

	# My profile id recuperation	
	try :
		my_profile = requests.post(URL_Tinder_API + "profile", headers=header)
		if my_profile.status_code == 200 :
			my_id = my_profile.json()["_id"]
			print " [+] My Tinder profile id is : " + my_id
		else :
			print "\n [x] Fail... make sure to have correclty entered the Facebook ID and Facebook Token in credz.json file\n"
			exit(1)
	except requests.exceptions.RequestException as e :
		print 'Error : ' + e

	# Menu loop
	stalk = True
	while stalk == True :
		print "\n#############################################################################\n"
		print " TinderStalker Menu : \n"
		print " [0] List Facebook friends on tinder"
		print " [1] Stalk a Tinder profile"
		print " [2] Like a Tinder profile or all new recommendations"
		print " [3] Send message to a Tinder profile (match required)"
		print " [4] Update location"
		print " [5] Get Updates"
		print " [6] Report a Tinder Profile"
		print " [q] Quit"
		print "\n#############################################################################\n"

		choice = raw_input(" [->] Choice : ")	


		if choice == "0" :
			Friends.friends(URL_Tinder_API, header)

		elif choice == "1" :
			Stalker.stalker(URL_Tinder_API, header)

		elif choice == "2" :
			print "\n [0] Like one profile"
			print " [1] Like all recommendations\n"
			like_choice = raw_input( " [->] Choice : ")
			if like_choice == "0" :
				Like.like(URL_Tinder_API, header)
			elif like_choice == "1" :
				Like.likes(URL_Tinder_API, header)
			else :
				print "\n [x] Bad choice."

		elif choice == "3" :
			Message.message(URL_Tinder_API, header)

		elif choice == "4" :
			Location.location(URL_Tinder_API, header)

		elif choice == "5" :
			Updates.updates(URL_Tinder_API, header)

		elif choice == "6" :
			Report.report(URL_Tinder_API, header)

		elif choice == "q" or choice == "Q":
			stalk = False
			print "\n [<-] Goodbye Stalker.\n"
			sys.exit(1)

		else :
			print "\n [x] Bad choice."


		print "\n [+] Continue."
		raw_input()




if __name__ == '__main__' :
	try :
		main()
	except Exception, e :
		print "\Error : " + str(e)
		raw_input()
        except KeyboardInterrupt:
                print('\nHard Quit')



		

