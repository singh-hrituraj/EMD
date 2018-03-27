#Empirical Mode Decomposition
#Written By Hrituraj Singh

import numpy as np
import pandas as pd

filepath = '/home/hrituraj/Desktop/IOP/AirPassengers.csv'
dataset = pd.read_csv(filepath)
X = np.array(dataset['#Passengers'])




c = X.T
N = len(X)


imf = []

while True:
    
    h = c
    SD = 1
    
    while SD > 0.3:
        d = np.diff(h)
        maxmin = []
        
        for i in range(0,N-2):
            if d[i] == 0:
                maxmin.append(i)
            
            elif np.sign(d[i]) != np.sign(d[i+1]):
                maxmin(i+1)
                
        if len(maxmin) < 2:
            break
        
        #To Be Done From Here
