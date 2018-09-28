import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,datasets
def createClusteredData(N,k):
    np.random.seed(10)
    pointsPerCluster=float (N)/k
    x=[]
    y=[]
    for i in range(k):
        incomecentroid=np.random.uniform(20000.0,200000.0)
        agecentroid=np.random.uniform(20.0,70.0)
        for j in range(int(pointsPerCluster)):
            x.append([np.random.normal(incomecentroid,10000.0),np.random.normal(agecentroid,2.0)])
            y.append(i)
        x=np.array(x)
        y=np.array(y)
        return x,y
##
(x,y)=createClusteredData(100,5)
plt.figure(figsize=(8,6))
plt.scatter(x[:,0],x[:,1],c=y.astype(np.float))
plt.show()
##
C=1.0
svc=svm.SVC(kernel='linear',C=C).fit(x,y)

def plotPredictions(clf):
    xx,yy=np.meshgrid(np.arange(0,250000,10),np.arange(10,70,0.5))
    z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
    plt.figure(figsize=(8,6))
    z=z.reshape(xx.shape)
    plt.contourf(xx,yy,z,cmap=plt.cm.Paired,alpha=0.8)
    plt.scatter(x[:,0],x[:,1],c=y.astype(np.float))
    plt.show()
    
plotPredictions(svc)

svc.predict([200000,40])
svc.predict([5000,65])
    

  

