import numpy as np
import pandas as pd
from sklearn import tree
input_file="C:\\Users\M_K_P\Downloads\Compressed\DataScience\DataScience-Python3\PastHires.csv"
df=pd.read_csv(input_file,header=0)
df.head()

d={'Y':1, 'N':0}
df['Hired']=df['Hired'].map(d)
df['Employed?']=df['Employed?'].map(d)
df['Top-tier school']=df['Top-tier school'].map(d)
df['Interned']=df['Interned'].map(d)
d={'BS':0, 'MS':1 ,'PhD':2}
df['Level of Education']=df['Level of Education'].map(d)
df.head()

features=list(df.columns[:6])
features

y=df["Hired"]
x=df[features]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)

from IPython.display import Image  
from sklearn.externals.six import StringIO  
import pydotplus

dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=features)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png()) 
from sklearn.ensemble import RandomForestClassification
clf=RandomForestClassifier(n_estimators=10)
clf=clf.fit(x,y)
#predict employment f an employed 10 years veteran
print (clf.predict([10,1,4,0,0,0]))
#predict employment f an unemployed 10 years veteran
print (clf.predict([10,0,4,0,0,0]))

