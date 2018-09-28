from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import datasets
from sklearn import svm
iris=datasets.load_iris()
#spliting the iris data into train /test data sers with 
#40% reserved for test set
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.4,random_state=0)
#build an svc model for prdicting iris classification using training data
clf=svm.SVC(kernel='linear',C=1).fit(x_train,y_train)
#now measures its performance with the test data
print(clf.score(x_test,y_test))
#we give cross_val_score a model ,the entire dataset and
#its "real" value and the number of folds:
scores=cross_val_score(clf,iris.data,iris.target,cv=5)
#now print accuracy for each fold
print(scores)
#and mean accuract for all the 5 fold
print(scores.mean())

#lets try a different kernel in svm for doing better and check our luck

clf=svm.SVC(kernel='poly',degree=2,C=1).fit(x_train,y_train)
scores=cross_val_score(clf,iris.data,iris.target,cv=5)
print(scores)
print(scores.mean())
#but this produces low accuracy..
#now sil=milarly bulid an svc poly model for iris data classificcation
clf=svm.SVC(kernel='poly',C=1).fit(x_train,y_train)
print(clf.score(x_test,y_test))