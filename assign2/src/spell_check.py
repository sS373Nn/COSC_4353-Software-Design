import requests

def get_response(word):
    return requests.get(f"https://agiledeveloper.com/spellcheck?check={word}").text.strip()
    
def parseresponse(response):
    return response == "true"

def is_spelling_correct(word, get_response=get_response, parse_response=parseresponse):
    try:
        return parse_response(get_response(word))
    
    except Exception as exception:
        return exception
