# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:32:54 2013

@author: jmcastro
"""

#import string
#import random
#def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#    return ''.join(random.choice(chars) for x in range(size))
#print id_generator()

import numpy as np

a = np.ndarray((1e6,2))
a = np.random.rand(1e6,20)

np.savetxt("zz.txt",a)

#b = np.loadtxt("zz.txt")