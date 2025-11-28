import pandas as pd
import numpy as np

def preprocess_reviews():
    # Load raw data
    df = pd.read_csv('bank_reviews_raw.csv')
    
    print(f"Original data: {len(df)} reviews")
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['review_id'])
    print(f"After removing duplicates: {len(df)} reviews")
    
    # Handle missing data
    df = df.dropna(subset=['review_text'])
    print(f"After removing empty reviews: {len(df)} reviews")
    
    # Fill missing ratings with median
    if df['rating'].isna().any():
        df['rating'] = df['rating'].fillna(df['rating'].median())
        print("Filled missing ratings with median")
    
    # Ensure date format
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    
    # Save cleaned data
    df.to_csv('bank_reviews_clean.csv', index=False)
    
    print(f"Final cleaned data: {len(df)} reviews")
    print(f"Reviews per bank:")
    print(df['bank'].value_counts().to_dict())
    
    # Show some sample data
    print("\nSample of cleaned data:")
    print(df.head(3))

if __name__ == "__main__":
    preprocess_reviews()