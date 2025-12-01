import sqlite3
import pandas as pd

print("Updating database with complete sentiment analysis...")

# Load completely analyzed data
df = pd.read_csv('bank_reviews_completely_analyzed.csv')
print(f"Loaded {len(df)} completely analyzed reviews")

# Connect to database
conn = sqlite3.connect('bank_reviews_complete.db')
cursor = conn.cursor()

# Update existing records with sentiment
bank_id_map = {'CBE': 1, 'BOA': 2, 'DASHEN': 3}
updated = 0

for _, row in df.iterrows():
    cursor.execute('''
    UPDATE reviews 
    SET sentiment_label = ?, sentiment_score = ?, themes = ?
    WHERE review_id = ?
    ''', (row['sentiment_label'], row['sentiment_score'], row['themes'], row['review_id']))
    updated += 1
    
    if updated % 200 == 0:
        print(f"  Updated {updated}/{len(df)}...")

conn.commit()

# Verify
cursor.execute("SELECT COUNT(*) FROM reviews WHERE sentiment_label != 'NEUTRAL'")
analyzed = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM reviews")
total = cursor.fetchone()[0]

print(f"\n✅ DATABASE UPDATED!")
print(f"   Total reviews: {total}")
print(f"   With sentiment: {analyzed}")
print(f"   Coverage: {analyzed/total*100:.1f}%")

conn.close()