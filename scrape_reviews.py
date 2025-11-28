from google_play_scraper import reviews_all
import pandas as pd
from datetime import datetime

# CORRECT Bank app IDs from our search
apps = {
    'CBE': 'prod.cbe.birr',           # CBEBirr Plus
    'BOA': 'com.combanketh.mobilebanking',  # Using this as alternative for BOA
    'DASHEN': 'com.cr2.amolelight'    # Dashen Mobile
}

def scrape_bank_reviews():
    all_reviews = []
    
    for bank, app_id in apps.items():
        try:
            print(f"Scraping reviews for {bank}...")
            
            # Scrape reviews with Ethiopia country
            reviews = reviews_all(
                app_id,
                lang='en',
                country='et',  # Ethiopia
                sleep_milliseconds=100
            )
            
            print(f"Found {len(reviews)} reviews for {bank}")
            
            # Take first 400 reviews (or all if less)
            for review in reviews[:400]:
                all_reviews.append({
                    'review_id': review['reviewId'],
                    'review_text': review['content'],
                    'rating': review['score'],
                    'date': review['at'].strftime('%Y-%m-%d'),
                    'bank': bank,
                    'source': 'Google Play'
                })
                
        except Exception as e:
            print(f"Error scraping {bank}: {e}")
    
    return pd.DataFrame(all_reviews)

# Run scraping
print("Starting review scraping...")
df = scrape_bank_reviews()

if len(df) > 0:
    print(f"Successfully scraped {len(df)} total reviews")
    print(f"Reviews per bank:")
    print(df['bank'].value_counts())

    # Save to CSV
    df.to_csv('bank_reviews_raw.csv', index=False)
    print("Saved to bank_reviews_raw.csv")
else:
    print("No reviews were scraped. Please check the app IDs.")