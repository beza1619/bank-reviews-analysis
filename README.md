# Bank Mobile App Reviews Analysis

## Project Overview
This project analyzes customer satisfaction with mobile banking apps for three Ethiopian banks:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA) 
- Dashen Bank

## Business Objective
Omega Consultancy is supporting banks to improve their mobile apps to enhance customer retention and satisfaction by analyzing user reviews from Google Play Store.

## Project Structure
bank-reviews-analysis/
├── scrape_reviews.py # Web scraping script
├── preprocess.py # Data preprocessing
├── sentiment_analysis.py # Sentiment & theme analysis
├── find_apps.py # App ID discovery
├── database_setup.py # Database implementation
├── bank_reviews_clean.csv # Cleaned dataset (1200+ reviews)
├── bank_reviews_analyzed_sample.csv # Sentiment analysis sample
├── bank_reviews_with_themes.csv # Thematic analysis
├── requirements.txt # Python dependencies
└── README.md # This file

## Data Collection
- **Source**: Google Play Store
- **Total Reviews**: 1,200+ (400+ per bank)
- **Data Points**: Review text, rating, date, bank, source
- **Time Period**: Recent user reviews

## Analysis Features
1. **Sentiment Analysis**: Positive/Negative/Neutral classification using distilbert model
2. **Thematic Analysis**: Identifying common topics and issues (Login, Transactions, Performance, etc.)
3. **Rating Distribution**: Star rating analysis per bank
4. **Trend Analysis**: Review patterns over time

## Technologies Used
- Python 3.x
- Google Play Scraper
- Transformers (Hugging Face) for sentiment analysis
- spaCy for NLP processing
- pandas for data manipulation
- PostgreSQL for data storage

## Installation & Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run data collection
python scrape_reviews.py

# Preprocess data
python preprocess.py

# Analyze sentiment and themes
python sentiment_analysis.py