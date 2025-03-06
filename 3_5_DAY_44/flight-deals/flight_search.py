import requests
from flight_keys import API_KEY,API_SECRET
# from https://developers.amadeus.com/
api_key=API_KEY
api_secret=API_SECRET

flight_endpoint='https://test.api.amadeus.com/v2/shopping/flight-offers'
iata_endpoint='https://test.api.amadeus.com/v1/reference-data/locations/cities'
token_endpoint='https://test.api.amadeus.com/v1/security/oauth2/token'
class FlightSearch:
    def __init__(self):
        self.api_key=api_key
        self.api_secret=api_secret
        self.token=self.get_new_token()

    def get_new_token(self):
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response=requests.post(url=token_endpoint,headers=headers,data=body)

        return response.json()['access_token']


    def get_destination_code(self,city_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "countryCode":"FR",
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response=requests.get(url=iata_endpoint,headers=headers,params=query)
        # code=response.json()
        # print(code)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flights(self,origin_city_code, destination_city_code, from_time, to_time):
        headers={"Authorization": f"Bearer {self.token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response=requests.get(url=flight_endpoint,params=query, headers=headers)
        print(response.status_code)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()



# ft=FlightSearch()
# ft.get_destination_code("Paris")
# print(ft.token)
