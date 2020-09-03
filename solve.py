#!/usr/bin/python3

import random

"""
by Gabriel Andrada @ Iset55 

  GALOIS
+ PASCAL
--------
 LAPLACE

"""

while(1):
  dataset = [0,1,2,3,4,5,6,7,8,9]

  l = dataset[1]
  dataset.remove(l)

  g = dataset[random.randint(0,len(dataset)-1)]
  dataset.remove(g)

  a = dataset[random.randint(0,len(dataset)-1)]
  dataset.remove(a)

  o = dataset[random.randint(0,len(dataset)-1)]
  dataset.remove(o)

  i = dataset[random.randint(0,len(dataset)-1)]
  dataset.remove(i)

  s = dataset[random.randint(0,len(dataset)-1)]
  dataset.remove(s)

  p = dataset[random.randint(0,len(dataset)-1)]
  dataset.remove(p)

  c = dataset[random.randint(0,len(dataset)-1)]
  dataset.remove(c)

  e = dataset[random.randint(0,len(dataset)-1)]
  dataset.remove(e)

  galois = ("{}{}{}{}{}{}".format(g,a,l,o,i,s))
  pascal = ("{}{}{}{}{}{}".format(p,a,s,c,a,l))
  laplace = ("{}{}{}{}{}{}{}".format(l,a,p,l,a,c,e))

  if (int(galois) + int(pascal) == int(laplace)):
    print("---------- ENCONTRADO!!! -----------")
    print("galois = ",galois)
    print("pascal = ",pascal)
    print("laplace = ",laplace)
    break
  else:
    print("[X] Fuck!")
