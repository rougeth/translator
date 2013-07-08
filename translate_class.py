# -*- coding: utf-8 -*-

import http.client
import sys

class Translate:
    # This dictionary contains the word class translations
    classes = {"interjection":"interjeição" ,"noun":"substantivo", "verb":"verbo", "pronoun":"pronome", "adjective":"adjetivo", "article":"artigo"}
    # The string will contain the return from the http request
    http_returned_string = ""

    def show_ident_str(self):
        """
        This is a helper funtion for reading the huge 
        string returned by the http query.
        """
        counter = 0

        for a_char in self.http_returned_string:
            if a_char == "[":
                print ("")
                print ("\t" * counter, a_char, end = "")
                counter = counter + 1
                print ("")
                print ("\t" * counter, end = "")

            elif a_char == "]":
                print ("")
                counter = counter - 1
                print ("\t" * counter, a_char, end = "")
                print ("")
                print ("\t" * counter, end = "")

            else:
                print (a_char, end = "")

        print ("\n")

    def get_class_translations(word_class):
        """
        This function returns the translated words
        for a given class as a string of separated words
        Call this function after making the internet request
        @word_class -> one of the <classes> dictionary keys
        """

        index = self.http_returned_string.find(word_class)
        ret_str = ""

        if index == -1:
            return None

        for i in range(index, len(self.http_returned_string)):
            if self.http_returned_string[i] == "[":
                for j in range (i + 1, len(self.http_returned_string)):
                    if self.http_returned_string[j] == "]":
                        return ret_str
                    else:
                        ret_str = ret_str + self.http_returned_string[j]

    # It's an example of a string returned by the http request
    # http_returned_string = '''[[["teste","test","",""]],[["substantivo",["teste","ensaio","prova","exame","análise","experiência","verificação","padrão","bitola","craveira","pedra-de-toque"],[["teste",["test","assay","audition","try","try-out"],,0.39777252],["ensaio",["test","assay","testing","trial","essay","rehearsal"],,0.093014486],["prova",["proof","evidence","test","trial","testing","competition"],,0.023153137],["exame",["examination","exam","test","review","survey","inspection"],,0.015423315],["análise",["analysis","review","parsing","test","assay","decomposition"],,0.0034414066],["experiência",["experience","experiment","background","trial","test","experimentation"],,0.00074425637],["verificação",["verification","examination","inspection","test","proofing","proof"],,0.00057962746],["padrão",["standard","pattern","model","template","type","test"],,6.0145136e-05],["bitola",["gauge","gage","diameter","test","scantling"],,2.2959243e-06],["craveira",["standard","test"],,8.7143462e-07],["pedra-de-toque",["touchstone","shibboleth","test"],,4.247033e-07]]],["verbo",["ensaiar","verificar","experimentar","provar","examinar","pôr à prova","submeter a teste","analisar com reagente"],[["ensaiar",["test","rehearse","try","assay","experiment","essay"],,0.00062672672],["verificar",["check","verify","see","ascertain","find","test"],,0.00013136906],["experimentar",["experience","try","experiment","try out","sample","test"],,8.4818232e-05],["provar",["prove","taste","sample","show","evidence","test"],,7.1424118e-05],["examinar",["examine","look","scan","check","explore","test"],,4.5399931e-05],["pôr à prova",["test","prove","proof","tax","tempt","match"],,6.8543641e-06],["submeter a teste",["test"],,2.9944499e-06],["analisar com reagente",["test"],,8.990969e-07]]]],"en",,[["teste",[5],1,0,1000,0,1,0]],[["test",4,,,""],["test",5,[["teste",1000,1,0],["ensaio",0,1,0],["teste de",0,1,0],["de teste",0,1,0],["de ensaio",0,1,0]],[[0,4]],"test"]],,,[["en"]],34]'''

    def make_request(word):
        """
        Make a request to translate.google.com and get the
        translated results
        @word -> the word to translate
        """

        # Request url
        word = sys.argv[1]
        url = "http://translate.google.com/translate_a/t?client=t&text=" + word + "&sl=en&tl=pt"

        conn = http.client.HTTPConnection("www.translate.google.com")
        conn.request("GET", url)

        r1 = conn.getresponse()

        # Get the answer string
        self.http_returned_string = r1.read()

        # Close the connection
        conn.close()

        # Deal with character encoding returned from the request
        self.http_returned_string = str(self.http_returned_string , 'latin-1')

    def print_all_translated_classes():
        """
        Run through the word classes printing the translations for each possible kind
        """

        for curr_class in self.classes:
            result = get_class_translations(self.http_returned_string, curr_class)
            if result != None:
                print (self.classes[curr_class], ":")
                print (result)
                print ("")
