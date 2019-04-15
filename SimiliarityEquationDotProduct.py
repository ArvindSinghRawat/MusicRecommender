import pandas as pd
import numpy as np
import time
start = time.time()
infile = pd.read_csv("tech_details.csv",encoding="ANSI")
id = pd.read_csv('Export.csv')['track_id']
infile = infile.transpose().to_dict()
end = time.time()
print("Time to Read tech_details : ",end-start)
start = time.time()
l = len(infile)
for i in range(100):
    #f = open('1\\'+id[i]+'.txt','w',encoding='ascii')
    sim = list()
    ls1 = list(infile[i].values())
    for j in range(l):
        ls2 = list(infile[j].values())
        sim.append(np.dot(ls1,ls2))
#    for j in sim:
#         f.write(str(j))
#         f.write(',')
#    f.write('\n')
    np.array(sim).dump('1\\'+id[i]+'.dat')
    print(i)
    break
#f.close()
end = time.time()
print("Time to Write II Similiarity : ",end-start)