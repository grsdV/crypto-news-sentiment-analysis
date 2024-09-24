# crypto-news-sentiment-analysis
A project to analyze cryptocurrency news sentiment using the NewsCatcher API and its impact on cryptocurrency price movements

## Overview
This project leverages the NewsCatcher API to fetch cryptocurrency-related news and applies sentiment analysis to the articles, titles, and summaries.The goal is to determine how news sentiment affects the cryptocurrency market, using regression analysis to link sentiment scores with price movements.

## Project Structure
- **data/**: Folder containing the fetched news articles, sentiment scores, and cryptocurrency price data.
- **scripts/**: Python scripts for fetching news, performing sentiment analysis, and processing data.
- **notebooks/**: Jupyter notebooks showcasing sentiment analysis and price correlation.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/crypto-news-sentiment-analysis.git
2. **Install dependencies**:
   - Navigate to the project directory:
     ```bash
     cd crypto-news-sentiment-analysis
     ```
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # On macOS/Linux
     venv\Scripts\activate  # On Windows
     ```
   - Install required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Setup API Keys**:
   - Obtain your API key from [NewsCatcher API](https://newscatcherapi.com/) and create a `.env` file in the root directory with the following content:
     ```
     NEWS_API_KEY=your_api_key
     ```

4. **Run the Project**:
   - To fetch the latest cryptocurrency news, run:
     ```bash
     python scripts/fetch_news.py
     ```
   - To perform sentiment analysis on the news data, run:
     ```bash
     python scripts/sentiment_analysis.py
     ```

## Sentiment Analysis
Sentiment analysis in this project is performed using libraries such as `VADER` and `TextBlob`. The sentiment score is categorized as positive, negative, or neutral for each article fetched from the NewsCatcher API.

## Credits
This project uses the [NewsCatcher API](https://newscatcherapi.com/) to retrieve real-time cryptocurrency news articles for sentiment analysis.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
