import unittest

class Translator(unittest.TestCase):

    def setUp(self):

        from core import Translator
        self.t = Translator('tests')

    def tearDown(self):
        pass

    def test_source_language(self):

        self.t.source_language('af')

        self.assertEqual(
            self.t.params['sl'],
            'af'
        )

    def test_target_language(self):

        self.t.target_language('af')

        self.assertEqual(
            self.t.params['tl'],
            'af'
        )


if __name__ == '__main__':
    unittest.main()
