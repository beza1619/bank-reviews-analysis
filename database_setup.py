import pandas as pd
from sqlalchemy import create_engine

print("Starting database setup...")

try:
    # Connect to PostgreSQL - use the password YOU set during installation
    engine = create_engine('postgresql://postgres:admin123@localhost:5432/bank_reviews')
    
    # Load our analyzed data
    df_sample = pd.read_csv('bank_reviews_analyzed_sample.csv')
    df_themes = pd.read_csv('bank_reviews_with_themes.csv')
    
    # Merge data
    df_combined = df_sample.merge(df_themes[['review_id', 'themes']], on='review_id', how='left')
    
    print(f"Loaded {len(df_combined)} reviews for database")
    
    # Create banks table and insert data
    banks_data = pd.DataFrame({
        'bank_id': [1, 2, 3],
        'bank_name': ['CBE', 'BOA', 'DASHEN'],
        'app_name': ['CBEBirr Plus', 'Commercial Bank Mobile', 'Dashen Mobile']
    })
    
    banks_data.to_sql('banks', engine, if_exists='replace', index=False)
    print("✅ Banks table created")
    
    # Prepare reviews data
    bank_id_map = {'CBE': 1, 'BOA': 2, 'DASHEN': 3}
    df_combined['bank_id'] = df_combined['bank'].map(bank_id_map)
    
    # Insert reviews
    df_combined[['review_id', 'bank_id', 'review_text', 'rating', 'date', 
                'sentiment_label', 'sentiment_score', 'themes', 'source']].to_sql(
        'reviews', engine, if_exists='replace', index=False)
    
    print("✅ Reviews table created and data inserted")
    
    # Verify
    result = pd.read_sql("SELECT COUNT(*) as total_reviews FROM reviews", engine)
    print(f"✅ Database verified: {result['total_reviews'][0]} reviews in database")
    
    # Show summary
    summary = pd.read_sql("""
        SELECT b.bank_name, COUNT(*) as reviews, AVG(r.rating) as avg_rating
        FROM reviews r 
        JOIN banks b ON r.bank_id = b.bank_id 
        GROUP BY b.bank_name
    """, engine)
    
    print("\n📊 DATABASE SUMMARY:")
    print(summary)
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure PostgreSQL is running")
    print("2. Check if password 'admin123' is correct")
    print("3. Try using pgAdmin to verify connection")