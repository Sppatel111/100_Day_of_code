import requests
from dotenv import load_dotenv
import os
from config44 import SHEET_ENDPOINT
# load_dotenv()
# sheet_endpoint=os.environ.get("SHEET_ENDPOINT")

class DataManager:
    def __init__(self):
        self.destination_data={}
    def get_destination_data(self):
        response=requests.get(url=SHEET_ENDPOINT)
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
            response=requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}",json=sheet_input)
            print(response.text)

