import sqlite3

# Path to your SQLite database
DB_PATH = r"/home/konrad/.local/share/Anki2/User 1/collection.anki2"

# Connect to the database
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Query to get all table names
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()

# Print table names
for table in tables:
    print(table[0])

# Close the connection
conn.close()
