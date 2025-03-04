import requests
from twilio.rest import Client
from secret import AUTH_TOKEN,API_KEY,ACCOUNT_SID,FROM,TO
#weather
api_key=API_KEY
OWN_ENDPOINT="https://api.openweathermap.org/data/2.5/weather"
#twilio
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

parameters={
    'lat':20.593683,
    'lon':78.962883,
    'appid':api_key,
}
will_rain=False

response=requests.get(OWN_ENDPOINT,params=parameters)


data=response.json()



condition_code=data["weather"][0]["id"]
if condition_code < 700:
    will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today!!bring Umbrella.",
        from_=FROM,
        to=TO
    )
    print(message.status)





