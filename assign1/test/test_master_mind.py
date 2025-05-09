import unittest

from src.color import Color
from src.master_mind import guess, play, select_colors
from src.match import Match
from src.result import Result


EXACT = Match.EXACT
PRESENT = Match.PRESENT
NO_MATCH = Match.NO_MATCH

class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_guess_with_all_colors_match_in_position(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = selected_colors 

    response = guess(selected_colors, user_provided_colors)

    self.assertEqual(response[EXACT], 6)

  def test_guess_with_all_mismatch_colors(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.WHITE, Color.BROWN, Color.PINK, Color.CYAN, Color.CYAN, Color.CYAN]

    response = guess(selected_colors, user_provided_colors)

    self.assertEqual(response[NO_MATCH], 6)

  def test_guess_with_all_colors_match_out_of_position(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE, Color.RED]

    response = guess(selected_colors, user_provided_colors)

    self.assertEqual(response, {EXACT: 0, PRESENT: 6, NO_MATCH: 0})

  def test_guess_with_first_four_colors_match_in_position(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.CYAN, Color.PINK]

    response = guess(selected_colors, user_provided_colors)
   
    self.assertEqual(response, {EXACT: 4, PRESENT: 0, NO_MATCH: 2})

  def test_guess_with_last_four_colors_match_in_position(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.PINK, Color.CYAN, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]

    response = guess(selected_colors, user_provided_colors)

    self.assertEqual(response, {EXACT: 4, PRESENT: 0, NO_MATCH: 2})

  def test_guess_with_first_three_color_match_in_position_last_three_match_out_position(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.PURPLE, Color.ORANGE, Color.YELLOW]

    response = guess(selected_colors, user_provided_colors)

    self.assertEqual(response, {EXACT: 3, PRESENT: 3, NO_MATCH: 0})

  def test_guess_first_and_third_color_mismatch_second_in_position_and_the_others_match_out_of_position(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.CYAN, Color.BLUE, Color.PINK, Color.PURPLE, Color.ORANGE, Color.YELLOW]

    response = guess(selected_colors, user_provided_colors)

    self.assertEqual(response, {EXACT: 1, PRESENT: 3, NO_MATCH: 2})

  def test_guess_with_first_color_in_selected_colors_repeated_from_position_two_to_six__first_position_in_guess_matches_second_color_in_color_selection(self):
    selected_colors = [Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE, Color.RED]
    user_provided_colors = [Color.GREEN, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]

    response = guess(selected_colors, user_provided_colors)

    self.assertEqual(response, {EXACT: 0, PRESENT: 2, NO_MATCH: 4})

  def test_guess_with_first_color_in_selected_colors_repeated_from_position_two_to_six_first_position_in_guess_no_match(self):
    selected_colors = [Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE, Color.RED]
    user_provided_colors = [Color.CYAN, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]

    response = guess(selected_colors, user_provided_colors)

    self.assertEqual(response, {EXACT: 0, PRESENT: 1, NO_MATCH: 5})

  def test_play_first_attempt_with_exact_match(self):
    selected_colors = [Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE, Color.RED]
    user_provided_colors = [Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE, Color.RED]

    number_of_attempts = 1

    result, currentAttempts, status = play(selected_colors, user_provided_colors, number_of_attempts)

    self.assertEqual((result, currentAttempts, status),
      (Result.WON, number_of_attempts + 1, {Match.EXACT: 6, Match.PRESENT: 0, Match.NO_MATCH: 0}))
    
  def test_play_first_attempt_with_no_match(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.WHITE, Color.BROWN, Color.PINK, Color.CYAN, Color.CYAN, Color.CYAN]

    number_of_attempts = 1

    result, currentAttempts, status = play(selected_colors, user_provided_colors, number_of_attempts)

    self.assertEqual((result, currentAttempts, status),
      (Result.LOST, number_of_attempts + 1, {Match.EXACT: 0, Match.PRESENT: 0, Match.NO_MATCH: 6}))
    
  def test_play_first_attempt_some_exact_and_some_nonexact_match(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.PURPLE, Color.CYAN]

    number_of_attempts = 1

    result, currentAttempts, status = play(selected_colors, user_provided_colors, number_of_attempts)

    self.assertEqual((result, currentAttempts, status),
      (Result.LOST, number_of_attempts + 1, {Match.EXACT: 3, Match.PRESENT: 2, Match.NO_MATCH: 1}))

  def test_play_second_attempt_with_exact_match(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]

    number_of_attempts = 2

    result, currentAttempts, status = play(selected_colors, user_provided_colors, number_of_attempts)

    self.assertEqual((result, currentAttempts, status),
      (Result.WON, number_of_attempts + 1, {Match.EXACT: 6, Match.PRESENT: 0, Match.NO_MATCH: 0}))

  def test_play_second_attempt_with_no_match(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.WHITE, Color.BROWN, Color.PINK, Color.CYAN, Color.CYAN, Color.CYAN]

    number_of_attempts = 2

    result, currentAttempts, status = play(selected_colors, user_provided_colors, number_of_attempts)

    self.assertEqual((result, currentAttempts, status),
      (Result.LOST, number_of_attempts + 1, {Match.EXACT: 0, Match.PRESENT: 0, Match.NO_MATCH: 6}))

  def test_play_twenty_attempt_with_exact_match(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]

    number_of_attempts = 20

    result, currentAttempts, status = play(selected_colors, user_provided_colors, number_of_attempts)

    self.assertEqual((result, currentAttempts, status),
      (Result.WON, number_of_attempts + 1, {Match.EXACT: 6, Match.PRESENT: 0, Match.NO_MATCH: 0}))
  
  def test_play_twenty_attempt_with_no_match(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.WHITE, Color.BROWN, Color.PINK, Color.CYAN, Color.CYAN, Color.CYAN]

    number_of_attempts = 20

    result, currentAttempts, status = play(selected_colors, user_provided_colors, number_of_attempts)

    self.assertEqual((result, currentAttempts, status),
      (Result.LOST, number_of_attempts + 1, {Match.EXACT: 0, Match.PRESENT: 0, Match.NO_MATCH: 6}))
    
  def test_play_twentyfirst_attempt_with_exact_match(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]

    number_of_attempts = 21

    with self.assertRaisesRegex(Exception, "Result.GAME_OVER"):
      play(selected_colors, user_provided_colors, number_of_attempts)
    
  def test_play_twentyfirst_attempt_with_no_match(self):
    selected_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PURPLE, Color.ORANGE]
    user_provided_colors = [Color.WHITE, Color.BROWN, Color.PINK, Color.CYAN, Color.CYAN, Color.CYAN]

    number_of_attempts = 21

    with self.assertRaisesRegex(Exception, "Result.GAME_OVER"):
      play(selected_colors, user_provided_colors, number_of_attempts)
     
  def test_randomize_selected_colors(self):
    EXPECTED_SIZE = 6
    selected_colors = select_colors()

    self.assertEqual(EXPECTED_SIZE, len(selected_colors))

    self.assertTrue(all(color in list(Color) for color in selected_colors))

  def test_selected_colors_different_when_called_twice(self):
    selected_colors_first_call = select_colors()
    selected_colors_second_call = select_colors()

    self.assertNotEqual(selected_colors_first_call, selected_colors_second_call)
    
if __name__ == '__main__': 
  unittest.main()
