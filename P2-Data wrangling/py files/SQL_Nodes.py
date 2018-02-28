import sqlite3
import csv
import pprint

database = 'C:/sqlite_windows/osm.db'

con = sqlite3.connect(database)
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS nodes; ''')
con.commit()

cur.execute("CREATE TABLE nodes (id INTEGER PRIMARY KEY NOT NULL, lat REAL, lon REAL, user TEXT, uid INTEGER, version TEXT, changeset INTEGER, timestamp DATE);") # use your column names here
con.commit()
with open('C:/sqlite_windows/nodes.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"),i['lat'].decode("utf-8"),i['lon'].decode("utf-8"),              i['user'].decode("utf-8"),i['uid'].decode("utf-8"),i['version'].decode("utf-8"),              i['changeset'].decode("utf-8"), i['timestamp'].decode("utf-8")) for i in dr]


cur.executemany("INSERT INTO nodes (id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?,?,?);", to_db)
con.commit()
con.close()
