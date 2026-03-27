import sys
from math import sqrt

#inserimento dei lati

lati = []
lati.append (float (input ('inserisci il primo lato: ')))
lati.append (float (input ('inserisci il secondo lato: ')))
lati.append (float (input ('inserisci il terzo lato: ')))
lati.sort ()
print ('I lati inseriti sono: ')
print (lati)
    
#controllo esistenza del triangolo 
    
if (lati[0] < lati[1] + lati[2]) and (lati[1] < lati[0] + lati[2]) and ( lati[2] < lati[0] + lati [1]) :
    print ('il triangolo esiste') 
else : sys.exit('il triangolo non esiste') 

#calcolo del perimetro

var_2p = sum (lati)
print ('Perimetro:', var_2p)

#calcolo del semiperimetro

var_p = 0.5 * (sum (lati))

#calcolo dell'area del triangolo con la formula di erone
area = sqrt (var_p * (var_p - lati[0]) * (var_p - lati[1]) * (var_p - lati[2]))
print ('Area calcolata con la formula di Erone:', area)