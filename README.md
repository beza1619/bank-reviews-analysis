# Bank Mobile App Reviews Analysis

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

## Current Status
- ✅ **Task 1**: Data Collection & Preprocessing (Complete)
- ✅ **Task 2**: Partial Sentiment & Thematic Analysis
- 🚧 **Task 3**: Database Implementation (In Progress)

## Data Collection
- **Source**: Google Play Store
- **Total Reviews**: 1,200+ (400+ per bank)
- **Banks**: CBE, BOA, Dashen Bank
- **Average Ratings**: CBE (4.18), BOA (4.13), Dashen (4.01)

## Technologies
- Python, Transformers, spaCy, PostgreSQL
- Google Play Scraper for data collection

## Usage
bash
pip install -r requirements.txt
python scrape_reviews.py
python preprocess.py
python sentiment_analysis.py