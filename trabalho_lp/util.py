# -*- coding: iso8859-1 -*-
"""
Created on Fri May 30 11:31:20 2014

@author: i13129
"""

import pickle

def ler_ficheiro(ficheiro):
	lista = []
	try:
		f = open(ficheiro, "rb")
		lista = pickle.load(f)		
		f.close
	except:
		print "Ficheiro %s não existe!" % (ficheiro)

	return lista


def escrever_ficheiro(ficheiro, lista):
	try:
		f = open(ficheiro, "wb")
		pickle.dump(lista, f)		
		f.close
		print "Escrevi ficheiro %s" % (ficheiro)
	except:
		print "Erro a gravar ficheiro %s!" % (ficheiro)