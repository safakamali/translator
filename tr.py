# Importing ...
from requests import get
from termcolor import colored
import sys

def translate(text, lang): # use to send translation request
    try:
        url = f"https://one-api.ir/translate/?token=501896:623851760ca2a2.97528414&action=google&lang={lang}&q={text}"
        data = get(url).json()
        return data
    except:
        return colored('error in connection!', 'red')

if __name__ == '__main__': # run program when run type is main

    # givv translate text and translate language ...
    args_t = sys.argv
    args_t.pop(0)
    lang = args_t.pop()
    text = " ".join(args_t)

    translate_response = translate(text, lang) # send translate request

    if type(translate_response) == dict: # Check for no errors (if translate_response type = string (error in connection): connection was disrupted )
        translate_response_text = colored(translate_response['result'], 'cyan') # make colored text
        print( # print the response
        f"""
    status: {translate_response['status']}
    result:
    {translate_response_text}"""
        )
    else:
        print(translate_response) # error in connection