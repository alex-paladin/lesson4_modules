# This the example of using external module in Python
# Yahoo Weather module is invoked
# pip install yahoo-weather
# Yahoo APP_ID is required (can be ordered here https://developer.yahoo.com/weather/?guccounter=1)

from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit

data = YahooWeather(APP_ID="ElssVX7a",
                     api_key="dj0yJmk9UWFZWjQ2RGNhY3BIJmQ9WVdrOVJXeHpjMVpZTjJFbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWE0",
                     api_secret="6e29d9f7fa9dd3c56e7a0319ecd0e51918e2f450")

print('Welcome to Yahoo Weather!')
print('*************************')
print('Input city name (e.g. Chisinau):')

city = input()

data.get_yahoo_weather_by_city(city, Unit.celsius)

print('Condition:',data.condition.text)
print('Temperature, Celcius:',data.condition.temperature)
print('Atmopshere pressure:',data.atmosphere.pressure)
print('Atmosphere humidity:',data.atmosphere.humidity)

