import requests
import json

def report(URL_Tinder_API, my_id, header) :

	# report a profile :
	report_id = raw_input("\n [->] Enter id of a profile to report : ")
	match_id_1 = my_id + report_id
	match_id_2 = report_id + my_id
	try :
		report_response = requests.get(URL_Tinder_API + "report/" + match_id_1, headers=header)
		if report_response.status_code == 200 :
			print "\n [+] Profile reported !"
		elif report_response.status_code == 500 :
			try :
				report_response = requests.get(URL_Tinder_API + "report/" + match_id_2, headers=header)
				if report_response.status_code == 200 :
					print "\n [+] Profile reported !"
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


	# Print report informations
	report_data = report_response.json()
	print json.dumps(report_data, indent=4)
