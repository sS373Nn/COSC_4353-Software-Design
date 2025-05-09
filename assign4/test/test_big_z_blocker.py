import unittest

from src.Block.big_z_blocker import big_z_blocker

class Test_Big_Z_Blocker(unittest.TestCase):
    def test_big_z_blocker_with_big_z_returns_empty_string(self):
        input = "Z"

        self.assertEqual(big_z_blocker(input), "")

    def test_big_z_blocker_with_small_z_returns_small_z(self):
        input = "z"

        self.assertEqual(big_z_blocker(input), "z")

    def test_given_a_non_letter_symbol_big_z_blocker_returns_symbol(self):
        input = "!"

        self.assertEqual(big_z_blocker(input), "!")

    def test_given_a_number_big_z_blocker_returns_number(self):
        input = "1"

        self.assertEqual(big_z_blocker(input), "1")
