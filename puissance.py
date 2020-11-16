#!/usr/bin/python3
#coding: utf-8


try:
  x = int(input("Quel est le nombre de base : "))
  y = int(input("Quelle est la puissance : "))
  i = 1
  cumul = x
  while (i < y):
    cumul = cumul * x
    i += 1
print (x, "^", y, "= "+str(cumul))
except:
  print("Veuillez saisir un nombre.")


--------------------------------------------------------------------- Résultat --------------------------------------------------------------------------------
Quel est le nombre de base : 10
Quelle est la puissance : 3
10 ^ 3 = 1000