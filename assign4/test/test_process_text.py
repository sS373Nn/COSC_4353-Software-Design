import unittest

from src.process_text import process_text
from src.Block.uppercase_converter import uppercase_converter
from src.Block.lowercase_converter import lowercase_converter
from src.Block.multiplier_converter import multiplier_converter
from src.Block.small_k_blocker import small_k_blocker
from src.Block.big_z_blocker import big_z_blocker

class Test_Process_Text(unittest.TestCase):
    def test_process_text_with_string_and_no_block(self):
        input = "Hello"

        self.assertEqual(process_text(input), "Hello")

    def test_process_text_with_uppercase_block(self):
        input = "Hello"

        self.assertEqual(process_text(input, uppercase_converter), "HELLO")

    def test_process_text_with_lowercase_block(self):
        input = "Hello"

        self.assertEqual(process_text(input, lowercase_converter), "hello")

    def test_process_text_with_multiplier_block(self):
        input = "Hello"

        self.assertEqual(process_text(input, multiplier_converter), "HHeelllloo")
        
    def test_process_text_with_two_block_small_k_blocker_and_multiplier_blocks(self):
        input = "Hellok"
        
        self.assertEqual(process_text(input, small_k_blocker, multiplier_converter), "HHeelllloo")

    def test_process_text_with_abzde_and_uppercase_converter_and_big_z_blocker(self):
        input = "abzde"

        self.assertEqual(process_text(input, uppercase_converter, big_z_blocker), "ABDE")
    
    def test_process_text_with_abzde_and_big_z_blocker_and_uppercase_converter(self):
        input = "abzde"

        self.assertEqual(process_text(input, big_z_blocker, uppercase_converter), "ABZDE")

    def test_process_text_with_abzde_and_uppercase_converter_and_multiplier_converter(self):
        input = "abzde"

        self.assertEqual(process_text(input, uppercase_converter, multiplier_converter), "AABBZZDDEE")

    def test_process_text_with_abzde_and_big_z_blocker_and_uppercase_converter_and_multiplier_converter(self):
        input = "abzde"

        self.assertEqual(process_text(input, big_z_blocker, uppercase_converter, multiplier_converter), "AABBZZDDEE")
