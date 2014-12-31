#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ce script permet d'encoder un nombre selon le codage de Fibonacci (http://fr.wikipedia.org/wiki/Codage_de_Fibonacci)
# A venir : encodage de fichiers entiers !!!!!!!!!! (et éventuellement de quoi les décoder, ça peut être utile tiens)

def fibo(num):
	#retourne la liste des termes de la suite de Fibonacci inférieurs à num
	a, b = 1, 1
	termes = []
	while b < num:
		termes.append(b)
		a, b = b, b + a
	return termes
	
def encode(n):
	termes = fibo(n)
	valeurEncodee = "1"
	for i in reversed(termes):
		if n >= i:
			n = n - i
			valeurEncodee = "1" + valeurEncodee
		else:
			valeurEncodee = "0" + valeurEncodee
	return valeurEncodee
		
print(encode(50))