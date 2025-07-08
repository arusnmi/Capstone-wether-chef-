import pandas as pd
import sqlite3

csv_file1 = 'recipes_with_categories.csv'
db_file1 = 'recpies.db'
table_name = 'my_table'

# Read CSV into DataFrame
df = pd.read_csv(csv_file1)

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_file1)

# Write the DataFrame to the SQLite table
df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.close()