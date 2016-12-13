import requests
import json

def updates(URL_Tinder_API, header) :

        # Updates :
        try :
                updates_response = requests.post(URL_Tinder_API + "updates", headers=header)
                if updates_response.status_code == 200 :
                        print "\n [+] Got updates !"
                else :
                        print " [x] Fail..."
        except requests.exceptions.RequestException as e :
                print 'Error : ' + e
                sys.exit(1)


        # Print updates information
        updates_data = updates_response.json()
        print json.dumps(updates_data, indent=4)

