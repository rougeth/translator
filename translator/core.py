'''
translator.Translator
---------------------

Módulo básico utilizado na tradução
'''

from packages import requests
from packages.clint.textui import colored


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

    REQ = None
    DICT = {}

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

        self.REQ = req.json()

    def organize_dict(self):

        '''
        {
            orig: original word
            trans: translated word
            classes: [
                {
                    class: name of the class
                    terms: all terms
                }
                {
                    class: name of the class
                    terms: all terms
                }
                ...
            ]
        }
        '''
        r = self.REQ

        dictionary = {}
        dictionary['orig'] = r['sentences'][0]['orig']
        dictionary['trans'] = r['sentences'][0]['trans']
        dictionary['classes'] = []

        for _class in r['dict']:
            dictionary['classes'].append({
                'name': _class['pos'],
                'terms': _class['terms'][:5]
            })
        return dictionary

    def show(self, detailed=False):

        self.request()

        d = self.organize_dict()

        # Translation
        print('{0}: {1}'.format(
            colored.white(self.PARAMS['tl']),
            colored.red(d['trans'])
        ))

        # More information about the word translated
        if detailed:
            print('{0}: {1}'.format(
                colored.white(self.PARAMS['sl']),
                d['orig']
            ))
            print()
            for _class in d['classes']:
                print('{0}: {1}'.format(
                    colored.white(_class['name']),
                    ', '.join([word for word in _class['terms']])
                ))

        print()
