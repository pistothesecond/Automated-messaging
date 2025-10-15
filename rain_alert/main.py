
import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "97076de4dc04e8ca1c1d33f278fd6a57"
account_sid = 'AC9499fdc3e952c897807e1a8bc677ca64'
auth_token = '[AuthToken]'


weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])



will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
            .create(
        body="It's goint to be rainy today, remember to bring an umbrella",
        fro= "+447564270384",
        to="+447477406660",
    )
    print(message.sid)

