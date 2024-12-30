# Lets do something creative with our time
from pip._vendor import requests

# Something goes here

def get_flight_data():
    url = 'https://opensky-network.org/api/states/all'
    response = requests.get(url)
    data = response.json()
    return data
flight_data = get_flight_data()
#print(flight_data)
