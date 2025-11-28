import pandas as pd
from transformers import pipeline
import spacy
from collections import Counter
import re

print("Loading models... This may take a minute...")

# Load models
sentiment_pipeline = pipeline("sentiment-analysis", 
                             model="distilbert-base-uncased-finetuned-sst-2-english")
nlp = spacy.load("en_core_web_sm")

def analyze_sentiment(text):
    try:
        # Limit text length for the model
        clean_text = str(text)[:512]
        result = sentiment_pipeline(clean_text)[0]
        return result['label'], result['score']
    except:
        return 'NEUTRAL', 0.5

def extract_keywords(text):
    doc = nlp(str(text).lower())
    keywords = []
    
    for token in doc:
        if (not token.is_stop and not token.is_punct and 
            token.is_alpha and len(token.text) > 2):
            keywords.append(token.lemma_)
    
    return keywords

# Define theme categories
theme_keywords = {
    'Login Issues': ['login', 'password', 'authenticate', 'access', 'account', 'sign'],
    'Transaction Problems': ['transfer', 'transaction', 'payment', 'send', 'money', 'bill'],
    'App Performance': ['slow', 'crash', 'freeze', 'lag', 'loading', 'bug', 'error'],
    'User Interface': ['interface', 'design', 'layout', 'button', 'navigation', 'ui', 'ux'],
    'Customer Support': ['support', 'help', 'service', 'contact', 'response', 'assistance'],
    'Security': ['secure', 'security', 'safe', 'privacy', 'protection'],
    'Features': ['feature', 'function', 'option', 'tool', 'capability']
}

def assign_theme(text):
    text_lower = str(text).lower()
    themes = []
    
    for theme, keywords in theme_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            themes.append(theme)
    
    return ', '.join(themes) if themes else 'Other'

# Load cleaned data
print("Loading data...")
df = pd.read_csv('bank_reviews_clean.csv')

# Analyze sentiment for first 100 reviews (to save time initially)
print("Analyzing sentiment...")
sample_size = min(100, len(df))  # Start with 100 for testing

sentiments = []
scores = []

for i, review in enumerate(df['review_text'].head(sample_size)):
    if i % 20 == 0:
        print(f"Processed {i}/{sample_size} reviews...")
    label, score = analyze_sentiment(review)
    sentiments.append(label)
    scores.append(score)

# Add sentiment to the sample
df_sample = df.head(sample_size).copy()
df_sample['sentiment_label'] = sentiments
df_sample['sentiment_score'] = scores

# Extract themes for all reviews
print("Extracting themes...")
df['themes'] = df['review_text'].apply(assign_theme)

# Save results
df_sample.to_csv('bank_reviews_analyzed_sample.csv', index=False)
df.to_csv('bank_reviews_with_themes.csv', index=False)

print("\n=== ANALYSIS COMPLETE ===")
print(f"Sentiment analysis done for {sample_size} reviews")
print(f"Theme extraction done for all {len(df)} reviews")

print(f"\nSentiment Distribution (Sample):")
print(df_sample['sentiment_label'].value_counts())

print(f"\nTop Themes (All Reviews):")
print(df['themes'].value_counts().head(10))

print(f"\nFiles saved:")
print("- bank_reviews_analyzed_sample.csv (with sentiment)")
print("- bank_reviews_with_themes.csv (with themes)")