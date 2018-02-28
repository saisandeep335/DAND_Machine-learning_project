from pprint import pprint 
import sqlite3

def sqlquery(query):
    database = 'C:/sqlite_windows/osm.db'
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(query)
    pprint(cur.fetchall())
    con.close()
