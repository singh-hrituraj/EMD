#Empirical Mode Decomposition
#Written By Hrituraj Singh

import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline



def emd(X):
    c = X.T
    N = len(X)
    imf = np.zeros((1,N))
    imf = np.array(imf)

    while True:
    
        h = c
        SD = 1
    
        while SD > 0.3:
            d = np.diff(h)
            maxmin = np.array([])
        
            for i in range(0,N-2):
                if d[i] == 0:
                    maxmin = np.hstack([maxmin,i])
            
                elif (np.sign(d[i]) != np.sign(d[i+1])):
                    maxmin = np.hstack([maxmin,i+1])
                
            if len(maxmin) < 2:
                break
            
            if maxmin[0] > maxmin[1]:
                maxes = maxmin[np.arange(0,len(maxmin),2)]
                mins  = maxmin[np.arange(1,len(maxmin),2)]
            else:
                maxes = maxmin[np.arange(1,len(maxmin),2)]
                mins  = maxmin[np.arange(0,len(maxmin),2)]
            
            beg = np.array([0])
            end = np.array([N-1])
        
            maxes = np.hstack((beg,maxes))
            maxes = np.hstack((maxes,end)).astype('int')
        
            mins  = np.hstack((beg,mins))
            mins  = np.hstack((mins,end)).astype('int')
            
    
            
            maxenv = CubicSpline(maxes, h[maxes])(np.arange(0,N))
            minenv = CubicSpline(mins, h[mins])(np.arange(0,N))
        
            m = (maxenv + minenv)/2
            prevh = h
        
            h = h - m
            eps = 0.0000001
            num = (prevh - h)*(prevh - h)
            den = prevh * prevh
        
            SD = np.sum(num.astype('float') / den)
        
        imf = np.vstack((imf,h)) 
    
        if len(maxmin) < 2:
            break
    
        c = c - h

    return imf[1:,:]
    
        
        
        
        
            
        
        
            
            

