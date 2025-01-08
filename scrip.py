import sqlite3
conn = sqlite3.connect('database/hotel.db')
with open('database/schema.sql', 'r') as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
exit()
