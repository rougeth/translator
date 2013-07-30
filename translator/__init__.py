'''
translator.Translator
---------------------

Módulo básico utilizado na tradução
'''

from translator.packages import *


class Translator:

    def __init__(self, word, source_word='en', targe_language='pt'):

        self.URL = 'http://translate.google.com/translate_a/t'

        self.PARAMS = {
            'client': 'j',
            'text': word,
            'sl': source_word,
            'tl': targe_language
        }

        self.HEADERS = {
            'Accept-language': 'pt',
            'Content-Type': 'text/javascript; charset=UTF-8'
        }

    def request(self):
        '''
        '''

        # Realiza uma requisição GET na url informada, passando os parâmetros e
        # cabeçalhos
        req = requests.get(
            url=self.URL,
            params=self.PARAMS,
            headers=self.HEADERS
        )

        # Transforma a string de retorn em formato json
        req_json = req.json()

        return self.organize_dict(req_json)

    def organize_dict(self, r):
        '''
        Função retorna um novo dicionário contendo apenas informações
        necessárias, como por exemplo:

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

        # Cria o dicionário que irá conter as informações filtradas da
        # requisição
        dictionary = {}

        dictionary['orig'] = r['sentences'][0]['orig']
        dictionary['trans'] = r['sentences'][0]['trans']

        # Para cada classe (artigo, substantivo, etc) adiciona o nome da classe
        # e seus termos em uma lista
        dictionary['classes'] = []

        for _class in r['dict']:
            dictionary['classes'].append({
                'name': _class['pos'],
                'terms': _class['terms'][:5]
            })

        return dictionary

    def show(self, detailed=False):

        d = self.request()

        # Imprime a tradução
        print('{0}: {1}'.format(
            colored.white(self.PARAMS['tl']),
            colored.red(d['trans'])
        ))

        # Caso solicitado, imprime mais informações
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
