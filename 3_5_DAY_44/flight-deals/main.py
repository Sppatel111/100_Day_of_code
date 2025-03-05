#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime,timedelta
import time

from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch

dm=DataManager()
sheet_data=dm.get_destination_data()
fs=FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row["iataCode"]=fs.get_destination_code(row["city"])
    print(sheet_data)

    dm.destination_data=sheet_data
    dm.update_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = fs.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flights)
    cheapest_flight =find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)