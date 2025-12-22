# Source - https://stackoverflow.com/a
# Posted by flokk, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-22, License - CC BY-SA 4.0

import sqlite3

DB_PATH = r"/home/konrad/.local/share/Anki2/User 1/collection.anki2"

connection = sqlite3.connect(DB_PATH)
connection.row_factory = sqlite3.Row
cursor = connection.execute("select * from notetypes")
# instead of cursor.description:
row = cursor.fetchone()
names = row.keys()
print(names)
