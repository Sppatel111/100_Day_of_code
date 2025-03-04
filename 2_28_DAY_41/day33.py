import requests
import datetime
import smtplib
import time
from config import EMAIL,KEY_PASSWORD

my_email = EMAIL
password = KEY_PASSWORD

MY_LAT=20.593683
MY_LNG=78.962883
def iss_overhead():
    response=requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data=response.json()
    iss_longitude=float(data['iss_position']['longitude'])
    iss_latitude=float(data['iss_position']['latitude'])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

def is_night():
    parameters={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0,
    }
    response2=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    data2=response2.json()
    print(data2)

    sunrise=int(data2["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset=int(data2["results"]["sunset"].split('T')[1].split(':')[0])

    time_now=datetime.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# print(response.status_code)
# if response.status_code == 404:
#     raise Exception("That resources doesn't exist")
# if response.status_code == 401:
#     raise Exception("you are not authorized to access data.")
while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="subject:Lookup\n\nthe iss is above you in the sky.")

