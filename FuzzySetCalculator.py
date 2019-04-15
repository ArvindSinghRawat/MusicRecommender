import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient

def dplot( x , y ):
    for column in y.T:
        plt.scatter(x,column)
    plt.xlabel("Values")
    plt.ylabel("Degree of membership")
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
        if( x <= q[0] ): # First Quartile
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
        # Combining All values into a single matrix
    calcV = np.concatenate((low,mid,high),axis=1)
        # If plot is True then Plot the calculated sets
    if plot == True:
        dplot(data,calcV) 
        # Retruns Calculated matrix
    return calcV

def CrispSetCalculator( *args ):
    crisp_set = np.zeros((args[0].shape[0],1),dtype=int)
    v = 0 # Feature Counter
    for vec in args:
        n = vec.argmax(axis=1)
        k = np.array(n.reshape(n.shape[0],1),dtype=int)
        print(k)
        crisp_set += k
        v += 1
    return crisp_set

myclient = MongoClient('localhost', 27017)  # Created a connection with MongoDB
mydb   = myclient["MusicDatabase"]          # Database Connected
mycoll = mydb["MusicDetails"]               # Table Connected
data   = mycoll.find()                      # Data from table
valence = np.zeros((mycoll.estimated_document_count(),1),dtype=float)   # Blank vector of Size count * 1
energy  = np.zeros((mycoll.estimated_document_count(),1),dtype=float)   # Blank vector of Size count * 1
track = np.empty((mycoll.estimated_document_count(),1), dtype=object, order='C')   # Blank vector of Size count * 1
i = 0
for x in data:
    valence[i] = float(x["valence"])   # Assigning Valence in a vector
    energy[i]  = float(x["energy"])    # Assigning Energy in a vector
    track[i] = str(x.get('_id'))       # Assigning Track in a vector
    i += 1
valenceF = calcFuzzySet(valence,plot = True)   # Calculating Fuzzy Values for Valence
energyF = calcFuzzySet(energy,plot = False)     # Calculating Fuzzy Values for Valence
#crisp = CrispSetCalculator(valenceF,energyF)    # Finding Combined Crisp Values
#i = 0
#for t in track:  # Updating Database to add new crisp values
#    mycoll.find_one_and_update(query={'_id':track[i][0]},\
#    update={"$set": {'CrispMood': str(crisp[i])}},\
#    upsert=True,full_response= True,filter=dict())
#    i += 1
myclient.close() # Closing the Connection