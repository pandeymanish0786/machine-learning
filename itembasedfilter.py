import pandas as pd
r_cols =['user_id','movie_id','rating']
ratings=pd.read_csv("C:\\Users\\M_K_P\\Downloads\\Compressed\\DataScience\\DataScience-Python3\\ml-100k\\u.data",sep= '\t' , names = r_cols ,usecols=range(3),encoding="ISO-8859-1")
m_cols=['movie_id','title']
movies=pd.read_csv("C:\\Users\\M_K_P\\Downloads\\Compressed\\DataScience\\DataScience-Python3\\ml-100k\\u.item",sep='|', names = m_cols ,usecols=range(2),encoding="ISO-8859-1")
ratings=pd.merge(movies,ratings)
print(ratings.head())
print('\n')
userratings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
#print(userratings.head())
print('\n')
#  will compute a correlation score for every column pair in the matrix!  
#this gives us a correlation score between every pair of movies (where at least one user rated both movies - otherwise NaN's will show up.) That's amazing!
corrmatrix=userratings.corr()
#print(corrmatrix.head())
print('\n')
#we'll use the min_periods argument to throw out results where fewer than 100 users rated a given movie pair:
corrMatrix = userratings.corr(method='pearson', min_periods=100)
#print(corrMatrix.head())
#I'll extract his ratings from the userRatings DataFrame, 
#and use dropna() to get rid of missing data (leaving me only with a Series of the movies I actually rated:)
myratings=userratings.loc[0].dropna()
print(myratings)
#now bulid up a lis of possible reccommedation based oh the pas movies which they are similar to..or which i actually hated or liked..similar
simcandidates=pd.Series()
for i in range(0,len(myratings.index)):
    print("adding sims for"+ myratings.index[i] + "...")
    #retrieve similar movies to this one that i rated
    sims=corrmatrix[myratings.index[i]].dropna()
    #now scale its similarty by how well i rated this movie
    sims=sims.map(lambda x:x*myratings[i])
    #add the score to the list of similarty candidates
    simcandidates=simcandidates.append(sims)
#glance at our result so for:
print("sorting...")
simcandidates.sort_values(inplace=True,ascending=False)
#print(simcandidates.head(10))
simcandidates=simcandidates.groupby(simcandidates.index).sum()
#we use group by function..because this add together the score from movies that show
#up more than once//so they'll count more
simcandidates.sort_values(inplace=True,ascending=False)
print(simcandidates.head(10))
#the last thing is to drop the same movies ehich rated mre than once
filteredsims=simcandidates.drop(myratings.index)
print(filteredsims.head(10))




