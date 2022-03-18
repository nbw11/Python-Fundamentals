import unittest
from exercise14 import city_country


def test_city_country(city, country):
    city_country = '{0}, {1}'.format(city, country)
    return city_country

