import matplotlib.pyplot as plt
import random
import numpy as np

samples = range(20)

data = 20*[0]

M = 20

for i in range(M):
    data[samples.index(int(19*random.random()))] += 1
#print data.index(max(data))
print int(19*random.random())
