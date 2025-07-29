#!/usr/bin/env python3
"""
Script to create SQLite database from NFL CSV files
"""

import sqlite3
import pandas as pd
import os

def create_nfl_database():
    """Create SQLite database from the three CSV files"""
    
    # Database file name
    db_file = 'nfl_data.db'
    
    # Remove existing database if it exists
    if os.path.exists(db_file):
        os.remove(db_file)
    
    # Create connection to SQLite database
    conn = sqlite3.connect(db_file)
    
    try:
        # Read and load eagles.csv
        print("Loading eagles.csv...")
        eagles_df = pd.read_csv('eagles.csv')
        eagles_df.to_sql('eagles', conn, index=False, if_exists='replace')
        print(f"✓ Created 'eagles' table with {len(eagles_df)} rows")
        
        # Read and load players_2024.csv
        print("Loading players_2024.csv...")
        players_df = pd.read_csv('players_2024.csv')
        players_df.to_sql('players_2024', conn, index=False, if_exists='replace')
        print(f"✓ Created 'players_2024' table with {len(players_df)} rows")
        
        # Read and load teams.csv
        print("Loading teams.csv...")
        teams_df = pd.read_csv('teams.csv')
        teams_df.to_sql('teams', conn, index=False, if_exists='replace')
        print(f"✓ Created 'teams' table with {len(teams_df)} rows")
        
        # Verify tables were created
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print(f"\nDatabase '{db_file}' created successfully!")
        print("Tables in database:")
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
            count = cursor.fetchone()[0]
            print(f"  - {table[0]}: {count} rows")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_nfl_database()
