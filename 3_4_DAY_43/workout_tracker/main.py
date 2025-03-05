import json
import requests
from datetime import datetime as dt
from config3 import NUTRITION_API_ID,NUTRITION_API_KEY
nutrition_api_id=NUTRITION_API_ID
nutrition_api_key=NUTRITION_API_KEY

GENDER = 'Female'
WEIGHT_KG = 55
HEIGHT_CM = 160
AGE = 21

exercise_text = input('Tell me which exercises you did: ')

sheet_endpoint='https://api.sheety.co/6d839aa4beb61480cf4b7817313db86b/myWorkout/sheet1'
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers={
    'x-app-id':nutrition_api_id,
    'x-app-key':nutrition_api_key,
}

parameters={
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}
response=requests.post(url= exercise_endpoint, json=parameters, headers=headers)
result=response.json()
print(result)

today_date=dt.now().strftime("%d/%m/%Y")
print(today_date)
now_time=dt.now().strftime(('%X'))
print(now_time)

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],

        }
    }
    print(sheet_inputs)
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=headers)

    print(sheet_response.text)


