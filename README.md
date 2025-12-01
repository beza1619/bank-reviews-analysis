# Bank Mobile App Reviews Analysis

## Business Objective
Omega Consultancy is supporting banks to improve their mobile apps by analyzing user reviews from Google Play Store for three Ethiopian banks:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA) 
- Dashen Bank

---

## TASK 1: DATA COLLECTION & PREPROCESSING ✅ COMPLETED

### **Files:**
- `scrape_reviews.py` - Main scraping script
- `find_apps.py` - App ID discovery utility
- `preprocess.py` - Data cleaning and preprocessing
- `bank_reviews_raw.csv` - Raw scraped data
- `bank_reviews_clean.csv` - Cleaned dataset (1,200+ reviews)

### **Results:**
- ✓ 1,200+ reviews collected (400+ per bank)
- ✓ Data cleaned: duplicates removed, missing values handled
- ✓ Average ratings: CBE (4.18), BOA (4.13), Dashen (4.01)

---

## TASK 2: SENTIMENT & THEMATIC ANALYSIS ✅ COMPLETED

### **Files:**
- `sentiment_analysis.py` - Sentiment analysis using DistilBERT
- `bank_reviews_analyzed_sample.csv` - 100+ reviews with sentiment labels
- `bank_reviews_with_themes.csv` - Reviews with thematic analysis

### **Results:**
- ✓ 100+ reviews analyzed for sentiment
- ✓ Sentiment distribution: 67% Positive, 33% Negative
- ✓ 7 key themes identified: Login Issues, Transaction Problems, App Performance, Customer Support, Security, Feature Requests, User Interface

---

## TASK 3: DATABASE IMPLEMENTATION ✅ COMPLETED

### **Files:**
- `database_sqlite.py` - SQLite database setup script
- `bank_reviews.db` - SQLite database file
- `database_schema.md` - Database schema documentation

### **Results:**
- ✓ SQLite database created with 2 tables: `banks` and `reviews`
- ✓ 100+ reviews stored with sentiment scores
- ✓ Database schema properly designed with indexes
- ✓ SQL queries for data verification implemented

---

## TASK 4: VISUALIZATION & INSIGHTS ✅ COMPLETED

### **Files:**
- `visualization1_rating_dist.png` - Rating distribution chart
- `visualization2_sentiment.png` - Sentiment analysis chart
- `visualization3_bank_comparison.png` - Bank comparison dashboard
- `visualization4_wordcloud.png` - Common themes word cloud
- `Bank_Reviews_Analysis.ipynb` - Complete Jupyter notebook

### **Results:**
- ✓ 4 professional visualizations created
- ✓ Key insights extracted from analysis
- ✓ Bank-specific recommendations generated

---

## PROJECT METRICS SUMMARY

| Metric | Result |
|--------|--------|
| Total Reviews Collected | 1,200+ |
| Reviews Analyzed | 100+ |
| Average Rating | 4.14 ⭐ |
| Positive Sentiment | 67% |
| Database Records | 100+ |
| Visualizations Created | 4 |

---

## KEY FINDINGS

### **Common Issues Identified:**
1. **Transaction Speed** - Slow transfers during peak hours
2. **Login Problems** - Authentication and password issues
3. **App Performance** - Crashes and slow loading times
4. **Customer Support** - Response time and service quality

### **Bank-Specific Insights:**
- **CBE**: Highest ratings, focus on transaction optimization
- **BOA**: Login experience improvements needed
- **Dashen**: App stability and performance enhancements

---

## TECHNOLOGIES USED

- **Python 3.x** - Primary programming language
- **Google Play Scraper** - Review data collection
- **Transformers (DistilBERT)** - Sentiment analysis
- **SQLite** - Database storage
- **Matplotlib/Seaborn** - Data visualization
- **pandas/numpy** - Data manipulation

---

## INSTALLATION & USAGE

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run Task 1: Data collection
python scrape_reviews.py
python preprocess.py

# 3. Run Task 2: Analysis
python sentiment_analysis.py

# 4. Run Task 3: Database
python database_sqlite.py

# 5. Visualizations are automatically created