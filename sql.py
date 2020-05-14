import sqlite3

import time

def init_DB():
    conn = sqlite3.connect('data.db')
    conn.execute('''CREATE TABLE EMAILS(
    EMAIL VARCHAR(20) PRIMARY KEY     NOT NULL,
    NAME           VARCHAR(20),
    SURNAME            VARCHAR(20),
    TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP);''')
def reset_DB():
    conn = sqlite3.connect('data.db')
    conn.execute(''' DROP TABLE EMAILS ''')

def add_Email(email, name, surname):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    query = """INSERT INTO EMAILS (EMAIL, NAME, SURNAME) VALUES (?,?,?)"""
    c.execute(query,(email, name, surname))
    conn.commit()
    conn.close()
