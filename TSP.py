# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:45:10 2018

@author: WindFamilyRain
"""
from __future__ import division
import pandas as pd
import utils
import numpy as np
import math
import matplotlib.pyplot as plt
citys=pd.read_table('./data/tsp100.txt',sep='\t',header=None)
citys.columns=['x']
citys['y']=None

for i in range(len(citys)):
    coordinate=citys['x'][i].split()
    citys['x'][i]=float(coordinate[0])
    citys['y'][i]=float(coordinate[1])

print (citys.head(5))

start=list(citys.iloc[0])
end=list(citys.iloc[0])
citys=citys.drop([0])
citys.index=[i for i in range(len(citys))]

paths=[i for i in range(len(citys))]# initiate path

'''
random path and calculate distance to sreach for optimal initiate temperature
'''

distance1=0
distance2=0
dif=0
for i in range(10):  
    #np.random.shuffle(path)
    newPaths1=list(np.random.permutation(paths))
    newPaths2=list(np.random.permutation(paths))
    distance1=utils.CalLength(citys,newPaths1,start,end)
    distance2=utils.CalLength(citys,newPaths2,start,end)
    difNew=abs(distance1-distance2)
    if difNew>=dif:
        dif=difNew



Pr=0.5 #initiate accept possibility
T0=dif/Pr#initiate terperature
T=T0
Tmin=T/50
k=10*len(paths) #times of internal circulation
initialPath=paths.copy()
length=utils.CalLength(citys,initialPath,start,end)
print (length)

t=0 #time  
'''
optimalPath=initialPath.copy()
optimalLength=length
while T>Tmin:
    for i in range(k):
        a=0
        b=0
        newPaths=optimalPath.copy()
        while a==b:
            a=np.random.randint(0,len(paths))
            b=np.random.randint(0,len(paths))
        te=newPaths[a]
        newPaths[a]=newPaths[b]
        newPaths[b]=te
        newLength=utils.CalLength(citys,newPaths,start,end)
        if newLength<length:
            optimalLength=newLength
            optimalPath=newPaths
        else:
             #metropolis principle
             p=math.exp(-(newLength-length)/T)
             r=np.random.uniform(low=0,high=1)
             if r<p:
                optimalLength=newLength
                optimalPath=newPaths
    t+=1
    print t
    T=T0/(1+t)
print optimalLength

'''
initialPath=list(np.random.permutation(paths))
length=utils.CalLength(citys,initialPath,start,end)
optimalPath = initialPath.copy()
optimalLength=length
t=0
while T>Tmin:
    for i in range(k):
        newPaths=optimalPath.copy()
        for j in range(int(T0/500)):
            a=0
            b=0
            while a==b:
                a=np.random.randint(0,len(paths))
                b=np.random.randint(0,len(paths))
            te=newPaths[a]
            newPaths[a]=newPaths[b]
            newPaths[b]=te
        newLength=utils.CalLength(citys,newPaths,start,end)
        if newLength<optimalLength:
            optimalLength=newLength
            optimalPath=newPaths
            print(optimalPath[:5])
        else:
             #metropolis principle
             p=math.exp(-(newLength-optimalLength)/T)
             r=np.random.uniform(low=0,high=1)
             if r<p:
                 optimalLength=newLength
                 optimalPath=newPaths

    back=np.random.uniform(low=0,high=1)
    if back>=0.85:
        T=T*2
        continue
    t+=1
    print (t)
    T=T0/(1+t)
print (optimalLength)




citys['order']=initialPath
citys_order=citys.sort_values(by=['order'])
plt.plot(citys_order['x'],citys_order['y'])         
