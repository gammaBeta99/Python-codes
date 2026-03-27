import random
import numpy as np
'''
questo file contiene tutte (o quasi) le
funzioni per generare numeri pseudo-casuali
'''
def generate_uniform (N, seed = 0.) :
    '''genera N numeri pseudo-casuali 
       tra 0 e 1 a partire da un seed
    '''
    if seed != 0. : random.seed (float (seed))
    randlist = []
    for i in range (N) :
        randlist.append (random.random()) 
        
    return randlist
    
'randmom.random () genera un numero pseudo-casuale tra 0 e 1'

def rand_range (xMin, xMax) :
    return xMin + (xMax - xMin) * random.random()

def generate_range (xMin, xMax, N, seed = 0.) :
    '''genera N numeri pseudo-casuali 
       tra xMin e xMax a partire da un seed noto
    '''   
    if seed != 0. : random.seed (float (seed))
    randlist = []
    for i in range (N) :
        randlist.append (rand_range (xMin, xMax)) 
    
    return randlist

def rand_TAC (f, xMin, xMax, yMax) :
    '''genera un numero pseudo-casuale 
       con il metodo try and catch
    '''
    x = rand_range (xMin, xMax)
    y = rand_range (0, yMax)
    while (y > f (x)) :
        x = rand_range (xMin, xMax)
        y = rand_range (0, yMax)

    return x

def generate_TAC (f, xMin, xMax, yMax, N, seed = 0.) :
    '''genera N numeri pseudo-casuali 
       con il metodo try and catch
    '''   
    if seed != 0. : random.seed (float (seed))
    randlist = []
    for i in range (N) :
        randlist.append (rand_TAC (f, xMin, xMax, yMax))

    return randlist

def rand_TCL (xMin, xMax, N_sum = 10) :
    '''genera un numero pseudo-casuale con il metodo
       del teorema cenrtrale del limite su un intervallo fissato
    '''
    y = 0.
    for i in range (N_sum) :
        y = y + rand_range (xMin, xMax)
    y /= N_sum

    return y

def generate_TCL (xMin, xMax, N, N_sum = 10, seed = 0.) :
    '''generazione di N numeri pseudo-casuali con il
       metodo del teorema centrale del limite
    '''
    if seed != 0. : random.seed (float (seed))
    randlist = []
    for i in range (N) :
        randlist.append (rand_TCL (xMin, xMax, N_sum))

    return randlist

def rand_TCL_ms (mean, sigma, N_sum = 10) :
    '''genera un numero pseudo-casuale con il metodo
       del teorema cenrtrale del limite su un intervallo fissato
       note mu e sigma della gaussiana
    '''
    y = 0.
    delta = np.sqrt (3. * N_sum) * sigma
    xMin = mean - delta
    xMax = mean + delta
    
    for i in range (N_sum) :
        y = y + rand_range (xMin, xMax)
    y /= N_sum

    return float (y)

def generate_TCL_ms (mean, sigma, N, N_sum = 10, seed = 0.) :
    '''
    genera N numeri psudo-casuali secondo il teorema centrale del limite
    note mu e sigma della gaussiana
    '''
    if seed != 0. : random.seed (float (seed))
    randlist = [] 
    for i in range (N) :
        randlist.append (rand_TCL_ms (mean, sigma, N_sum))

    return randlist

def rand_range_2D (center, delta) :
    '''
    funziona con i vettori di numpy np.arrays
    '''
    return np.array ([
        rand_range (center[0]-delta[0], center[0]+delta[0]),
        rand_range (center[1]-delta[1], center[1]+delta[1])
    ])

