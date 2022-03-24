import pickle

def predict_sentiment(df):
    pipe = pickle.load(open('pipeline.pkl', 'rb'))
    docs = []
    for index, row in df.iterrows():
        docs.append(row['title'] + " " + row["comment"])
    predicted_sentiment = pipe.predict(docs)
    df['sentiment'] = predicted_sentiment
    return df