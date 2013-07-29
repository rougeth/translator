'''
translator.Translator
~~~~~~~~~~~~~~~~~~~~~

description...
'''

import requests


class Translator:

    URL = 'http://translate.google.com/translate_a/t'

    PARAMS = {
        'client': 'j',
        'text': None,
        'sl': 'en',
        'tl': 'pt'
    }

    HEADERS = {
        'Accept-language': 'pt',
        'Content-Type': 'text/javascript; charset=UTF-8'
    }

    def __init__(self, word, targe_language=None, source_word=None):

        self.PARAMS['text'] = word

        if source_word:
            self.PARAMS['sl'] = source_word

        if targe_language:
            self.PARAMS['tl'] = targe_language


    def request(self):

        req = requests.get(
            url=self.URL,
            params=self.PARAMS,
            headers=self.HEADERS
        )

        return req.json()
