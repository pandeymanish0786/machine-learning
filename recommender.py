import pandas as pd
r_cols =['user_id','movie_id','rating']
ratings=pd.read_csv("C:\\Users\\M_K_P\\Downloads\\Compressed\\DataScience\\DataScience-Python3\\ml-100k\\u.data",sep= '\t' , names = r_cols ,usecols=range(3),encoding="ISO-8859-1")
m_cols=['movie_id','title']
movies=pd.read_csv("C:\\Users\\M_K_P\\Downloads\\Compressed\\DataScience\\DataScience-Python3\\ml-100k\\u.item",sep='|', names = m_cols ,usecols=range(2),encoding="ISO-8859-1")
ratings=pd.merge(movies,ratings)
print(ratings.head())
print('\n')
movieratings=ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(movieratings.head())
print('\n')
#created a matrix using user id as rows and title as column .. and ratings as valus
  #now lets extracted a series of user who rated star wars
starwarsratings=movieratings['Star Wars (1977)']
print(starwarsratings.head())
 #now extract movie which ratings can be a pair with starwars using corrwith function..
similarmovies=movieratings.corrwith(starwarsratings)
similarmovies=similarmovies.dropna()
df=pd.DataFrame(similarmovies)
df.head(10)
#now lets sort the data
print(similarmovies.sort_values(ascending=False))
#lets create a new data frame that counts up how may ratinga wdist in each movie...
import numpy as np
moviestats=ratings.groupby('title').agg({'rating':[np.size,np.mean]})
print(moviestats.head())
#now lets left the movies ehich is rated by less than 100 people..
print('\n \n')
popularmovies=moviestats['rating']['size']>=500
print(moviestats[popularmovies].sort_values([('rating','mean')],ascending=False)[ :15])
print('\n\n')
# lets join this data with our original set of similar movies to starwars
df=moviestats[popularmovies].join(pd.DataFrame(similarmovies,columns=['similarty']))
df.head()
print(df.sort_values(['similarty'],ascending=False)[:15])

