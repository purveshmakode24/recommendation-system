import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ..utils import clean_text

df = pd.read_csv('csv/books.csv',on_bad_lines='skip',encoding='latin-1',sep=';')

# remove duplicate records
df1 = df.drop_duplicates(subset='Book-Title')

# sample random 8000 records
sample_size = 8000
df8k = df1.sample(n=sample_size, replace=False, random_state=490)
df8k = df8k.reset_index()
df8k = df8k.drop('index',axis=1)

# cleaning
df8k['Book-Author'] = df8k['Book-Author'].apply(clean_text)
df8k['Book-Title'] = df8k['Book-Title'].str.lower()
df8k['Publisher'] = df8k['Publisher'].str.lower()


# def q_books(input):
#     books = df8k[df8k['Book-Title'].str.contains(input)][:5].to_json(orient='records')
#     return books

def books():
    books = df8k.to_json(orient='records')
    return books

def book_recommendations(input_book):

    df2 = df8k.drop(['ISBN','Image-URL-S','Image-URL-M','Image-URL-L','Year-Of-Publication'],axis=1)
    df2['data'] = df2['Book-Title'].astype('str')+ ' ' + df2['Book-Author'].astype('str') + ' ' + df2['Publisher'].astype('str')

    vectorizer = CountVectorizer()
    vectorized = vectorizer.fit_transform(df2['data'])

    similarities = cosine_similarity(vectorized)

    # Remapping the simailarties vector back to the previos dataframe
    df2 = pd.DataFrame(similarities, columns=df8k['Book-Title'], index=df8k['Book-Title']).reset_index()
    df2['Image-URL-M'] = df8k['Image-URL-M']
    print(df2)

    # Get top 10 recommendations
    recommendations = pd.DataFrame(df2.nlargest(11,input_book)[['Book-Title','Image-URL-M']])
    print('-->',recommendations)
    recommendations = recommendations[recommendations['Book-Title']!=input_book]
    recommendations = recommendations.to_json(orient='records')

    return recommendations