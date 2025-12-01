import pandas as pd
import sqlite3

print('='*60)
print('EXACT DATA VERIFICATION')
print('='*60)

# Check 1: bank_reviews_clean.csv
try:
    df_clean = pd.read_csv('bank_reviews_clean.csv')
    clean_count = len(df_clean)
    clean_banks = df_clean['bank'].value_counts()
    print(f'1. bank_reviews_clean.csv: {clean_count} total reviews')
    print(f'   Bank distribution:')
    for bank, count in clean_banks.items():
        print(f'     {bank}: {count} reviews')
except Exception as e:
    print(f'1. ❌ bank_reviews_clean.csv error: {e}')

print()

# Check 2: bank_reviews_analyzed_sample.csv
try:
    df_sample = pd.read_csv('bank_reviews_analyzed_sample.csv')
    sample_count = len(df_sample)
    sample_banks = df_sample['bank'].value_counts()
    print(f'2. bank_reviews_analyzed_sample.csv: {sample_count} analyzed reviews')
    print(f'   Bank distribution:')
    for bank, count in sample_banks.items():
        print(f'     {bank}: {count} reviews')
except Exception as e:
    print(f'2. ❌ bank_reviews_analyzed_sample.csv error: {e}')

print()

# Check 3: Database
try:
    conn = sqlite3.connect('bank_reviews_complete.db')
    cursor = conn.cursor()
    cursor.execute('SELECT bank_name, COUNT(*) FROM reviews r JOIN banks b ON r.bank_id = b.bank_id GROUP BY bank_name')
    db_counts = cursor.fetchall()
    cursor.execute('SELECT COUNT(*) FROM reviews')
    db_total = cursor.fetchone()[0]
    conn.close()
    
    print(f'3. Database: {db_total} total reviews')
    print(f'   Bank distribution:')
    for bank, count in db_counts:
        print(f'     {bank}: {count} reviews')
except Exception as e:
    print(f'3. ❌ Database error: {e}')

print()
print('='*60)
print('REQUIREMENT: 400+ reviews per bank (1200+ total)')
print('='*60)

# Final assessment
if 'clean_count' in locals() and clean_count >= 1200:
    print('✅ CSV FILE: HAS 1200+ TOTAL REVIEWS')
    if all(count >= 400 for count in clean_banks.values):
        print('✅ CSV FILE: HAS 400+ PER BANK')
    else:
        print('❌ CSV FILE: MISSING 400+ PER BANK')
else:
    print('❌ CSV FILE: MISSING 1200+ TOTAL REVIEWS')