import unittest

from src.Block.small_k_blocker import small_k_blocker

class Test_Small_K_Blocker(unittest.TestCase):
    def test_small_k_blocker_with_small_k_returns_empty_string(self):
        input = "k"

        self.assertEqual(small_k_blocker(input), "")

    def test_small_k_blocker_with_big_k_returns_big_k(self):
        input = "K"

        self.assertEqual(small_k_blocker(input), "K")

    def test_given_a_non_letter_symbol_small_k_blocker_returns_symbol(self):
        input = "!"

        self.assertEqual(small_k_blocker(input), "!")

    def test_given_a_number_small_k_blocker_returns_number(self):
        input = "1"

        self.assertEqual(small_k_blocker(input), "1")
