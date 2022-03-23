from src.weather_03.weather_wrapper import WeatherWrapper
from unittest import mock
from unittest.mock import MagicMock
from unittest.mock import patch

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

def weather_test():
    with patch.object(WeatherWrapper, 'get', return_value=BASE_URL) as mock_method:

         thing = WeatherWrapper(api_key ='fgf')
         res = thing.get(city = 'city', url = BASE_URL)

    assert res == BASE_URL

def response_city_test():
    with patch.object(WeatherWrapper, 'get_response_city', return_value={}) as mock_method:

         thing = WeatherWrapper(api_key ='fgf')
         res = thing.get_response_city(city = 'city', url = BASE_URL)

    assert res == {}

def response_cit_test():
    with patch.object(WeatherWrapper, 'get_temperature', return_value= {'main': { "temp":0}}) as mock_method:

         thing = WeatherWrapper(api_key ='fgf')
         response = thing.get_temperature(city = 'city', url = BASE_URL)

    assert response['main']['temp'] == 0

