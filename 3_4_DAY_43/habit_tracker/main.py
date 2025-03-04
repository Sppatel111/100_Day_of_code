import requests
import datetime

USERNAME="alianx"
TOKEN="thisissecret"
GRAPH_ID="graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token":TOKEN ,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_param = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "km",
    "type":"float",
    "color": "ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}
# response1=requests.post(url=graph_endpoint,json=graph_param,headers=headers)

#create
pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime.datetime.now()
print(today.strftime("%Y%m%d"))

pixel_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity":input("how many kilometers did you cycle today?"),
}
response2=requests.post(url=pixel_creation_endpoint,json=pixel_param,headers=headers)
print(response2.text)

#update
update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_pixel={
    "quantity":"20.05"
}
# response3=requests.put(url=update_endpoint,json=update_pixel, headers=headers,)
# print(response3.text)

#delete
delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response4=requests.delete(url=delete_endpoint,headers=headers)
# print(response4.text)