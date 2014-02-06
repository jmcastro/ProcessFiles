# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:34:03 2013

@author: Miguel
"""

from time import clock
import numpy as np

start_time = clock()

for i in range(10):
    a = np.loadtxt("nodalDispl.txt")
    #del a

end_time = clock()

print "Total time = ", end_time - start_time, "seconds"


start_time = clock()

record_dtype = np.dtype([
    ('node1', 'float'), 
    ('node2', 'float'), 
    ('node3', 'float'), 
    ('node4', 'float'), 
    ('node5', 'float'), 
    ('node6', 'float'), 
    ('node7', 'float'), 
    ('node8', 'float'), 
    ('node9', 'float'), 
    ('node10', 'float'), 
    ('node11', 'float'), 
    ('node12', 'float'), 
    ('node13', 'float'), 
    ('node14', 'float'), 
    ('node15', 'float'), 
    ('node16', 'float'), 
    ('node17', 'float'), 
    ('node18', 'float'), 
    ('node19', 'float'),     
    ('ws', '|S1'), 
])

for i in range(10):
    data = np.fromfile("nodalDispl.bin" , dtype = record_dtype)
    #del data

end_time = clock()

print "Total time = ", end_time - start_time, "seconds"
