from requests import *
from twilio.rest import Client

ACCOUNT_SID = "ACaf558fa5a2e4b53d3e6c85ae8b6104a6"
AUTH_TOKEN = "a35234df73788e44d0ed3377391b789e"
ZAINAB_HASHIMI = "whatsapp:+13473408570"

API_Key = "86c339ecb93847edd2a4f7ee7cd0dcf1"

panagia_params = {
    "lat": 35.185566,
    "lon": 33.382275,
    "appid": API_Key,
    "cnt": 4,
}

appweather = get(url = "https://api.openweathermap.org/data/2.5/forecast", params = panagia_params)
panagia_weather_dict = appweather.json()

raining = False
for id in range(0, len(panagia_weather_dict) - 1):
    all_cnts_ids = (panagia_weather_dict["list"][id]["weather"][0]["id"])
    print(all_cnts_ids)
    if all_cnts_ids < 850:
        raining = True
if raining:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body = "Good morning Khwar,\n<<Love you>>\nSincerely, SayedHashimi",
        from_ = "whatsapp:+14155238886",
        to = ZAINAB_HASHIMI
    )

    print(message.status)
    print(message.sid)
    print(message.body)










