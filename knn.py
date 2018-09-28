import pandas as pd
r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv('C://Users/M_K_P/Downloads/Compressed/DataScience/DataScience-Python3/ml-100k//u.data',sep='\t',names=r_cols,usecols=range(3))
#print(ratings.head())
import numpy as np
movieproperties=ratings.groupby('movie_id').agg({'rating':[np.size,np.mean]})
#print(movieproperties.head())

movienumratings=pd.DataFrame(movieproperties['rating']['size'])
movienormalizednumratings=movienumratings.apply(lambda x:(x-np.min(x))/(np.max(x)-np.min(x)))
print(movienormalizednumratings.head())
moviedict={}
with open (r'C://Users/M_K_P/Downloads/Compressed/DataScience/DataScience-Python3/ml-100k//u.item') as f:
    temp=''
    for line in f:
        #line.decode("iso-8859-1'")
        fields=line.rstrip('\n').split('|')
        movieid=int(fields[0])
        name=fields[1]
        geners=fields[5:25]
        geners=map(int,geners)
        moviedict[movieid]=(name,np.array(list(geners)),movienormalizednumratings.loc[movieid].get('size'),movieproperties.loc[movieid].rating.get('mean'))
print(moviedict[1])
from scipy import spatial
def ComputerDistance(a,b):
    genresA=a[1]
    genresB=b[1]
    genredistance=spatial.distance.cosine(genresA,genresB)
    popularityA=a[2]
    popularityB=b[2]
    popularitydistance=abs(popularityA-popularityB)
    return genredistance+popularitydistance
    
print(ComputerDistance(moviedict[2],moviedict[4]))
print(moviedict[2])
print(moviedict[4])
import operator
def getneighbors(movieid,k):
    distances=[]
    for movie in moviedict:
        if(movie != movieid):
            dist=ComputerDistance(moviedict[movieid],moviedict[movie])
            distances.append((movie,dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
    
k=5
avgrating=0
neighbors=getneighbors(1,k)
for neighbor in neighbors:
    avgrating += moviedict[neighbor][3]
    print(moviedict[neighbor][0] + " " + str(moviedict[neighbor][3]))
avgrating /= k
print(avgrating)  

print(moviedict[1])     