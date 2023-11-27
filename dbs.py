import sqlite3



db = sqlite3.connect("db.sqlit3")

cur = db.cursor()

# query = db.execute("CREATE TABLE etudiant(name VARCHAR(50), poids INT)")

# rows = db.execute("INSERT INTO etudiant VALUES (?,?)",("Abdoue",545))


rows = db.execute("SELECT rowid,* FROM etudiant")

for row in rows.fetchall():
    print(row)

db.commit()
db.close()