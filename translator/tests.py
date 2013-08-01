import unittest

class Translator(unittest.TestCase):

    def setUp(self):
        ''' Função antes de cada teste '''
        from core import Translator
        self.t = Translator('tests')

    def tearDown(self):
        ''' Função executada depois de cada teste '''
        pass

    def test_source_language(self):
        ''' Testa se a função source_language() altera a variável params['sl']
        '''

        self.t.source_language('af')

        self.assertEqual(
            self.t.params['sl'],
            'af'
        )

    def test_target_language(self):
        ''' Testa se a função target_language() altera a variável params['tl']
        '''

        self.t.target_language('af')

        self.assertEqual(
            self.t.params['tl'],
            'af'
        )


if __name__ == '__main__':
    unittest.main()
