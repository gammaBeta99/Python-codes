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
