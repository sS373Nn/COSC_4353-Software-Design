import unittest
import textwrap

from src.spell_check import get_response, parseresponse
from src.process_text import process_text

class ProcessTextTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_process_empty_text(self):
       self.assertEqual(process_text(""), "")

    def test_process_text_with_hello(self):
        self.assertEqual(process_text("hello"), "hello")

    def test_process_text_blah_which_we_will_consider_wrong_spelling(self):
        self.assertEqual(process_text("blah", lambda word: False), "[blah]")

    def test_process_text_one_good_word_one_mispelled_word(self):
        self.assertEqual(process_text("hello wrld", lambda word: word == "hello"), "hello [wrld]")

    def test_process_text_takes_hello_there_correctly(self):
        spelling_dictionary = ["hello", "world"]
        self.assertEqual(process_text("hello world", lambda word: word in spelling_dictionary), "hello world") 

    def test_process_text_takes_hello_tyoo_correctly(self):
        spelling_dictionary = ["hello"]
        self.assertEqual(process_text("hello tyop", lambda word: word in spelling_dictionary), "hello [tyop]") 

    def test_process_text_takes_misp_hello_correctly(self):
        spelling_dictionary = ["hello"]
        self.assertEqual(process_text("misp hello", lambda word: word in spelling_dictionary), "[misp] hello") 

    def test_process_text_takes_hello_tyop_there_misp_correctly(self):
        spelling_dictionary = ["hello", "there"]
        self.assertEqual(process_text("hello tyop there misp", lambda word: word in spelling_dictionary), "hello [tyop] there [misp]") 
    
    def test_process_text_takes_text_with_two_lines_and_returns_text_with_two_lines(self):
        spelling_dictionary = ["hello", "there"]
        text_with_two_lines = """hello
        there"""
        expected_return_value = textwrap.dedent("""
        hello
        there
        """).strip()

        self.assertEqual(process_text(text_with_two_lines, lambda word: word in spelling_dictionary), expected_return_value)

    def test_process_text_takes_text_with_two_lines_with_some_incorrect_spelling_words(self):
        spelling_dictionary = ["hello", "dog"]
        text_with_two_lines = """hello
        thee dog"""
        expected_return_value = textwrap.dedent("""
        hello
        [thee] dog""").strip()

        self.assertEqual(process_text(text_with_two_lines, lambda word: word in spelling_dictionary), expected_return_value)

    def test_process_text_takes_text_with_three_lines_and_returns_text_with_three_lines(self):
        spelling_dictionary = ["hello", "there", "dog"]
        text_with_three_lines = """hello
        there
        dog"""
        expected_return_value = textwrap.dedent("""
        hello
        there
        dog""").strip()
        
        self.assertEqual(process_text(text_with_three_lines, lambda word: word in spelling_dictionary), expected_return_value)
    
    def test_process_text_takes_text_with_three_lines_with_some_incorrect_spelling_words(self):
        spelling_dictionary = ["there"]
        text_with_three_lines = """hllo
        there
        dg"""
        expected_return_value = textwrap.dedent("""
        [hllo]
        there
        [dg]""").strip()
        
        self.assertEqual(process_text(text_with_three_lines, lambda word: word in spelling_dictionary), expected_return_value)

    def test_process_text_takes_text_that_runs_into_an_exception_from_the_spellchecker_for_one_word(self):
        text_string = "hello there how aare you"
        
        def is_spelling_correct(word):
          if word == 'there':
              raise Exception("Simulated Exception")
    
          return word != 'aare'
        
        self.assertEqual(process_text(text_string, is_spelling_correct), "hello _there_ how [aare] you")

if __name__ == '__main__': 
  unittest.main()
