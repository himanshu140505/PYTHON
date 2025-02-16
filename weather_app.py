import requests
from systemcommands import *

def weather_app_logo():
    print("================================================")
    print("||               WEATHER APP                  ||")
    owner()
    print("================================================")

def weather_app():
    clearscreen()
    weather_app_logo()
    print("================================================")
    current_location = input("|| Enter the location : ")
    print("================================================")
    clearscreen()
    weather_app_logo()
    url = f'http://api.weatherapi.com/v1/current.json?key=YOUR_KEY_HERE&q={current_location}&lang=english'
    response = requests.get(url)
    response_text = response.json()

    print("================================================")
    print(f"||  TEMPERATURE : {response_text['current']['temp_c']}*C                      ||")
    print(f"||  FEELS LIKE  : {response_text['current']['feelslike_c']}*C                      ||")
    print(f"||  WIND DIR.   : {response_text['current']['wind_dir']}                           ||")
    print(f"||  WIND SPEED  : {response_text['current']['wind_kph']}kph                      ||")
    print(f"||  WIND DEGREE : {response_text['current']['wind_degree']}                         ||")
    print(f"||  HUMIDITY    : {response_text['current']['humidity']}                          ||")

    print("================================================")
    

weather_app()

