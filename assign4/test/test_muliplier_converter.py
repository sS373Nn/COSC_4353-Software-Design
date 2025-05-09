import unittest

from src.Block.multiplier_converter import multiplier_converter

class Test_Multiplier(unittest.TestCase):
    def test_given_a_lower_case_letter_Multiplier_returns_two_of_the_same_lower_case_letters(self):
        input = "a"

        self.assertEqual(multiplier_converter(input), "aa")
        
    def test_given_an_upper_case_letter_Multipler_returns_two_of_the_same_lower_case_letters(self):
        input = "A"

        self.assertEqual(multiplier_converter(input), "AA")

    def test_given_a_non_letter_symbol_Multipler_returns_two_of_the_same_symbol(self):
        input = "!"

        self.assertEqual(multiplier_converter(input), "!!")

    def test_given_a_number_Multipler_returns_two_of_the_same_number(self):
        input = "1"

        self.assertEqual(multiplier_converter(input), "11")
