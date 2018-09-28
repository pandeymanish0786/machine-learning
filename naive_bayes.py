import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
def readfiles(path):
    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            path=os.path.join(root,filename)
            inBody=False
            lines=[]
            f=io.open(path,'r',encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line=='\n' :
                    inBody=True
            f.close()
            message='\n'.join(lines)
            yield path,message

def dataframefromDirectory(path,classification):
    rows=[]
    index=[]
    for filename,message in readfiles(path):
        rows.append({'message':message,'class':classification})
        index.append(filename)
    return DataFrame(rows,index)
data=DataFrame({'message':[],'class':[]})
data=data.append(dataframefromDirectory('C:\\Users\M_K_P\Downloads\Compressed\DataScience\DataScience-Python3\emails\spam','spam'))
data=data.append(dataframefromDirectory('C:\\Users\M_K_P\Downloads\Compressed\DataScience\DataScience-Python3\emails\ham','ham'))
data.head()
#result
vectorizer=CountVectorizer()
counts=vectorizer.fit_transform(data['message'].values)
classifier=MultinomialNB()
targets=data['class'].values
classifier.fit(counts,targets)
#result
examples=['free viagra here now!!!',"hi bob,now about a game of golf"]
example_counts=vectorizer.transform(examples)
predictions=classifier.predict(example_counts)
predictions
#result
