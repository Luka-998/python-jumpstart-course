import datetime as dt
import requests
import json
# I will check Belgrade weather status and temperature
# This app was not done in accordance to -Build 10 apps Course- but with my python knowledge from before. 
# I got API key from meteosource website (Need to register first to receive API), below is the url (base_url)
text = 'WEATHER_APP'
print('-'*60)
print(f'{text:-^60}')
print('-'*60)

base_url = 'https://www.meteosource.com/api/v1/free/point'
API_key = 'saax8isli867z1sxichoidv253lnn9col23njuz4'
LOCATION = 'Belgrade'

parameters = {
    "place_id":LOCATION,
    'sections':'current',
    'key':API_key,
    'units':'metric'
    
}

response =requests.get(base_url,params=parameters)

if response.status_code==200: # 200: This means the request was successful and the API returned valid data.
    data = response.json() # this converts API's JSON response into python dict.
    temperature = data['current']['temperature']
    weather_desc = data['current']['summary']

    print(f'Current weather is: {weather_desc}')
    print(f'Current temperature is {temperature}\nFor the location: {LOCATION}')
else: # if API call fails
    print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")

    