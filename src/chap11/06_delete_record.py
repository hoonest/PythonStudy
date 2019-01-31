import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
delete from phonebook where email=?
""", ('abc@abc.com', ))

conn.commit()

cursor.execute("select * from phonebook")

rows = cursor.fetchall()
for row in rows:
    print("NAME:{0}, PHONE:{1}, EMAIL:{2}".format(row[0], row[1], row[2]))

cursor.close()
conn.close()








