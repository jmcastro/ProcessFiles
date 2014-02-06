# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:18:41 2013

@author: jmcastro
"""

import struct
import numpy as np
import time
import pandas as pd

'''
f = open("Node7.bin", "r")

a = np.fromfile(f, dtype=float, count=2)
#np.fromfile()
#b = np.fromfile(f, dtype=np.uint8, count=6)
print a

b = np.fromfile(f, dtype='|S1', count=1)

#print b

c = np.fromfile(f, dtype=float, count=2)
print c

d = np.fromfile(f, dtype='|S1', count=1)

#print d

e = np.fromfile(f, dtype=float, count=2)
print e

f.close()
'''

start = time.clock()

#dt = np.dtype([('time', float), ('value', float), ('bin', str)])
#data = np.loadtxt("Node7.out")
#data = np.fromfile("Node7.out",dtype=dt)
#data = np.genfromtxt("Node7.out")
#data = pd.read_csv("Node7.out",delim_whitespace=True,header=None)

data = pd.read_table("Node7.out",sep=" ")
data

#a = np.ndarray((600000,))

'''
f = open("Node7.bin","r")
for i in range(12):
    a = np.fromfile(f, dtype=float, count=2)
    #a[i] = np.fromfile(f, dtype=float, count=1)
    b = np.fromfile(f, dtype='|S1', count=1)
    print b
    del b
    print a

#c = np.fromfile(f, dtype=float, count=1)
c = np.fromfile(f, dtype='|S1', count=4)
d = np.fromfile(f, dtype=float, count=1)
print c
print d
'''
stop = time.clock()
print stop - start