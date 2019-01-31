"""
# 파이썬 - SQLite 연동 절차
    import sqlite3           # 파이썬3에는 SQLite 라이브러리가 기본 탑재

    conn = sqlite3.connect('test.db')        # 1. 커넥션(connection) 열기
    cursor = conn.cursor()                   # 2. 커서(cursor) 열기

    cursor.execute()                         # 3. 커서를 이용하여 데이터
                                             #    추가/조회/수정/삭제하기

    cursor.close()                           # 4. 커서 닫기
    conn.close()                             # 5. 커넥션 닫기

"""


# test.db  파일 안에 phonebook 테이블 생성

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE PHONEBOOK(
NAME CHAR(32), PHONE CHAR(32), EMAIL CHAR(64) PRIMARY KEY)
""")

cursor.close()
conn.close()









