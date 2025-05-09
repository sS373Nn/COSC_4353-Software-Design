import unittest

from src.Block.small_z_blocker import small_z_blocker

class Test_Small_Z_Blocker(unittest.TestCase):
    def test_small_z_blocker_with_small_z_returns_empty_string(self):
        input = "z"

        self.assertEqual(small_z_blocker(input), "")

    def test_small_z_blocker_with_big_z_returns_big_z(self):
        input = "Z"

        self.assertEqual(small_z_blocker(input), "Z")

    def test_given_a_non_letter_symbol_small_z_blocker_returns_symbol(self):
        input = "!"

        self.assertEqual(small_z_blocker(input), "!")

    def test_given_a_number_small_z_blocker_returns_number(self):
        input = "1"

        self.assertEqual(small_z_blocker(input), "1")
