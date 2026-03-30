import random

def rand_range (xMin, xMax) :
  return xMin + (xMax - xMin) * random.random() 

"""
funzione rudimentale per stimare pi greco
basata sulla generazione di numeri pseudo-casuali 
""" 
def calc_pi (Ngen) :
  Ninside = 0
  x = rand_range (0., 1.) 
  y = rand_range (0., 1.)
  for i in range (Ngen) :
    x = rand_range (0., 1.) 
    y = rand_range (0., 1.)
    if (x**2 + y**2 < 1) :
      Ninside += 1

return 4. * (Ninside / Ngen)
