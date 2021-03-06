import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
UPDATE PHONEBOOK SET PHONE=?, EMAIL=? WHERE NAME=?
""", ('010-5555-5555', 'abc@abc.com', '강감찬'))

conn.commit()

cursor.execute("""
select name, phone, email from phonebook where name=?
""", ('강감찬',))

rows = cursor.fetchall()

for row in rows:
    print("NAME:{0}, PHONE:{1}, EMAIL:{2}".format(row[0], row[1], row[2]))

cursor.close()
conn.close()







