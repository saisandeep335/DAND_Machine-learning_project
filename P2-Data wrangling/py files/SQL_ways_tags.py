database = 'C:/sqlite_windows/osm.db'

con = sqlite3.connect(database)
cur = con.cursor()


cur.execute('''DROP TABLE IF EXISTS ways_tags; ''')
con.commit()

cur.execute("CREATE TABLE ways_tags (id INTEGER NOT NULL,key TEXT NOT NULL,value TEXT NOT NULL,type TEXT,FOREIGN KEY (id) REFERENCES ways(id));") # use your column names here
con.commit()

with open('C:/sqlite_windows/ways_tags.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"),i['key'].decode("utf-8"),i['value'].decode("utf-8"),              i['type'].decode("utf-8")) for i in dr]


cur.executemany("INSERT INTO ways_tags (id, key, value, type) VALUES (?,?,?,?);", to_db)
con.commit()
con.close()

