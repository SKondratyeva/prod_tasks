from src.weather_03.weather_wrapper import WeatherWrapper
import unittest
from unittest.mock import patch
import requests
from unittest.mock import MagicMock
from unittest.mock import Mock
data1 = {'list': [{'main': {'temp': 10}}] * 8}

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data





def test_get_tom_diff():

    WeatherWrapper.get_tomorrow_temperature = Mock(return_value=10)
    WeatherWrapper.get_temperature = Mock(return_value=4)

    assert WeatherWrapper(api_key='dfgh').get_tomorrow_diff(city='dfg') \
        == 'The weather in dfg tomorrow will be much warmer than today'


    WeatherWrapper.get_tomorrow_temperature = Mock(return_value=10)
    WeatherWrapper.get_temperature = Mock(return_value=9)

    assert WeatherWrapper(api_key='dfgh').get_tomorrow_diff(city='dfg') \
       == 'The weather in dfg tomorrow will be warmer than today'


    WeatherWrapper.get_tomorrow_temperature = Mock(return_value=7)
    WeatherWrapper.get_temperature = Mock(return_value=11)

    assert WeatherWrapper(api_key='dfgh').get_tomorrow_diff(city='dfg') \
       == 'The weather in dfg tomorrow will be much colder than today'


    WeatherWrapper.get_tomorrow_temperature = Mock(return_value=6)
    WeatherWrapper.get_temperature = Mock(return_value=7)

    assert WeatherWrapper(api_key='dfgh').get_tomorrow_diff(city='dfg') \
       == 'The weather in dfg tomorrow will be colder than today'

    WeatherWrapper.get_tomorrow_temperature = Mock(return_value=7)
    WeatherWrapper.get_temperature = Mock(return_value=7)

    assert WeatherWrapper(api_key='dfgh').get_tomorrow_diff(city='dfg') \
       == 'The weather in dfg tomorrow will be the same than today'

