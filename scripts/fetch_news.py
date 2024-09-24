import requests
import pandas as pd
import os
from datetime import datetime
import requests
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')  # Load your API key from .env file

def fetch_news():
    url = f'https://api.newscatcherapi.com/v2/search?q=cryptocurrency&lang=en'
    headers = {'x-api-key': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        return articles
    else:
        print(f'Error fetching news: {response.status_code}')
        return []

if __name__ == '__main__':
    news_articles = fetch_news()
    df = pd.DataFrame(news_articles)
    df.to_csv('data/cryptocurrency_news.csv', index=False)
    print('News articles fetched and saved to data/cryptocurrency_news.csv')

