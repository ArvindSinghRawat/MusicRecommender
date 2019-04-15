import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
import time
#csv to mongodb
startT = time.time()
csvfile = open('SpotifyFeaturesOmittedDuplicates.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client = MongoClient('localhost', 27017)
db = mongo_client['MusicDatabase']
db['MusicDetails'].drop()
header= ["_id", "genre", "artist_name", "track_name", "popularity", "acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness", "loudness", "mode" ,"speechiness","tempo","time_signature","valence"]
endT = time.time()
print("Reading Time : ",endT-startT)
startT = time.time()
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
    db['MusicDetails'].insert_one(row)
endT = time.time()
print("Time taken to insert in DB : ",endT-startT)