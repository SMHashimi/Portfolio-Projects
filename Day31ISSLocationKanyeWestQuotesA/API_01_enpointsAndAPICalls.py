
#import the built-in library 'requests'
from requests import get
ISS_endpoints = get(url = "http://api.open-notify.org/iss-now.json")
# print(ISS_endpoints.status_code)
ISS_endpoints.raise_for_status()
data = (ISS_endpoints.json())
# print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
ISS_position = (longitude, latitude)


#The ISS (the Internationla Space Station) location as of now (https://www.latlong.net/Show-Latitude-Longitude.html)
print(ISS_position)


