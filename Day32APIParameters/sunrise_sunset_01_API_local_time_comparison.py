from requests import *
from datetime import *

LATITUDE = 43.6525280
LONGTITUDE = -73.756233
FORMATTED = 0

parameters = {
    "lat": LATITUDE,
    "lng": LONGTITUDE,
    "formatted": FORMATTED,
}

sunset_sunrise = get(url = "https://api.sunrise-sunset.org/json", params = parameters)
sunset_sunrise.raise_for_status()

current_date_time = datetime.now().hour
data = sunset_sunrise.json()["results"]
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]

print(f"Sunrise hour: {sunrise}")
print(f"Sunset hour: {sunset}")
print(f"Local hour: {current_date_time}")




