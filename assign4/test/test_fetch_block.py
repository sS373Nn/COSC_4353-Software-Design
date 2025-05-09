import unittest

from src.Block.fetch_block import fetch_block
from src.Block.uppercase_converter import uppercase_converter
from src.Block.lowercase_converter import lowercase_converter
from src.Block.multiplier_converter import multiplier_converter
from src.Block.big_z_blocker import big_z_blocker
from src.Block.small_k_blocker import small_k_blocker

class Test_Fetch_Block(unittest.TestCase):
    def test_fetch_block_with_uppercase_converter(self):
        
        self.assertEqual(fetch_block("uppercase converter"), uppercase_converter)

    def test_fetch_block_with_lowercase_converter(self):
        
        self.assertEqual(fetch_block("lowercase converter"), lowercase_converter)

    def test_fetch_block_with_multiplier_converter(self):
        
        self.assertEqual(fetch_block("multiplier converter"), multiplier_converter)

    def test_fetch_block_with_big_z_blocker(self):
        
        self.assertEqual(fetch_block("big z blocker"), big_z_blocker)

    def test_fetch_block_with_small_k_blocker(self):
        
        self.assertEqual(fetch_block("small k blocker"), small_k_blocker)
