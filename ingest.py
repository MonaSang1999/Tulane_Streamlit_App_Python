from reddit_api import get_access_token, get_new_posts
from model import predict_sentiment
import pandas as pd
import os

data_file = 'reddit_movie_reviews.csv'

def ingest_predicted_reviews(num_posts):
    token = get_access_token()
    posts = get_new_posts('r/movies', token, limit=num_posts)
    df = pd.DataFrame()
    for post in posts:
        df = df.append({
            'id': post['id'],
            'created': post['created'],
            'title': post['title'],
            'comment': post['selftext'],
            'type': post['link_flair_text']
        }, ignore_index=True)    
    df = predict_sentiment(df)
    if os.path.isfile(data_file):
        # append data to datastore
        df = pd.read_csv(data_file).append(df, ignore_index=True)
    # eliminate duplicates
    df = df.drop_duplicates(subset='id', keep="last")
    df.to_csv(data_file, index=False)