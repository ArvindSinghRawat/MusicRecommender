import csv
import json
import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient
import time
li=[]
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["MusicDB"]
mycoll = mydb["users"]
data=mycoll.find()
for x in data:
    doc=x["energy"]
    li.append(doc)
li = list(map(float, li))
def energy(n):
    if(n<0.33):
        return 0
    elif(n>=0.33 and n<0.78):
        return 1
    else:
        return 2
    
           
li1=[]      
def plot():
    plt.xlim(0,1.5) 
    plt.ylim(0,2.5)
    for i in range(0,len(li)):
        li1.append(energy(li[i]))
    plt.scatter(li,li1, label= "stars", color= "green", marker= "*", s=30)
    
    plt.show()
        
plot()
