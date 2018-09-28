from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle
iris=load_iris()

numSamples,numFeatures=iris.data.shape
print(numSamples)
print(numFeatures)
print(list(iris.target_names))

x=iris.data
pca=PCA(n_components=1,whiten=True).fit(x)
x_pca=pca.transform(x)
print(pca.components_)
print('\n')
print(pca.explained_variance_ratio_)
print('\n')
print(sum(pca.explained_variance_ratio_))
from pylab import *
colors=cycle('rgb')
target_ids=range(len(iris.target_names))
pl.figure()
for i,c,label in zip(target_ids,colors,iris.target_names):
    pl.scatter(x_pca[iris.target==i,0],x_pca[iris.target==i,0],c=c,label=label)
pl.legend()
pl.show()