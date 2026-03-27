from math import sqrt

lato_1 = float (input ("Inserisci il primo lato:"))
lato_2 = float (input ("Inserisci il secondo lato:"))
lato_3 = float (input ("Inserisci il terzo lato:")) 

while (not ((lato_3 < lato_1 + lato_2) and (lato_1 < lato_2 + lato_3 ) and (lato_2 < lato_1 + lato_3))) :
    print ("Il triangolo non esiste")
    print ("Inserire nuovi lati")
    lato_1 = float (input ("Inserisci il primo lato:"))
    lato_2 = float (input ("Inserisci il secondo lato:"))
    lato_3 = float (input ("Inserisci il terzo lato:")) 

semiperimetro = (lato_1 + lato_2 + lato_3) / 2

area = sqrt (semiperimetro * (semiperimetro - lato_1) * (semiperimetro - lato_2) * (semiperimetro - lato_3))

print (area)


