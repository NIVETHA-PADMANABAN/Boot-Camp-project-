import requests
from datetime import datetime
import urllib.request
import numpy as np
print("                      WEATHER INFORMATION")
print("                     =====================")

api_key='fa0819d6b1990333dc8d16cf302e9af1'
print("")
place=input("Enter The Area Name:")
print("")
complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_info=api_link.json()
temperature=api_info['main']['temp']
weather=api_info['weather'][0]['description']
humidity=api_info['main']['humidity']
wind_speed=api_info['wind']['speed']
date_time=datetime.now().strftime(", Date : %d %m %y , Time : %I:%M:%S %p")
print("")
print("   * Today Weather Status In  {}  {}".format(place.lower(),date_time))
print("")
print("   * Today Temperature is : {:.2f} deg C ".format(temperature))
print("")
print("   * Current Weather Description :",weather)
print("")
print("   * Current Humidity :",humidity,"%")
print("")
print("   * Current Wind Speed :",wind_speed,"kmph")
print("") 





