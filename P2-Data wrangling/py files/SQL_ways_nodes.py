database = 'C:/sqlite_windows/osm.db'

con = sqlite3.connect(database)
cur = con.cursor()


cur.execute('''DROP TABLE IF EXISTS ways_nodes; ''')
con.commit()

cur.execute("CREATE TABLE ways_nodes (id INTEGER NOT NULL,node_id INTEGER NOT NULL,position INTEGER NOT NULL,FOREIGN KEY (id) REFERENCES ways(id),FOREIGN KEY (node_id) REFERENCES nodes(id));") # use your column names here
con.commit()

with open('C:/sqlite_windows/ways_nodes.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"),i['node_id'].decode("utf-8"),i['position'].decode("utf-8")) for i in dr]


cur.executemany("INSERT INTO ways_nodes (id, node_id, position) VALUES (?,?,?);", to_db)
con.commit()
con.close()
