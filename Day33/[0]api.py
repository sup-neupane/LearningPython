#An API is a set of commands, functions, protocols and objects that programmers can use to 
# create software or interact with an external system

#API is like cashier at bank to whom you can make many requests

#API endpoint is like location.
#Say if you want money out of bank you need to know where the bank is.
#Similarly if you want data from a website you should know its endpoint which is basically url

#API Request:
#For some requests like taking out money we must have some authentication to present to cashier
#But for some requests like what is your opening hours you dont need any authentication

#One example of such API is international Space Station API
#The endpoint is http://api.open-notify.org/iss-now.json
#The output is JSON for which we can make a simple get request

#We have to use requests library to use it

import requests # type: ignore

response = requests.get("http://api.open-notify.org/iss-now.json")  #This makes a get request at the endpoint

data = response.json()   #Response is an object we need to get data out of it
print(data)


#The response is a status code which can be:
# 1XX: Hold On..
# 2XX: Here You Go Sucess..
# 3XX: You Dont Have Permission..
# 4XX: You Messed Up..
# 5XX: I Messed Up..

#API Parameters:
#For requests such as withdrawing money you must also give input like
#your credentials these areknown as API Parameters
#API parameter is essentially input you can pass with api request

#e.g. in below sunrise and sunset api you must provide latitude and longitude



parameters = {
    "lat": 40.712776,
    "lng": -74.005974,
}

response = requests.get("https://api.sunrise-sunset.org/json",params = parameters)

sunrise = response.json()["results"]["sunrise"]  #Extract time for sunrise from json
sunset = response.json()["results"]["sunset"]  #Extract time for sunrise from json

print(sunrise)
print(sunset)
 

