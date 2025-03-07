import requests
from config44 import SHEET_ENDPOINT

sheet_endpoint=SHEET_ENDPOINT

class DataManager:
    def __init__(self):
        self.destination_data={}
    def get_destination_data(self):
        response=requests.get(url=sheet_endpoint)
        data=response.json()
        self.destination_data =data["sheet1"]
        return self.destination_data
    def update_destination_data(self):
        for city in self.destination_data:
            sheet_input={
                "sheet1":{
                     "iataCode":city["iataCode"]
                }
            }
            response=requests.put(url=f"{sheet_endpoint}/{city['id']}",json=sheet_input)
            print(response.text)

