import unittest

from src.process_airport import process_airports
from src.airport import Airport
from src.criteria_to_sort import criteria_to_sort_iata
from src.criteria_to_sort import criteria_to_sort_name
from src.criteria_to_sort import criteria_to_sort_city
from src.criteria_to_sort import criteria_to_sort_state
from src.criteria_to_sort import criteria_to_sort_delay
from src.criteria_to_sort import criteria_to_sort_temperature
from src.criteria_to_sort import criteria_to_sort_city_and_name

class Tests(unittest.TestCase):
  def setUp(self):
    self.iad = Airport("IAD", "DULLES INTL", "Washington", "DC", 71, "true")
    self.ord = Airport("ORD", "O'HARE INTERNATIONAL", "Chicago", "IL", 62, "true")
    self.mdw = Airport("MDW", "MIDWAY INTERNATIONAL", "Chicago", "IL", 60, "false")
  
  def test_canary(self):
    self.assertTrue(True)

  def test_process_airports_takes_an_empty_list_and_returns_an_empty_list(self):
    self.assertEqual(process_airports([]), [])

  def test_process_airport_takes_one_item_returns_one_item(self):
    airports = [self.iad]

    self.assertEqual(process_airports(airports), airports)

  def test_airport_takes_two_airports(self):
    airports = [self.iad, self.ord]

    self.assertEqual(process_airports(airports), airports)

  def test_process_airport_takes_three_airports(self):
    airports = [self.iad, self.mdw, self.ord]

    self.assertEqual(process_airports(airports), airports)

  def test_airport_takes_two_airports_and_sorts_by_iata_code(self):
    airports = [self.ord, self.iad] 
    sorted_airports = [self.iad, self.ord]  

    self.assertEqual(process_airports(airports, sort_key = criteria_to_sort_iata.criteria_to_sort), sorted_airports)

  def test_airport_takes_three_airports_and_sorts_by_name(self):
    airports = [self.ord, self.iad, self.mdw] 
    sorted_airports = [self.iad, self.mdw, self.ord]  

    self.assertEqual(process_airports(airports, sort_key = criteria_to_sort_name.criteria_to_sort), sorted_airports)

  def test_process_airports_takes_three_airports_and_sorts_by_city(self):
    airports = [self.ord, self.iad, self.mdw] 
    sorted_airports = [self.ord, self.mdw, self.iad]  

    self.assertEqual(process_airports(airports, sort_key = criteria_to_sort_city.criteria_to_sort), sorted_airports)

  def test_process_airports_takes_three_airports_and_sorts_by_state(self):
    airports = [self.ord, self.iad, self.mdw] 
    sorted_airports = [self.iad, self.ord, self.mdw]  

    self.assertEqual(process_airports(airports, sort_key = criteria_to_sort_state.criteria_to_sort), sorted_airports)

  def test_process_airports_takes_three_airports_and_sorts_by_delay(self):
    airports = [self.iad, self.mdw, self.ord] 
    sorted_airports = [self.mdw, self.iad, self.ord]  

    self.assertEqual(process_airports(airports, sort_key = criteria_to_sort_delay.criteria_to_sort), sorted_airports)

  def test_process_airports_takes_three_airports_and_sorts_by_temperature(self):
    airports = [self.iad, self.mdw, self.ord] 
    sorted_airports = [self.mdw, self.ord, self.iad]  

    self.assertEqual(process_airports(airports, sort_key = criteria_to_sort_temperature.criteria_to_sort), sorted_airports)

  def test_process_airports_takes_three_airports_and_sorts_by_city_and_name(self):
    airports = [self.iad, self.mdw, self.ord] 
    sorted_airports = [self.mdw, self.ord, self.iad] 

    self.assertEqual(process_airports(airports, sort_key = criteria_to_sort_city_and_name.criteria_to_sort), sorted_airports)

  def test_process_airports_given_airports_with_lowercase_names_returns_airports_with_name_in_uppercase(self):
    sfo = Airport("SFO", "San Francisco Intl.", "San Francisco", "CA", 59, "false")

    result = process_airports([sfo])
    
    self.assertEqual(sfo.name, "San Francisco Intl.")
    self.assertEqual(result[0].name, "SAN FRANCISCO INTL.")

if __name__ == '__main__': 
  unittest.main()
