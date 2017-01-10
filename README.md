# TinderStalker
**tinderStalker.py** is a python script for stalking your friends on tinder, it's not a good idea but it's possible.


You have to insert your Facebook ID and Facebook Token in credz.json.

1. You can find your ID at this URL : http://findmyfbid.com/ or with this command : 
      
      curl http://findmyfbid.com/ --data "url=https://www.facebook.com/[your.name]" | grep -m 1 -Eoh '[0-9]{7,10}'

2. For your token you can use the Firebug extension and visit :

    https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&scope=user_birthday,user_photos,user_education_history,email,user_relationship_details,user_friends,user_work_history,user_likes&response_type=token%2Csigned_request&client_id=464891386855067

    After cliking "OK" you should have in the response the variable "access_token" and his value is the token. 

3. Launch the tool and profit
  $ python tinderStalker.py

Fappment,
