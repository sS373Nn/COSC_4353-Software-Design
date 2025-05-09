import unittest
from unittest.mock import patch

from src.spell_check import get_response, parseresponse, is_spelling_correct

class SpellCheckerTests(unittest.TestCase):
    def test_get_response(self):
        response = get_response("hello")

        self.assertGreater(len(response), 0)
    
    def test_parse_response_returns_true(self):
        response = "true"

        self.assertTrue(parseresponse(response))

    def test_parse_response_returns_false(self):
        response = "false"

        self.assertFalse(parseresponse(response))

    @patch('src.spell_check.get_response')
    @patch('src.spell_check.parseresponse')
    def test_is_spelling_correct_with_get_response_parseresponse(self, mock_get_response, mock_parseresponse):
        mock_get_response.return_value = "true"
        mock_parseresponse.return_value = True

        result = is_spelling_correct("hello", mock_get_response, mock_parseresponse)

        mock_get_response.assert_called_once_with("hello")
        mock_parseresponse.assert_called_once_with("true")
        self.assertTrue(result)

    @patch('src.spell_check.get_response')
    @patch('src.spell_check.parseresponse')
    def test_is_spelling_correct_with_mocks(self, mock_get_response, mock_parseresponse):
        mock_get_response.side_effect = Exception("Simulated Exception")
        mock_parseresponse.return_value = True

        result = is_spelling_correct("hello", mock_get_response, mock_parseresponse)

        self.assertIsInstance(result, Exception)
        mock_get_response.assert_called_once_with("hello")
        mock_parseresponse.assert_not_called()
        