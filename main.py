#!/usr/bin/python3

import sys
import translate

# Handling data input
if len(sys.argv) < 2:
    print ("Usage: translate <english-word>")
    sys.exit()

if sys.argv[1].find(" ") != -1 or len(sys.argv) > 2:
    print ("Usage: translate <english-word>")
    sys.exit()

trl = translate.GoogleTranslate()
trl.make_request(sys.argv[1])
trl.print_all_translated_classes()
