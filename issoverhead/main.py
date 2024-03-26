import requests
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = int(str(datetime.now()).split(" ")[1].split(":")[0])


#If the ISS is close to my current position - done
# and it is currently dark - done
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

print(f"sunrise : {sunrise}, sunset : {sunset}, current : {time_now}" )
print(f"iss lat : {iss_latitude}, iss long : {iss_longitude}")

def check_dark():
    if time_now <= sunrise or time_now >= sunset:
        return True

def check_ISS_position():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        if MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            return True
        else:
            return False
    else:
        return False

if check_dark() and check_ISS_position():
    print("YES MATE LOOK UP")
else:
    print("NO MATE")

