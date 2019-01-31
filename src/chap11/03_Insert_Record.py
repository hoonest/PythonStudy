import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO PHONEBOOK(NAME, PHONE, EMAIL)
VALUES(?,?,?)
""", ('홍길동', '010-1111-1111', 'aaa@aaa.com'))

id = cursor.lastrowid
print(id)

cursor.execute("""
INSERT INTO PHONEBOOK(NAME, PHONE, EMAIL)
VALUES(?,?,?)
""", ('이순신', '010-2222-2222', 'bbb@bbb.com'))

id = cursor.lastrowid
print(id)

cursor.execute("""
INSERT INTO PHONEBOOK(NAME, PHONE, EMAIL)
VALUES(?,?,?)
""", ('강감찬', '010-3333-3333', 'ccc@ccc.com'))

id = cursor.lastrowid
print(id)

conn.commit()

cursor.close()
conn.close()