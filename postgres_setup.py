import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Create PostgreSQL database
engine = create_engine('postgresql://postgres:admin123@localhost:5432/bank_reviews_pg')

# Load data from SQLite and transfer
import sqlite3
conn_sqlite = sqlite3.connect('bank_reviews_complete.db')
df = pd.read_sql_query("SELECT * FROM reviews", conn_sqlite)
df.to_sql('reviews', engine, if_exists='replace', index=False)
print("✅ Data migrated to PostgreSQL")