import random
import os

from src.match import Match
from src.result import Result
from src.color import Color
from collections import Counter


EXACT = Match.EXACT
PRESENT = Match.PRESENT
NO_MATCH = Match.NO_MATCH

def guess(selected_colors, user_provided_colors):
    size = len(selected_colors)

    def match_for_position(position):
      candicate_color = user_provided_colors[position]

      if candicate_color == selected_colors[position]:
        return EXACT

      if candicate_color in user_provided_colors[0:position]:
        return NO_MATCH

      index = selected_colors.index(candicate_color) if candicate_color in selected_colors else -1
      
      if index > -1 and selected_colors[index] != user_provided_colors[index]:
        return PRESENT
  
      return NO_MATCH

    return {**{EXACT: 0, PRESENT: 0, NO_MATCH: 0}, **Counter(map(match_for_position, range(0, size)))}

def play(selected_colors, user_provided_colors, number_of_attempts):
    response = guess(selected_colors, user_provided_colors)
    MAX_ATTEMPTS = 20
    result = Result.LOST

    if number_of_attempts > MAX_ATTEMPTS:
       raise Exception(Result.GAME_OVER)

    if response[Match.EXACT] == 6:
       result = Result.WON

    return result, number_of_attempts+1, response
    
def select_colors():
   random.seed(int.from_bytes(os.urandom(8), 'big'))
   AMOUNT_OF_COLORS_NEEDED = 6
   SELECTED_COLORS = random.sample(list(Color), AMOUNT_OF_COLORS_NEEDED)
   return SELECTED_COLORS
