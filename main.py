#!/usr/bin/python3

import argparse
from translator import Translator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('word',
        action='store',
        help="word that will be translated"
    )
    parser.add_argument('-d', '--details',
        action='store_true',
        help='show detailed information about the translation',
        default=False
    )

    params = parser.parse_args()

    word = params.word
    details = params.details

    t = Translator(word)
    t.show(details)
