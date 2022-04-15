import sqlite3 as sql
"""""
con = sql.connect("database.db")
cur = con.cursor()
cur.execute("select * from question")
rows = cur.fetchall()
print(len(rows))
for x in rows:
    print(x[0])
"""

Id = '123B9'
Content = 'What can run, but never walks; has a mouth, but never talks; has a head, but never weeps; has a bed, but never sleeps?'
Ans = 'River'
PossibleAns = 'River,Clouds,The Sun,a mountain'
Hint = 'Upcoming'
conn = sql.connect('Question.db')



conn.execute("""INSERT INTO Question(ID, CONTENT, ANSWER, POSSIBLE_ANSWER, HINT) 
               VALUES (?,?,?,?,?);""", (Id, Content, Ans, PossibleAns, Hint))

conn.commit()
conn.close()