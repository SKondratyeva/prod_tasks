from src.weather_03.weather_wrapper import WeatherWrapper
import unittest
from unittest.mock import patch
import requests
from unittest.mock import MagicMock


BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def test_weather():
    with patch.object(requests, 'get', return_value=BASE_URL) as mock_method:

        thing = WeatherWrapper(api_key='fgf')
        res = thing.get(city='city', url=BASE_URL)

    assert BASE_URL == res


def test_response_city2():

    mocked_request_0 = MockResponse('data', 200)
    with patch.object(requests, 'get', return_value = mocked_request_0) as mock_method:

        thing = WeatherWrapper(api_key='fgf')
        response = thing.get(city='city', url=BASE_URL)

    assert response.status_code == 200

    with patch.object(WeatherWrapper, 'get', return_value=mocked_request_0) as mock_method:
         thing = WeatherWrapper(api_key='fgf')
         response = thing.get(city='city', url=BASE_URL)
         print( thing.get_response_city(city='city', url=BASE_URL))
         assert 'data' == thing.get_response_city(city='city', url=BASE_URL)


mocked_request_1 = MockResponse('data', 290)


class MyTestCase(unittest.TestCase):

    def test_no_path(self):
        mocked_request_1 = MockResponse('data', 290)
        with self.assertRaises(AttributeError):
             thing = WeatherWrapper(api_key='fgf')
             thing.get = MagicMock(return_value=mocked_request_1)
             response = thing.get_response_city(city='city', url=BASE_URL)

if __name__ == '__main__':
    unittest.main()

def test_get_temp():
    data = {'main': {'temp': 10}}
    mock_obj = MockResponse(data, 200)

    with patch.object(requests, 'get', return_value = mock_obj) as mock_method:
        thing = WeatherWrapper(api_key='fgf')
        response = thing.get_response_city(city='city', url=BASE_URL)
        temp_diff = thing.find_diff_two_cities('dfg', 'fdg')


    assert 0 == temp_diff
    assert 10 == response['main']['temp']

def test_get_temp_diff():
    data = {'main': {'temp': 10}}
    data_2 = {'main': {'temp': 20}}
    mock_obj = MockResponse(data, 200)
    mock_obj_2 = MockResponse(data, 200)

    with patch.object(WeatherWrapper, 'get', return_value = mock_obj) as mock_method:
        thing = WeatherWrapper(api_key='fgf')
        city1 = 'dfg'
        city2 = 'hhh'
        diff = thing.get_diff_string(city1, city2)
        status = 'warmer'
        temperature_diff = 0
        assert f'Weather in {city1} is {status} than in {city2} by {temperature_diff} degrees' ==  diff

