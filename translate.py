# -*- coding: utf-8 -*-

import http.client
import sys

#Função apenas para identar e facilitar leituda da string retornada pelo site.
def ident_str(id_str):
	counter = 0

	for a_char in id_str:
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

#A partir de position, pega tudo o que estiver antes do "]"
def get_str(my_str, position):
	ret_str = ""

	for i in range (position, len(my_str)):
		if my_str[i] == "]":
			return ret_str
		else:
			ret_str = ret_str + my_str[i]


#Função retorna uma string dos possíveis Resultados. Recebe a string, e o item desejado (substantivo, pronome, adjetivo, artigo, ...)
def result_str(my_str, item):
	index = my_str.find(item)
	if index == -1:
		return None

	for i in range(index, len(my_str)):
		if my_str[i] == "[":
			return get_str(my_str, i + 1)

#my_str = '''[[["teste","test","",""]],[["substantivo",["teste","ensaio","prova","exame","análise","experiência","verificação","padrão","bitola","craveira","pedra-de-toque"],[["teste",["test","assay","audition","try","try-out"],,0.39777252],["ensaio",["test","assay","testing","trial","essay","rehearsal"],,0.093014486],["prova",["proof","evidence","test","trial","testing","competition"],,0.023153137],["exame",["examination","exam","test","review","survey","inspection"],,0.015423315],["análise",["analysis","review","parsing","test","assay","decomposition"],,0.0034414066],["experiência",["experience","experiment","background","trial","test","experimentation"],,0.00074425637],["verificação",["verification","examination","inspection","test","proofing","proof"],,0.00057962746],["padrão",["standard","pattern","model","template","type","test"],,6.0145136e-05],["bitola",["gauge","gage","diameter","test","scantling"],,2.2959243e-06],["craveira",["standard","test"],,8.7143462e-07],["pedra-de-toque",["touchstone","shibboleth","test"],,4.247033e-07]]],["verbo",["ensaiar","verificar","experimentar","provar","examinar","pôr à prova","submeter a teste","analisar com reagente"],[["ensaiar",["test","rehearse","try","assay","experiment","essay"],,0.00062672672],["verificar",["check","verify","see","ascertain","find","test"],,0.00013136906],["experimentar",["experience","try","experiment","try out","sample","test"],,8.4818232e-05],["provar",["prove","taste","sample","show","evidence","test"],,7.1424118e-05],["examinar",["examine","look","scan","check","explore","test"],,4.5399931e-05],["pôr à prova",["test","prove","proof","tax","tempt","match"],,6.8543641e-06],["submeter a teste",["test"],,2.9944499e-06],["analisar com reagente",["test"],,8.990969e-07]]]],"en",,[["teste",[5],1,0,1000,0,1,0]],[["test",4,,,""],["test",5,[["teste",1000,1,0],["ensaio",0,1,0],["teste de",0,1,0],["de teste",0,1,0],["de ensaio",0,1,0]],[[0,4]],"test"]],,,[["en"]],34]'''
#ident_str (my_str)

#Tratando entrada de dados
if len(sys.argv) < 2:
	print ("Uso: translate [palavra em inglês]")
	sys.exit()

if sys.argv[1].find(" ") != -1 or len(sys.argv) > 2:
	print("Escreva apenas uma palavra para tradução...")
	sys.exit()

#Url de requisição HTTP
word = sys.argv[1]
url = "http://translate.google.com/translate_a/t?client=t&text=" + word + "&sl=en&tl=pt"

conn = http.client.HTTPConnection("www.translate.google.com")
conn.request("GET", url)

r1 = conn.getresponse()

#Obtém a string que será processada para apresentação das traduções
my_str = r1.read()

#fecha conexão
conn.close()

my_str = str(my_str)
my_str = repr(my_str)

#Dicionário representando a classificação das palavras e sua tradução.
classes = {"noun":"substantivo", "verb":"verbo", "pronoun":"pronome", "adjective":"adjetivo", "article":"artigo"}

#Percorre as classes de palavras e mostrando a tradução daquelas
#classes que estão contidas na string de retorno
for my_class in classes:
	result = result_str(my_str, my_class)
	if result != None:
		print (classes[my_class], ":")
		print (result)
		print ("")