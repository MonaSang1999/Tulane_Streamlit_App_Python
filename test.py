import pandas as pd
from wordcloud import WordCloud

df=pd.read_csv('IMDB_movie_reviews_labeled.csv')
text = ""
for index, row in df.loc[df.sentiment == "positive", : ].iterrows():  #go every row in the dataframe
    text += str(row['review']) + " "
wc = WordCloud()
wc.generate(text). to_file('wordcloud_pos.png')

text=""
for index, row in df.loc[df.sentiment == "negative", : ].iterrows():  #go every row in the dataframe
    text += str(row['review']) + " "
wc = WordCloud()
wc.generate(text). to_file('wordcloud_neg.png')