import unittest

from src.Block.uppercase_converter import uppercase_converter

class Test_Uppercase(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_given_a_lower_case_letter_UpperCase_returns_upper_case_letter(self):
        input = "a"

        self.assertEqual(uppercase_converter(input), "A")
        
    def test_given_an_upper_case_letter_UpperCase_returns_upper_case_letter(self):
        input = "A"

        self.assertEqual(uppercase_converter(input), "A")

    def test_given_a_non_letter_symbol_UpperCase_returns_the_same_symbol(self):
        input = "!"

        self.assertEqual(uppercase_converter(input), "!")

if __name__ == "__main__":
    unittest.main()
