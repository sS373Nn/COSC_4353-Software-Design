def character_blocker(blocked_char):
    return lambda text: text.replace(blocked_char, "")
