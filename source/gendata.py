import sqlite3 

conn = sqlite3.connect("site.db")

c = conn.cursor()

c.execute("""
	CREATE TABLE showman(
	id INTEGER PRIMARY KEY,
	content TEXT,
	emotion TEXT,
	image TEXT,
	itype TEXT
	)
	""")

conn.commit()

print('Database created!')

conn.close()