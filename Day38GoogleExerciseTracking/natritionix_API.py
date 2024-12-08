from requests import *
from datetime import *

current_date = datetime.now()
current_hour = current_date.time().hour
current_minute = current_date.time().minute
current_second = current_date.time().second
current_time = f"{current_hour}:{current_minute}:{current_second}"

APPLICATION_ID = "3c27cf40"
APPLICATION_KEY = "5f18f386557a9ab4073966886c386266"
endpoint_headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY
}
user_inquery = input("Tell me which exercises you did: ")
nutrients_params = {
    "query": user_inquery,
    "gender": "male",
    "weight_kg": 86,
    "height_cm": 187,
    "age": 27
}
response = post(url = "https://trackapi.nutritionix.com/v2/natural/exercise", headers = endpoint_headers, json = nutrients_params)
getting_response = response.json()
# print(getting_response)

#getting the 'workouts' from sheety - https://dashboard.sheety.co/projects/675497037ce98606875e7062/sheets/workouts
sheety_get_endpoint = post(url = "https://api.sheety.co/c559dfa8d031dc2b5af5c76c99ae8e91/exerciseTracking/workouts").json()

# posting the details on the spreadsheet
today_date = datetime.now().strftime("%d/%m/%Y")

for exercise in getting_response["exercises"]:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    print(exercise)
    # sheety_post_endpoint = post(url = "https://api.sheety.co/c559dfa8d031dc2b5af5c76c99ae8e91/exerciseTracking/workouts", json = sheety_params) #No authentication
    sheety_post_endpoint = post(url = "https://api.sheety.co/c559dfa8d031dc2b5af5c76c99ae8e91/exerciseTracking/workouts", json = sheety_params, auth = ("Sayed Mubaris Hashimi", "1234567Lexus600")) #Basic Authentication


    print(sheety_post_endpoint.text)