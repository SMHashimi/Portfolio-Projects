
from requests import *
from datetime import *
today = datetime(year = 2024, month = 12, day = 5)
# yyyy_mm_dd = f"{today.year}{today.month}{today.day}"  - applicable only for the days:1 - 9: 2024125
# print(today.strftime("%Y%m%d"))                                                             20241205

#Step;1 - Creating an account in Pixela
creating_pixelaAccount_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "hashimiSay123456ed",
    "username": "mubaris",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#There is no need to have the two below because now we have created our account
creating_account_response = post(url = creating_pixelaAccount_endpoint, json = user_params)
# print(response.text)

#Step;2 - Making a graph - /v1/users/<username>/graphs
graph_endpoint = "https://pixe.la/v1/users/mubaris/graphs"
graph_params = {
    "id": "graph1",
    "name": "My Habit Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
graph_headers = {
    "X-USER-TOKEN": "hashimiSay123456ed"
}
graph_creation_response = post(url = graph_endpoint, json = graph_params, headers = graph_headers)

#Step;3 - Posting a value to graph
#https://www.w3schools.com/python/python_datetime.asp
value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}
value_headers = {
    "X-USER-TOKEN": "hashimiSay123456ed"
}
VALUE_POINT = "https://pixe.la/v1/users/mubaris/graphs/graph1"
value_to_post = post(url = VALUE_POINT, json = value_params, headers = value_headers)

#Updating Data
update_endpoint = "https://pixe.la/v1/users/mubaris/graphs/graph1/" + today.strftime("%Y%m%d")
new_data = {
    "quantity": "4.5"
}
update_headers = {
    "X-USER-TOKEN": "hashimiSay123456ed"
}
response_response = put(url = update_endpoint, json = new_data, headers = update_headers)

#Deleting Data
delete_headers = {
    "X-USER-TOKEN": "hashimiSay123456ed"
}
delete_endpoint = "https://pixe.la/v1/users/mubaris/graphs/graph1/" + today.strftime("%Y%m%d")
delete_response = delete(url = delete_endpoint, headers = delete_headers)
print(delete_response.text)


