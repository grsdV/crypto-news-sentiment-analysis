# Import packages
# Default packages
import time
import csv
import os
import json
from datetime import datetime, timedelta  # Importing timedelta for date manipulation

# Preinstalled packages
import requests  # HTTP requests
import pandas as pd  # Data manipulation and analysis
from dotenv import load_dotenv  # Load environment variables

# Load environment variables from .env file
load_dotenv()

# Your API key
API_KEY = os.getenv('API_KEY')  # Load your API key

# Check if the API key was loaded correctly
if API_KEY is None:
    raise ValueError("API key not found. Please set it in the .env file.")

# Define desired work folder where you want to save your .csv files
os.chdir('/path/to/your/project/folder')  # Change this to your desired path

# URL of the News API
base_url = 'https://api.newscatcherapi.com/v2/search'

# Set headers for the API call
headers = {'x-api-key': API_KEY}

def fetch_news():
    # Define parameters for the API call
    params = {
        'q': 'cryptocurrency',  # Keyword/keywords you're searching for
        'from': (datetime.now() - timedelta(days=5 * 365)).strftime('%Y-%m-%d'),  # From which point in time to start the search. For example 5 years back
        'to': datetime.now().strftime('%Y-%m-%d'),  # Current date
        'lang': 'en',  # Only English articles
        'countries': 'US,CA,GB,DE,FR,AU',  # Example country codes
        'page_size': 100,  # Maximum articles per request
        'sort_by': 'relevancy',  # Sort by relevancy
        'published_date_precision': 'full',  # Ensure precision in published date
        'sources': 'businessinsider.com,forbes.com,apnews.com,yahoo.com',  # Example sources
    }

    all_news_articles = []
    unique_ids = set()  # Use a set for faster lookup for unique IDs

    print(f'Query in use => {str(params)}')

    params['page'] = 1  # Initialize page parameter
    while True:
        time.sleep(1)  # Wait for 1 second between each call

        # Make the API call
        response = requests.get(base_url, headers=headers, params=params)
        results = response.json()

        if response.status_code == 200:
            print(f'Done for page number => {params["page"]}')

            # Adding parameters to each result
            for article in results['articles']:
                if article['_id'] not in unique_ids:  # Check for duplicates
                    unique_ids.add(article['_id'])
                    article['used_params'] = str(params)  # Add parameters to article
                    all_news_articles.append(article)

            # Check if there are more pages
            if len(results['articles']) < params['page_size']:
                print("All articles have been extracted")
                break
            else:
                params['page'] += 1  # Increment page number for the next batch
                print(f'Proceed extracting next batch of articles.')
        else:
            print(f"ERROR: API call failed with status code {response.status_code}: {results.get('message', '')}")
            break

    print(f'Number of extracted articles => {len(all_news_articles)}')
    return all_news_articles

def save_to_csv(data):
    # Save data to CSV from a list of dictionaries
    if data:
        field_names = list(data[0].keys())
        with open('extracted_news_articles.csv', 'w', encoding="utf-8", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names, delimiter=";")
            writer.writeheader()
            writer.writerows(data)

        # Alternatively, create a pandas table and save to CSV
        pandas_table = pd.DataFrame(data)
        pandas_table.to_csv('extracted_news_articles_pandas.csv', encoding='utf-8', sep=';', index=False)

        print('Data has been successfully saved to extracted_news_articles.csv and extracted_news_articles_pandas.csv.')

if __name__ == '__main__':
    articles = fetch_news()
    save_to_csv(articles)
