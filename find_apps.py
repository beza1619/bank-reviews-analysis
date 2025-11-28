from google_play_scraper import search
import pandas as pd

# Search for Ethiopian banking apps
banks = [
    'Commercial Bank of Ethiopia',
    'Bank of Abyssinia', 
    'Dashen Bank'
]

def find_banking_apps():
    app_results = []
    
    for bank in banks:
        print(f"Searching for: {bank}")
        try:
            results = search(
                bank,
                lang='en',
                country='et'  # Ethiopia
            )
            
            for result in results[:3]:  # Top 3 results
                app_results.append({
                    'bank': bank,
                    'app_name': result['title'],
                    'app_id': result['appId'],
                    'score': result['score'],
                    'installs': result['installs']
                })
                print(f"  ✅ Found: {result['title']}")
                print(f"     ID: {result['appId']}")
                print(f"     Rating: {result['score']}")
                
        except Exception as e:
            print(f"Error searching for {bank}: {e}")
    
    return pd.DataFrame(app_results)

# Run search
print("Searching for banking apps...")
df = find_banking_apps()
df.to_csv('app_search_results.csv', index=False)
print("\nSearch complete! Check app_search_results.csv")