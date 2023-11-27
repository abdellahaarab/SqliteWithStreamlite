import streamlit as st
import pandas as pd
from MyClass import MyClass
import sqlite3



db = sqlite3.connect("db.sqlit3")

cur = db.cursor()

# query = db.execute("CREATE TABLE etudiant(name VARCHAR(50), poids INT)")

# rows = db.execute("INSERT INTO etudiant VALUES (?,?)",("Abdoue",545))


rows = db.execute("SELECT rowid,* FROM etudiant")

for row in rows.fetchall():
    print(row)



st.header("Home Page")

for i in range(6):
    st.text(f"Chiox {i}")

my1 = MyClass("Abdeou",566)
st.text(my1.afficher())


for row in rows.fetchall():
   st.text(row)

st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("homes.csv")
st.line_chart(df)


db.commit()
db.close()