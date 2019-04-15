import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient


def dplot( x , y ):
    for column in y.T:
        plt.scatter(x,column)
    plt.show()

def calcFuzzySet( data ,plot = False ):
#energy
        # Vectors for Fuzzy Membership Values
    high = np.zeros((mycoll.estimated_document_count(),1),dtype=float)  # For High value's set
    mid = np.zeros((mycoll.estimated_document_count(),1),dtype=float)   # For Mid value's set
    low = np.zeros((mycoll.estimated_document_count(),1),dtype=float)   # For Low value's set
        # Calculating Quartiles
    q = np.percentile(data,[25,50,75])
        # q[0] : 1st Quartile
        # q[1] : 2nd Quartile
        # q[2] : 3rd Quartile
    mn = data.min()
    mx = data.max()
    #print(mn," ",q[0]," ",q[1]," ",q[2]," ",mx )
    i = 0
    for x in data:
        #
        #  For calculating Low
        if( x <= q[0] ):
            mv = ( q[0] - x )/ ( q[0] - mn ) 
        else:
            mv = 0
        low[i] = mv
        #
        # For Calculating Mid
        if( x > q[0] and x <= q[1] ):
            mv = (x - q[0])/(q[1] - q[0])
        elif( x > q[1] and x <= q[2] ):
            mv = (q[2] - x)/(q[2] - q[1])
        else:
            mv = 0
        mid[i] = mv
        #
        # For Calculating High
        if(x > q[2]):
            mv = (x - q[2])/(mx - q[2])
        else:
            mv = 0
        high[i] = mv
        i += 1
    calcV = np.concatenate((low,mid,high),axis=1)
    if plot == True:
        dplot(data,calcV) 
    return calcV

# Calling Calculate Energy

myclient = MongoClient('localhost', 27017)
mydb   = myclient["MusicDatabase"]
mycoll = mydb["MusicDetails"]
data   = mycoll.find()
valence = np.zeros((mycoll.estimated_document_count(),1),dtype=float)
energy  = np.zeros((mycoll.estimated_document_count(),1),dtype=float)
i = 0
for x in data:
    valence[i] = float(x["valence"])
    energy[i]  = float(x["energy"])
    i += 1
valenceF = calcFuzzySet(valence,plot = True)
energyF = calcFuzzySet(energy,plot = True)