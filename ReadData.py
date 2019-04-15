import pandas as pd
import numpy as np
import itertools
def time(t):
    ms = t % 1000
    s = int(t / 1000)
    m = int(s / 60)
    s = s % 60
    h = int(m / 60)
    m = m % 60
    return (ms, s, m, h)
infile = pd.read_csv("SpotifyFeaturesOmittedDuplicates.csv",encoding="ANSI")
data = infile[['genre','artist_name','track_name','track_id','popularity','duration_ms']]
print(data.columns)
print(len(data))
pt = data['duration_ms'].apply(time)
m = list(itertools.chain(*pt))
q = np.reshape(m,(int(len(m)/4),4))
pt = pd.DataFrame(q)
pt.columns = ['milliseconds','seconds','minutes','hours']
print(pt.head())
data = pd.concat([data,pt],axis=1)
print(data.head())
data.to_csv('Export.csv')