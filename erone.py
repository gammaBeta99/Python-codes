'''
Calcolo dell'area di un triangolo usando la formula di Erone di Alessandria.
Il programma controlla la terna inserita e ti fornisce infinite possibilità
di errore: non calcola l'are fin quand la terna inserita non corrisponde 
a un triangolo matematicamente esistente.
'''

from math import sqrt 

#primo inserimento dei lati 

l_1 = float (input ("Inserisci il primo lato:"))
l_2 = float (input ("Inserisci il secondo lato:"))
l_3 = float (input ("Inserisci il terzo lato:")) 

#contollo della terna con possibilità di riscatto

while (not ((l_3 < l_1 + l_2) and (l_1 < l_2 + l_3 ) and (l_2 < l_1 + l_3))) :
    print ("Il triangolo non esiste")
    print ("Inserire nuovi lati")
    l_1 = float (input ("Inserisci il primo lato:"))
    l_2 = float (input ("Inserisci il secondo lato:"))
    l_3 = float (input ("Inserisci il terzo lato:")) 

p = (l_1 + l_2 + l_3) / 2 #p è il semiperimetro

area = sqrt (p * (p - l_1) * (p - l_2) * (p - l_3)) #area secondo la frmula di Erone

print (area)


