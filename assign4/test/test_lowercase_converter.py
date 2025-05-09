import unittest

from src.Block.lowercase_converter import lowercase_converter

class Test_Lowercase(unittest.TestCase):
    def test_given_a_lower_case_letter_LowerCase_returns_lower_case_letter(self):
        input = "a"

        self.assertEqual(lowercase_converter(input), "a")
        
    def test_given_an_upper_case_letter_LowerCase_returns_lower_case_letter(self):
        input = "A"

        self.assertEqual(lowercase_converter(input), "a")

    def test_given_a_non_letter_symbol_LowerCase_returns_the_same_symbol(self):
        input = "!"

        self.assertEqual(lowercase_converter(input), "!")
