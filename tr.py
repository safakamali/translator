# Importing ...
from requests import get
from termcolor import colored
from pyperclip import copy

import sys


def translate(text, lang):  # use to send translation request
    try:
        url = f"https://one-api.ir/translate/?token=501896:623851760ca2a2.97528414&action=google&lang={lang}&q={text}"
        data = get(url).json()
        return data
    except:
        return colored('error in connection!', 'red')


def app():
    do_copy = False

    # give translate text and translate language ...
    args_t = sys.argv
    args_t.pop(0)

    if "-" in args_t[-1]: # check if last argument is a switch
        switch = args_t.pop(-1)
        if switch == "-help":
            print("""
            usage:
            tr.py [text] [language] [switch]
            -h: help
            -copy: copy to clipboard

            example:
            tr.py hello world en
            tr.py hello world fr -copy
            """)
            return 1
        elif switch == "-copy":
            do_copy = True
        elif switch == 'c':
            do_copy = True
        else: # if switch is not valid
            print(
                colored(f'error in usage! Unknown switch {switch}', 'red'))
            return 0

    lang = args_t.pop() # get language
    text = " ".join(args_t) # get text

    translate_response = translate(text, lang)  # send translate request

    # Check for no errors (if translate_response type = string (error in connection): connection was disrupted )
    if type(translate_response) == dict:
        translate_response_text = colored(
            translate_response['result'], 'cyan')  # make colored text
        if do_copy:
            copy(translate_response['result'])
        print(  # print the response
            f"""
    status: {translate_response['status']}
    result:
    {translate_response_text}"""
        )
    else:
        print(translate_response)  # error in connection


if __name__ == '__main__':  # run program when run type is main
    app()
