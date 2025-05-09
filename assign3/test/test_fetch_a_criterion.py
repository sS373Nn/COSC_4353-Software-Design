import unittest

from src.fetch_a_criterion import fetch_a_criterion, fetch_criteria
from src.criteria_to_sort import criteria_to_sort_name
from src.criteria_to_sort import criteria_to_sort_city
from src.criteria_to_sort import criteria_to_sort_city_and_name

class Tests(unittest.TestCase):
    def test_fetch_a_criteria_returns_criteria_function(self):
        self.assertEqual(fetch_a_criterion("name"), criteria_to_sort_name.criteria_to_sort)

    def test_fetch_a_criteria_city_returns_city(self):
        self.assertEqual(fetch_a_criterion("city"), criteria_to_sort_city.criteria_to_sort)

    def test_given_property_city_and_name_fetch_a_criterion_returns_city_and_name(self):
        self.assertEqual(fetch_a_criterion("city and name"), criteria_to_sort_city_and_name.criteria_to_sort) 

    def test_fetch_criteria_contains_name(self):
        self.assertTrue("name" in fetch_criteria())

    def test_fetch_criteria_contains_city_and_name(self):
        self.assertTrue("city and name" in fetch_criteria())
       