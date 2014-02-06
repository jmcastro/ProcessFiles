# -*- coding: utf-8 -*-
"""
Created on Tue Dec 03 15:01:21 2013

@author: Miguel
"""

import matplotlib.pyplot as plt
import numpy as np

##%%
f = open("ref_file.txt","r")
lst = f.readlines()
sum = 0.0
for i in lst:
    sum += float(i.split()[2])
print sum
print sum/len(lst)
f.close()


g = open("1-NGA_no_191_H2.dat", "r")
lst2 = g.readlines()
g.close()

y = [float(i) for i in lst2]
x = [i*0.01 for i in range(len(y))]

h = np.loadtxt("1-NGA_no_191_H2.dat")
print h

plt.plot(x[:8000],h[:8000])
#plt.suptitle("Teste")
plt.grid(color="y", linestyle="-.", linewidth=0.5)