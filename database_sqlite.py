"""
Task 3: Database Implementation for Bank Reviews Analysis
Using SQLite for persistent data storage
"""

import sqlite3
import pandas as pd
from datetime import datetime

def create_database():
    """Create SQLite database with proper schema"""
    print("=" * 50)
    print("TASK 3: DATABASE IMPLEMENTATION")
    print("=" * 50)
    
    # Connect to SQLite database (creates if doesn't exist)
    conn = sqlite3.connect('bank_reviews.db')
    cursor = conn.cursor()
    
    print("✅ Connected to SQLite database: bank_reviews.db")
    
    # Create banks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS banks (
        bank_id INTEGER PRIMARY KEY AUTOINCREMENT,
        bank_name TEXT NOT NULL,
        app_name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Create reviews table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        review_id TEXT PRIMARY KEY,
        bank_id INTEGER,
        review_text TEXT NOT NULL,
        rating INTEGER CHECK (rating >= 1 AND rating <= 5),
        review_date DATE NOT NULL,
        sentiment_label TEXT,
        sentiment_score REAL,
        themes TEXT,
        source TEXT DEFAULT 'Google Play',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (bank_id) REFERENCES banks (bank_id)
    )
    ''')
    
    # Create indexes for better query performance
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_bank_id ON reviews(bank_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_rating ON reviews(rating)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_sentiment ON reviews(sentiment_label)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_date ON reviews(review_date)')
    
    conn.commit()
    print("✅ Database tables created successfully")
    print("   - banks (bank information)")
    print("   - reviews (user reviews with sentiment analysis)")
    
    return conn

def insert_banks_data(conn):
    """Insert bank information into banks table"""
    cursor = conn.cursor()
    
    banks = [
        ('CBE', 'CBEBirr Plus'),
        ('BOA', 'Commercial Bank of Ethiopia Mobile'),
        ('DASHEN', 'Dashen Mobile')
    ]
    
    for bank_name, app_name in banks:
        cursor.execute('''
        INSERT OR IGNORE INTO banks (bank_name, app_name) 
        VALUES (?, ?)
        ''', (bank_name, app_name))
    
    conn.commit()
    
    # Get bank IDs for reference
    cursor.execute("SELECT bank_id, bank_name FROM banks")
    banks_data = cursor.fetchall()
    print("✅ Banks data inserted:")
    for bank_id, bank_name in banks_data:
        print(f"   - {bank_name} (ID: {bank_id})")
    
    return {bank_name: bank_id for bank_id, bank_name in banks_data}

def insert_reviews_data(conn, bank_id_map):
    """Insert review data with sentiment analysis"""
    print("\n📊 Loading review data...")
    
    # Load analyzed data
    df_sample = pd.read_csv('bank_reviews_analyzed_sample.csv')
    df_themes = pd.read_csv('bank_reviews_with_themes.csv')
    
    # Merge data
    df_combined = df_sample.merge(df_themes[['review_id', 'themes']], on='review_id', how='left')
    
    # Add bank_id column
    df_combined['bank_id'] = df_combined['bank'].map(bank_id_map)
    
    # Prepare data for insertion
    reviews_to_insert = []
    for _, row in df_combined.iterrows():
        reviews_to_insert.append((
            row['review_id'],
            row['bank_id'],
            str(row['review_text']),
            int(row['rating']),
            row['date'],
            row['sentiment_label'],
            float(row['sentiment_score']),
            str(row['themes']),
            'Google Play'
        ))
    
    # Insert in batches
    cursor = conn.cursor()
    cursor.executemany('''
    INSERT OR IGNORE INTO reviews 
    (review_id, bank_id, review_text, rating, review_date, sentiment_label, 
     sentiment_score, themes, source) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', reviews_to_insert)
    
    conn.commit()
    
    print(f"✅ Reviews inserted: {cursor.rowcount} records")
    return len(reviews_to_insert)

def run_queries(conn):
    """Run SQL queries to verify data and get insights"""
    print("\n" + "=" * 50)
    print("DATABASE VERIFICATION & INSIGHTS")
    print("=" * 50)
    
    queries = {
        "Total Reviews": "SELECT COUNT(*) as total_reviews FROM reviews",
        "Reviews per Bank": """
            SELECT b.bank_name, COUNT(*) as review_count, 
                   AVG(r.rating) as avg_rating
            FROM reviews r 
            JOIN banks b ON r.bank_id = b.bank_id 
            GROUP BY b.bank_name
            ORDER BY avg_rating DESC
        """,
        "Sentiment Distribution": """
            SELECT sentiment_label, COUNT(*) as count,
                   ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM reviews), 2) as percentage
            FROM reviews 
            GROUP BY sentiment_label
            ORDER BY count DESC
        """,
        "Most Common Themes": """
            SELECT themes, COUNT(*) as occurrence
            FROM reviews 
            WHERE themes != 'Other'
            GROUP BY themes
            ORDER BY occurrence DESC
            LIMIT 5
        """,
        "Average Rating by Bank": """
            SELECT b.bank_name, 
                   AVG(r.rating) as avg_rating,
                   MIN(r.rating) as min_rating,
                   MAX(r.rating) as max_rating
            FROM reviews r 
            JOIN banks b ON r.bank_id = b.bank_id 
            GROUP BY b.bank_name
        """
    }
    
    for query_name, query in queries.items():
        print(f"\n📈 {query_name}:")
        df = pd.read_sql_query(query, conn)
        print(df.to_string(index=False))
    
    return True

def export_database_schema(conn):
    """Export database schema for documentation"""
    cursor = conn.cursor()
    
    # Get table schema
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    schema_content = "# Database Schema Documentation\n\n"
    
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        
        schema_content += f"## Table: {table_name}\n"
        schema_content += "| Column | Type | Constraints |\n"
        schema_content += "|--------|------|-------------|\n"
        
        for col in columns:
            col_id, col_name, col_type, not_null, default_val, pk = col
            constraints = []
            if pk: constraints.append("PRIMARY KEY")
            if not_null: constraints.append("NOT NULL")
            if default_val: constraints.append(f"DEFAULT {default_val}")
            
            schema_content += f"| {col_name} | {col_type} | {', '.join(constraints)} |\n"
        
        schema_content += "\n"
    
    # Write to file
    with open('database_schema.md', 'w') as f:
        f.write(schema_content)
    
    print("\n📄 Database schema exported to: database_schema.md")
    return schema_content

def main():
    """Main function to run database setup"""
    try:
        # Step 1: Create database and tables
        conn = create_database()
        
        # Step 2: Insert banks data
        bank_id_map = insert_banks_data(conn)
        
        # Step 3: Insert reviews data
        review_count = insert_reviews_data(conn, bank_id_map)
        
        if review_count == 0:
            print("⚠️ No reviews were inserted. Check your data files.")
            return False
        
        # Step 4: Run verification queries
        run_queries(conn)
        
        # Step 5: Export schema
        export_database_schema(conn)
        
        # Step 6: Close connection
        conn.close()
        
        print("\n" + "=" * 50)
        print("🎉 TASK 3 COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print("Database created: bank_reviews.db")
        print("Schema documented: database_schema.md")
        print(f"Total records: {review_count} reviews")
        print("\nReady for Task 4: Visualization & Insights!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in database setup: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        exit(0)
    else:
        exit(1)