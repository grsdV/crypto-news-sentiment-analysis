import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
    # Analyze the sentiment polarity of the given text
    return TextBlob(text).sentiment.polarity

if __name__ == '__main__':
    # Load the news articles from the CSV file
    df = pd.read_csv('data/cryptocurrency_news.csv')
    
    # Analyze sentiment for the 'title' and 'summary' columns
    df['title_sentiment'] = df['title'].apply(analyze_sentiment)
    df['summary_sentiment'] = df['summary'].apply(analyze_sentiment)
    
    # Save the DataFrame with sentiment analysis to a new CSV file
    df.to_csv('data/cryptocurrency_news_with_sentiment.csv', index=False)
    print('Sentiment analysis completed and saved to data/cryptocurrency_news_with_sentiment.csv')
