from enum import Enum

class Match(Enum):
    EXACT = "exact match" 
    PRESENT = "Non Positional Match"
    NO_MATCH = "Not Found"
    