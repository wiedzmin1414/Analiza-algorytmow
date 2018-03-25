#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:23:26 2018

@author: lpolakiewicz
"""
import random

ddd = 2**31-1
eee = 16807
fff = 2**32
h31 = 2**31
h32 = 2**32

def multiset(n,m):
    r = [i % n for i in range(m)]
    for i in range(m):
        i = random.randint(0,m-1)
        j = random.randint(0,m-1)
        r[i], r[j] = r[j],r[i]
    return r

def haa(seed,ile):
    r = [seed]
    for i in range(30):
        seed = eee*seed % ddd
        r.append(seed)
    for i in range(3):
        r.append( r[i] )
    for i in range(310+ile):
        r.append( (r[i+31] + r[i+3]) % fff)
    return r[344:]
    #return [i>>1 for i in r[344:] ]

ziarno = 5
tab = haa(ziarno,33)

llll = h31 - 1
def h(i):
    #r =[i for i in tab ]
    if( i < len(tab )):
        return (tab[i] >>1) / h31
    else:
        for i in range(i-31):
            tab.append( (tab[-31] + tab[-3]) % fff)
    return (tab[-1]>>1) / llll
    
def kMn(k, ms):
    M = [1] * k
    for i in ms:
        zzz = h(i)
        if( zzz < M[-1] and zzz not in M):
            M[-1] = zzz
            M.sort()
    if ( M[-1] == 1):
        z = [i for i in M if i != 1]
        return len(z)
    else:
        return (k-1) / M[-1]
    
tabk = [ 2, 3, 10, 100, 400]
ile_k = len(tabk)
tabn = [i for i in range(1,10**4,10)]
estymacje = []
for i in tabk:
    estymacje.append([])
M = [1]
for n in tabn:
    est = []
    #M = [1]
    for k in tabk:
        #m = 3*n
        #M = multiset(n,m)
        est.append(kMn(k, M))
    x = len(M)
    for z in range(10):
        M.append(M[-1] + 1)
    M = [ l + x for l in M ]
    #print(k)
    for i in range(ile_k):
        estymacje[i].append(est[i]/n )


import matplotlib.pyplot as plt
import math as m
import random as r
import numpy as np


for i in range(ile_k):
    plt.plot(tabn,estymacje[i],'*')
    plt.show()

#for i in estymacje:
  #  plt.plot(tabn,i)
    
szukane_k = 1;
n = 100
w =  0.5
g = multiset(n,m)
while(w < 0.95):
    wyniki = []
    g = [i for i in range(n)]
    szukane_k += 1
    for i in range(100):
        #nnn = r.randint(1,10)
        g = [l + n for l in g]
        wyniki.append(kMn(szukane_k,g))
    w = len( [ i for i in wyniki if abs( i/n -1) < 0.1 ]) / 100
    #print(w)
    

    
