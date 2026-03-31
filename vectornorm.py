"""
programma che calcola la norma di un vettore:
l'utente deve inserire la dimensione del vettore e le N coordinate
"""
import numpy as np
import random
#from math import sqrt

"""
versione con array python 
"""
#dim = 3 

dim = int (input ("Inserisci la dimensione del vettore"))
vector = []
vectorsquare = []

for i in range (dim) :
    norma = 0.
    elem = float (input ("Inserisci una coordinata:"))
    vector.append (elem)
    vectorsquare.append (elem**2)
    norma = np.sqrt (sum (vectorsquare))

print ("Il tuo vettore è:\n", vector, "\ne ha norma:\n", norma)

"""
versione con array di NumPy 
"""
#dim = 3 

dim = int (input ("Inserisci la dimensione del vettore"))
vector = np.zeros (dim)
vectorsquare = np.zeros (dim)

for i in range (dim) :
    norma = 0.
    elem = float (input ("Inserisci una coordinata:"))
    vector[i] = elem 
    vectorsquare[i] = elem**2
       
norma = np.sqrt (sum (vectorsquare))

print ("Il tuo vettore è:\n", vector, "\ne ha norma:\n", norma)
    