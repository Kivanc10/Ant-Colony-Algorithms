# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:52:55 2020

@author: Kivanc
"""
#%%
from random import uniform , randint ,shuffle,sample
import math
import time
import numpy
import numpy

a=time.time()

distanceMatrix = [[0 , 29 , 20 , 21 , 16 , 31 , 100 ,12 , 4  , 31],
[29 , 0  , 15 , 29 , 28 , 40 , 72 , 21 , 29 , 41],
[20 , 15 , 0  , 15 , 14 , 25 , 81 , 9  , 23 , 27],                    
[21 , 29 , 15 , 0  , 4 ,  12 , 92 , 12 , 25 , 13],
[16 , 28 , 14 , 4  , 0 ,  16 , 94 , 9  , 20 , 16],
[31 , 40 , 25 , 12 , 16 , 0 ,  95 , 24 , 36 , 3],
[100 ,72 , 81 , 92 , 94 , 95 , 0 ,  90 , 101 ,99],
[12 , 21 , 9 ,  12 , 9  , 24 , 90 , 0  , 15 , 25],
[4  , 29 , 23 , 25 , 20 , 36 , 101 ,15 , 0 ,  35],
[31 , 41 , 27 , 13 , 16 , 3 ,  99,  25,  35,  0]]

n=len(distanceMatrix)

def calculateDistance(path):
  index = path[0]             # Düğümler arası uzaklık hesabı
  distance = 0
  for nextIndex in path[1:]:
    distance += distanceMatrix[index][nextIndex]
    index = nextIndex
  return distance # mesafe döndürüldü

def swap(sequence,i,j):
  temp = sequence[i]     #Düğümler arası yer değiştirme(indis) fonksiyonu
  sequence[i]=sequence[j]
  sequence[j]=temp


def localPhremone(ants,a,b):
    ants=ants[0][:]
    swap(ants,a,b) 
    return (ants,calculateDistance(ants)) # ants listesi döndürür.

def globalPhremone(ants,a,b,c):
    ants=ants[0][:]
    swap(ants,a,b)
    swap(ants,b,c)
    return (ants,calculateDistance(ants)) # ants listesi döndürü

numAnts=10 # karınca sayısı

worstAnts=int(0.1*numAnts) # kötü değerli karıncalar(çok maliyetli)

bestAnts=int(0.8*numAnts) # iyi değerlikli karıncalar(az maliyetli)

alfa=2 # geçiş metodu için gereken alfa değeri

beta=2 # geçiş metodu için gereken beta değeri

passMax=10 # geçiş metodu değişkenleri

passMin=0 # geçiş metodu değişkenleri

transitionProbability=0.9

passMethod=alfa*1/n*beta*(passMax-passMin) # geçiş metodu rota üzerinde etkili bir yöntemdir.

iterationSize=100 # iterasyon büyüklüğü

ants=[] # karınca için array(liste)

initPath = list(range(0,n))

for i in range(numAnts):
    rota = sample(initPath,n)
    ants.append((rota,calculateDistance(rota)))

ants.sort(key = lambda x:x[1])

for iterationIndex in range(iterationSize):
    goAnts = ants[randint(0,bestAnts)] # haraket grubu seçilecek
    randomAntsIndex = randint(0,passMethod) # sonraki grup geçiş metoduna göre şekillendirilecek
    if (numpy.random.random() < transitionProbability):
        morePowerfulAnts = localPhremone(goAnts,randint(0,n-1),randint(0,n-1))
        if (ants[randomAntsIndex][1] > morePowerfulAnts[1]):
            ants[randomAntsIndex] = morePowerfulAnts
    else:
        for i in range(numAnts-worstAnts,numAnts):
            ants[i] = localPhremone(ants[i],randint(0,n-1),randint(0,n-1))
        ants.sort(key=lambda x:x[1])
    lowCostAnts = ants[0]
    effectlyGlobalAnts = globalPhremone(lowCostAnts,randint(0,n-1),randint(0,n-1),randint(0,n-1))
    if (ants[0][1] > effectlyGlobalAnts[1]):
        ants[0] = effectlyGlobalAnts
    ants.sort(key=lambda x:x[1])

print("Best path is : ",ants[0][0])
print("\n Best cost is : ",ants[0][1])


        


        
    
    

    
    





