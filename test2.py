import csv
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pymongo import MongoClient

myclient = MongoClient('localhost', 27017)
mydb   = myclient["MusicDatabase"]
mycoll = mydb["MusicDetails"]
data   = mycoll.find()

def dplot( x , y ):
    for column in y.T:
        plt.scatter(x,column)
    plt.show()

def calcEnergy( data,plot = False ):
#energy
    energy = np.zeros((mycoll.estimated_document_count(),1),dtype=float)
    highenergy = np.zeros((mycoll.estimated_document_count(),1),dtype=float)
    medenergy = np.zeros((mycoll.estimated_document_count(),1),dtype=float)
    lowenergy = np.zeros((mycoll.estimated_document_count(),1),dtype=float)
    i = 0
    for x in data:
        energy[i] = float(x["energy"])
        i += 1
    
    # Calculating Quartiles
    q = np.percentile(energy,[25,50,75])
    # q[0] : 1st Quartile
    # q[1] : 2nd Quartile
    # q[2] : 3rd Quartile
    mn = energy.min()
    mx = energy.max()
    
    # for low energy
    i = 0
    for x in energy:
        if( x <= q[0] ):
            mv = ( q[0] - x )/ ( q[0] - mn ) 
        else:
            mv = 0
        lowenergy[i] = mv
        i += 1
    
    # for medium energy
    i = 0
    for x in energy:
        if( x > q[0] and x <= q[1] ):
            mv = (x - q[0])/(q[1] - q[0])
        elif( x > q[1] and x <= q[2] ):
            mv = (q[2] - x)/(q[2] - q[1])
        else:
            mv = 0
        medenergy[i] = mv
        i += 1
        
    # for high energy
    i = 0
    for x in energy:
        if(x > q[2]):
            mv = (x - q[2])/(mx - q[2])
        else:
            mv = 0
        highenergy[i] = mv
        i += 1
    calc = np.concatenate((lowenergy,medenergy,highenergy),axis=1)
    if plot == True:
        dplot(energy,calc) 
    return calc

# Calling Calculate Energy
# calcEnergy(data,plot = True)







########################################
#               valence                #
########################################
valence=[]
lowvalence=[]
medvalence=[]
highvalence=[]
data = mycoll.find()
for x in data:
    doc=float(x["valence"])
    valence.append(doc)
#valence = list(map(float, valence))
for x in valence:
    if( x <= 0.206000 ):
        mv=(0.206000-x)/0.206000
    else:
        mv=0
    lowvalence.append(mv)
# for medium valence

for x in valence:
    if(x>0.206000 and x<=0.420000):
        mv=(x-0.206000)/0.214000
    elif(x>0.420000 and x<=0.652000):
        mv=(0.652000-x)/0.232000
    else:
        mv=0
    medvalence.append(mv)
# for high valence

for x in valence:
    if(x>0.652000):
        mv=(x-0.652000)/0.348000
    else:
        mv=0
    highvalence.append(mv)

def plotvalence():

    plt.scatter(valence,lowvalence)
    plt.scatter(valence,medvalence)
    plt.scatter(valence,highvalence)

    plt.show()
#plotvalence()

#tempo
tempo=[]
lowtempo=[]
medtempo=[]
hightempo=[]
data=mycoll.find()
for x in data:
    doc=x["tempo"]
    tempo.append(doc)
tempo = list(map(float, tempo))
for x in tempo:
    if(x<=0.289460):
        mv=(0.289460-x)/0.289460
    else:
        mv=0
    lowtempo.append(mv)
# for medium tempo

for x in tempo:
    if(x>0.289460 and x<=0.398479):
        mv=(x-0.289460)/0.109019
    elif(x>0.398479 and x<=0.513370):
        mv=(0.513370-x)/0.114891
    else:
        mv=0
    medtempo.append(mv)
# for high tempo

for x in tempo:
    if(x>0.513370):
        mv=(x-0.513370)/0.486630
    else:
        mv=0
    hightempo.append(mv)
def plottempo():

    plt.scatter(tempo,lowtempo)
    plt.scatter(tempo,medtempo)
    plt.scatter(tempo,hightempo)

    plt.show()
#plottempo()

#danceability    
danceability=[]
lowdanceability=[]
meddanceability=[]
highdanceability=[]
data=mycoll.find()
for x in data:
    doc=x["danceability"]
    danceability.append(doc)
danceability = list(map(float, danceability))
for x in danceability:
    if(x<=0.411000):
        mv=(0.411000-x)/0.354000
    else:
        mv=0
    lowdanceability.append(mv)
# for medium danceability

for x in danceability:
    if(x>0.411000 and x<=0.560000):
        mv=(x-0.411000)/0.149000
    elif(x>0.560000 and x<=0.686000):
        mv=(0.686000-x)/0.126000
    else:
        mv=0
    meddanceability.append(mv)
# for high danceability

for x in danceability:
    if(x>0.686000):
        mv=(x-0.686000)/0.301000
    else:
        mv=0
    highdanceability.append(mv)
def plotdanceability():

    plt.scatter(danceability,lowdanceability)
    plt.scatter(danceability,meddanceability)
    plt.scatter(danceability,highdanceability)

    plt.show()
#plotdanceability()

#acousticness
acousticness=[]
lowacousticness=[]
medacousticness=[]
highacousticness=[]
data=mycoll.find()
for x in data:
    doc=x["acousticness"]
    acousticness.append(doc)
acousticness = list(map(float, acousticness))
for x in acousticness:
    if(x<=0.050300):
        mv=(0.050300-x)/0.050300
    else:
        mv=0
    lowacousticness.append(mv)
# for medium acousticness

for x in acousticness:
    if(x>0.050300 and x<=0.299000):
        mv=(x-0.050300)/0.248700
    elif(x>0.299000 and x<=0.803000):
        mv=(0.803000-x)/0.504000
    else:
        mv=0
    medacousticness.append(mv)
# for high acousticness

for x in acousticness:
    if(x>0.803000):
        mv=(x-0.803000)/0.193000
    else:
        mv=0
    highacousticness.append(mv)
def plotacousticness():

    plt.scatter(acousticness,lowacousticness)
    plt.scatter(acousticness,medacousticness)
    plt.scatter(acousticness,highacousticness)

    plt.show()
#plotacousticness()

#liveness
liveness=[]
lowliveness=[]
medliveness=[]
highliveness=[]
data=mycoll.find()
for x in data:
    doc=x["liveness"]
    liveness.append(doc)
liveness = list(map(float, liveness))
for x in liveness:
    if(x<=0.097700):
        mv=(0.097700-x)/0.088030
    else:
        mv=0
    lowliveness.append(mv)
# for medium liveness

for x in liveness:
    if(x>0.097700 and x<=0.130000):
        mv=(x-0.097700)/0.032300
    elif(x>0.130000 and x<=0.280000):
        mv=(0.280000-x)/0.150000
    else:
        mv=0
    medliveness.append(mv)
# for high liveness

for x in liveness:
    if(x>0.280000):
        mv=(x-0.280000)/0.720000
    else:
        mv=0
    highliveness.append(mv)
def plotliveness():

    plt.scatter(liveness,lowliveness)
    plt.scatter(liveness,medliveness)
    plt.scatter(liveness,highliveness)

    plt.show()
#plotliveness()

#loudness
loudness=[]
lowloudness=[]
medloudness=[]
highloudness=[]
data=mycoll.find()
for x in data:
    doc=x["loudness"]
    loudness.append(doc)
loudness = list(map(float, loudness))
for x in loudness:
    if(x<=0.728267):
        mv=(0.728267-x)/0.728267
    else:
        mv=0
    lowloudness.append(mv)
# for medium loudness

for x in loudness:
    if(x>0.728267 and x<=0.818586):
        mv=(x-0.728267)/0.090319
    elif(x>0.818586 and x<=0.865234):
        mv=(0.865234-x)/0.046648
    else:
        mv=0
    medloudness.append(mv)
# for high loudness

for x in loudness:
    if(x>0.865234):
        mv=(x-0.865234)/0.134766
    else:
        mv=0
    highloudness.append(mv)
def plotloudness():

    plt.scatter(loudness,lowloudness)
    plt.scatter(loudness,medloudness)
    plt.scatter(loudness,highloudness)

    plt.show()
#plotloudness()

#instrumentalness
instrument=[]
lowinstrument=[]
medinstrument=[]
highinstrument=[]
data=mycoll.find()
for x in data:
    doc=x["instrumentalness"]
    instrument.append(doc)
instrument = list(map(float, instrument))
for x in instrument:
    if(x<=0):
        mv=1
    else:
        mv=0
    lowinstrument.append(mv)
# for medium instrument

for x in instrument:
    if(x>0 and x<=0.000058):
        mv=(x)/0.000058
    elif(x>0.000058 and x<=0.088500):
        mv=(0.088500-x)/0.088442
    else:
        mv=0
    medinstrument.append(mv)
# for high instrument

for x in instrument:
    if(x>0.088500):
        mv=(x-0.088500)/0.910500
    else:
        mv=0
    highinstrument.append(mv)
def plotinstrument():

    plt.scatter(instrument,lowinstrument)
    plt.scatter(instrument,medinstrument)
    plt.scatter(instrument,highinstrument)

    plt.show()
#plotinstrument() 

#speechiness
speechiness=[]
lowspeechiness=[]
medspeechiness=[]
highspeechiness=[]
data=mycoll.find()
for x in data:
    doc=x["speechiness"]
    speechiness.append(doc)
speechiness = list(map(float, speechiness))
for x in speechiness:
    if(x<=0.037100):
        mv=(0.037100-x)/0.014900
    else:
        mv=0
    lowspeechiness.append(mv)
# for medium speechiness

for x in speechiness:
    if(x>0.037100 and x<=0.049800):
        mv=(x-0.037100)/0.012700
    elif(x>0.049800 and x<=0.108000):
        mv=(0.108000-x)/0.058200
    else:
        mv=0
    medspeechiness.append(mv)
# for high speechiness

for x in speechiness:
    if(x>0.108000):
        mv=(x-0.108000)/0.859000
    else:
        mv=0
    highspeechiness.append(mv)
def plotspeechiness():

    plt.scatter(speechiness,lowspeechiness)
    plt.scatter(speechiness,medspeechiness)
    plt.scatter(speechiness,highspeechiness)

    plt.show()
#plotspeechiness()

#user()
def user(x,y):
    if(x in highenergy and y in highvalence):
        return 5
    elif(x in highenergy and y in medvalence):
        return 4
    elif(x in highenergy and y in lowvalence):
        return 3
    elif(x in medenergy and y in highvalence):
        return 3
    elif(x in medenergy and y in medvalence):
        return 2
    elif(x in medenergy and y in lowvalence):
        return 1
    elif(x in lowenergy and y in highvalence):
        return 2
    elif(x in lowenergy and y in medvalence):
        return 1
    else:
        return 0