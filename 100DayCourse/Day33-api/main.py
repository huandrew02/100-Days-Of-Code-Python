import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 40.712776
MY_LNG = -74.005974
MY_EMAIL = "huandrew321@gmail.com"
PASSWORD = "urwzaavdhowlenbu"

# your position is +- 5 degrees of the iss position
def poscheck():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    # print(longitude, latitude)
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        print("ISS is close to your current position")
        return True
    else:
        print("ISS is not close to your current position")
        return False

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

# if iss is close to my current location and it is currently dark, then send me an email to loop up BONUS: runt he code every 60 seconds
while True:
    if poscheck() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # make the connection secure
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL, 
                msg=f"Subject:LOOK OUTSIDE!\n\nThe ISS is above you in the sky. Go outside and look up!"
            )

    time.sleep(60)

