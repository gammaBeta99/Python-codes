import sys

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

#determinare il tipo di triangolo tra ottusangolo, acutangolo, rettangolo

if (lati[0]**2 + lati[1]**2 < lati[2]**2)    : print ('triangolo ottusangolo')
elif (lati[0]**2 + lati[1]**2 > lati[2]**2)  : print ('triangolo acutangolo') 
else                                         : print ('triangolo rettangolo')   
