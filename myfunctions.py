#inserisco qui le funzioni che mi serviranno 
import random
import numpy as np

def phi (x, theta_a, theta_b, theta_c) :
    return theta_a*x**2 + theta_b*x + theta_c

#funzione di calibrazione phi (V)

def model_para (x, a, b, c) :
    return a*x**2 + b*x + c

def rand_range (xMin, xMax) :
    return xMin + (xMax - xMin) * random.random()

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


def sturges (N_events) :
     return int(np.ceil( 1 + np.log2(N_events)))

#funzionale phi cappuccio, phi_hat

def phi_hat (Qs_1, Qs_2, par_1, par_2, n = 5) :
    norm = (n - par_2) / (par_2 - par_1)
    return norm * (Qs_1 - Qs_2) / (Qs_2)
    
#le variabili Qs_i indicano i valori dei Q^2