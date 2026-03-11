
"""
Lets do something with apis?
Like weather, news, stocks, etc?
Ok weather is a good one, lets do that.
Maybe not weather it's no fun
"""

import requests

def get_weather(city):
  city = city.replace(" ", "+")
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    return f"The current temperature in {city.replace('+', ' ')} is {temp}°C with {description}."

