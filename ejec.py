import sqlite3
import pandas as pd

def load_data():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    with open("create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

    return conn, cur
    
    
if (__name__ =="__main__"):
    conn, cur = load_data()
    
    with open("pregunta_13.sql", encoding="utf-8") as file:
        query = file.read()
        
    res = pd.read_sql_query(query, conn).to_dict()
    print(res)