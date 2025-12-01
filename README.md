# Bank Mobile App Reviews Analysis
**Omega Consultancy Data Analytics Project**

---
## Business Objective
Omega Consultancy is supporting banks to improve their mobile apps to enhance customer retention and satisfaction by analyzing user reviews from Google Play Store for three Ethiopian banks:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA) 
- Dashen Bank

---

## Dataset Overview
Collected from Google Play Store with the following attributes:
- **Review Text**: User feedback in English
- **Rating**: 1–5 stars
- **Date**: Review posting date
- **Bank/App Name**: Identifier for each banking application
- **Source**: Google Play Store

**Minimum Requirement**: 400 reviews per bank (1,200 total) - **✓ EXCEEDED**

---

## Project Deliverables Completed

### Task 1: Data Collection and Preprocessing ✓
**Minimum Essential:** 400 reviews per bank (1,200 total)

**Files:**
- `scrape_reviews.py` - Main scraping script using google-play-scraper
- `preprocess.py` - Data cleaning and preprocessing
- `bank_reviews_clean.csv` - Cleaned dataset with 1,200+ reviews

**Results:**
- ✓ 1,200+ reviews collected (400 per bank)
- ✓ Data cleaned with <5% errors
- ✓ Dates normalized to YYYY-MM-DD format

---

### Task 2: Sentiment and Thematic Analysis ✓
**Minimum Essential:** Sentiment scores for 400 reviews, 2 themes per bank

**Files:**
- `sentiment_analysis.py` - DistilBERT-based sentiment analysis
- `complete_sentiment.py` - Full coverage sentiment analysis
- `bank_reviews_completely_analyzed.csv` - All reviews with sentiment scores

**Sentiment Analysis:**
- ✓ Model: distilbert-base-uncased-finetuned-sst-2-english
- ✓ Coverage: 100% of reviews analyzed (exceeds 90% requirement)
- ✓ Output: Sentiment label (POSITIVE/NEGATIVE/NEUTRAL) + confidence score

**Thematic Analysis:**
- ✓ 7 key themes identified per bank:
  1. Login Issues
  2. Transaction Problems
  3. App Performance
  4. Customer Support
  5. Security Concerns
  6. Feature Requests
  7. User Interface

---

### Task 3: Store Cleaned Data in PostgreSQL ✓
**Minimum Essential:** PostgreSQL database with both tables, 400+ reviews inserted

**Files:**
- `database_sqlite.py` - SQLite database implementation
- `postgres_implementation.py` - PostgreSQL setup script
- `bank_reviews_complete.db` - SQLite database file
- `database_schema.md` - Database schema documentation

**Database Schema:**
```sql
-- Banks Table
bank_id (PRIMARY KEY), bank_name, app_name

-- Reviews Table  
review_id (PRIMARY KEY), bank_id (FOREIGN KEY), review_text, 
rating, review_date, sentiment_label, sentiment_score, source
```

**Results:**
- ✓ Database created with 1,200+ review entries
- ✓ Proper table relationships and indexing
- ✓ SQL queries for data verification implemented

---

### Task 4: Insights and Recommendations ✓
**Minimum Essential:** 1 driver, 1 pain point per bank; 2 plots; 4-page final report

**Visualizations Created:**
1. `viz1_ratings.png` - Rating distribution by bank
2. `viz2_sentiment.png` - Sentiment analysis dashboard
3. `viz3_comparison.png` - Bank comparison charts
4. `visualization4_wordcloud.png` - Common themes word cloud

**Key Insights per Bank:**

**CBE (Commercial Bank of Ethiopia):**
- **Driver**: High overall satisfaction (4.14 average rating)
- **Pain Point**: Transaction speed during peak hours
- **Recommendation**: Optimize server capacity

**BOA (Bank of Abyssinia):**
- **Driver**: Reliable basic functionality
- **Pain Point**: Login authentication issues
- **Recommendation**: Implement biometric login

**Dashen Bank:**
- **Driver**: Modern user interface
- **Pain Point**: Application stability and crashes
- **Recommendation**: Performance optimization updates

**Final Report**: 10-page comprehensive analysis with all findings and recommendations

---

## Technical Implementation

### Technology Stack
- **Python 3.x**: Primary programming language
- **Google Play Scraper**: Official review collection
- **Transformers (Hugging Face)**: State-of-the-art NLP models
- **SQLite/PostgreSQL**: Database management
- **Matplotlib/Seaborn**: Data visualization
- **spaCy**: Advanced text processing

### Repository Structure
```
bank-reviews-analysis/
├── data/                    # Collected and processed data
│   ├── bank_reviews_clean.csv
│   ├── bank_reviews_completely_analyzed.csv
│   └── app_search_results.csv
├── scripts/                 # Analysis pipeline
│   ├── scrape_reviews.py
│   ├── preprocess.py
│   ├── sentiment_analysis.py
│   └── database_sqlite.py
├── database/               # Database files
│   ├── bank_reviews_complete.db
│   └── database_schema.md
├── visualizations/         # Generated charts
│   ├── viz1_ratings.png
│   ├── viz2_sentiment.png
│   ├── viz3_comparison.png
│   └── visualization4_wordcloud.png
├── docs/                  # Documentation
│   ├── README.md
│   └── requirements.txt
└── notebooks/             # Jupyter notebooks
    └── Bank_Reviews_Analysis.ipynb
```

### Installation and Setup
```bash
# 1. Clone repository
git clone https://github.com/beza1619/bank-reviews-analysis.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run analysis pipeline
python scrape_reviews.py    # Data collection
python preprocess.py        # Data cleaning
python sentiment_analysis.py # Sentiment analysis
python database_sqlite.py   # Database setup
```

---

## GitHub Repository
**URL**: https://github.com/beza1619/bank-reviews-analysis

**Branch Structure:**
- `main` - Complete project with all deliverables
- `task-1` - Interim submission branch

**Commit History:**
- Regular commits with descriptive messages
- Proper branching strategy for each task
- All code documented and reproducible

---

## Ethical Considerations
- User reviews collected ethically via official API
- No personal identifiable information stored
- Analysis focused on aggregate trends, not individual users
- Review biases acknowledged in final report