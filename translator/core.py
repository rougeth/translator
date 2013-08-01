class Translator:

    def __init__(self, word):

        # Línguas suportadas pelo Google Translate
        self.supported_languages = (
            ('af', 'africâner'),
            ('sq', 'albanês'),
            ('de', 'alemão'),
            ('ar', 'árabe'),
            ('hy', 'armênio'),
            ('az', 'arzebaijano'),
            ('eu', 'basco'),
            ('bn', 'bengale'),
            ('be', 'bielo-russo'),
            ('bs', 'bósnio'),
            ('bg', 'búlgaro'),
            ('ca', 'catalão'),
            ('ceb', 'cebuano'),
            ('zh-CN', 'chinês (simplificado)'),
            ('zh-TW', 'chinês (tradicional)'),
            ('ko', 'koreano'),
            ('en', 'inglês'),
            ('pt', 'português')
            # completar a lista
        )

        self.url = 'http://translate.google.com/translate_a/t'

        self.params = {
            'client': 'j',
            'text': word,
            'sl': 'en',
            'tl': 'pt'
        }

        self.headers = {
            'Accept-language': 'pt',
            'Content-Type': 'text/javascript; charset=UTF-8'
        }

    def source_language(self, sl):
        ''' Muda língua de origem da palavra '''

        for language in self.supported_languages:
            if sl in language:
                self.params['sl'] = sl
                return True

        return False

    def target_language(self, tl):
        ''' Muda língua em que a palavra será traduzida '''

        for language in self.supported_languages:
            if tl in language:
                self.params['tl'] = tl
                return True

        return False

    def request(self):
        pass

    def orig_word(self):
        pass

    def trans_word(self):
        pass

    def classes_word(self):
        pass
