import requests
import datetime
import smtplib
import time
from manage import KEY_PASSWORD,EMAIL
my_email = EMAIL
password = KEY_PASSWORD

MY_LAT = 20.593683
MY_LNG = 78.962883


# iss API
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # check position is within like +5 or -5 degree of iss_position.
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True


# sunset and sunset time
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now_time = datetime.datetime.now().hour

    if now_time <= sunrise or now_time >= sunset:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(to_addrs=my_email, from_addr=my_email, msg="Subject:Lock up \n\niss is above in the sky.")
