import numpy as np
import random

def gauss_0 (x) :
    #0.3989422 approssimazione per 1 / sqrt (2 * pi)
    return 0.3989422 * np.exp (-0.5 * x**2) 

def KDE (x, sample, func, h = 1) :
    if h <= 0. : return 0.
    result = 0.
    for elem in sample :
        result += func ((x - elem) / h)
    result /= (h * len (sample))
    return result
    
def rand_range (xMin, xMax) :
    return float (xMin + (xMax - xMin) * random.random())

def unif (xMin, xMax) :
    yMax = 1. / (xMax - xMin)
    x = rand_range (xMin, xMax)
    y = rand_range (0., yMax)
    while (y > yMax) :
        x = rand_range (xMin, xMax)
        y = rand_range (0., yMax)
    return x

def generate_uniform (xMin, xMax, N, seed = 0.) :
    if seed != 0. : random.seed (float (seed))
    randlist = []
    for i in range (N) :
        randlist.append (unif (xMin, xMax))
    return randlist
    
def parabola (x) :
    if abs (x) < 1. : return 0.75 * (1 - x**2)
    return 0.

def sezioneAureaMin (
    g,              # funzione di cui trovare lo zero
    x0,             # estremo dell'intervallo          
    x1,             # altro estremo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola estremanti
    con il metodo della sezione aurea
    '''

    r = 0.618
    x2 = 0.
    x3 = 0. 
    larghezza = abs (x1 - x0)
     
    while (larghezza > prec):
        x2 = x0 + r * (x1 - x0) 
        x3 = x0 + (1. - r) * (x1 - x0)  
      
        # si restringe l'intervallo tenendo fisso uno dei due estremi e spostando l'altro        
        if (g (x3) > g (x2)): 
            x0 = x3
                   
        else :
            x1 = x2
             
            
        larghezza = abs (x1-x0)             
                                   
    return (x0 + x1) / 2. 

def loglikelihood_kernel (sample, kernel = gauss_0, h = 1) :
    loglike = 0.
    for i, xi in enumerate (sample) :
        newsample = sample [0:i] + sample [i+1:]
        loglike += np.log (KDE (xi, sample, kernel, h))
    return loglike

def calcola_scarti (func, sample_x, sample_y) :
    scarti = []
    for x_i, y_i in zip (sample_x, sample_y):
        scarti.append (func (x_i) - y_i)
    return scarti

def gauss_2D_new (mean_x, sigma_x, mean_y, sigma_y, N) :
    x_coord = generate_TCL_ms (mean_x, sigma_x, N)
    y_coord = generate_TCL_ms (mean_y, sigma_y, N)
    return x_coord, y_coord