
query = 'select user, uid, count(*) from nodes group by uid order by count(*) desc limit 10;'
sqlquery(query)


# In[72]:

query = 'select user, uid, count(*) from nodes group by uid order by count(*) desc limit 10;'
sqlquery(query)


# In[73]:

query = 'select key, count(*) from nodes_tags group by key order by count(*) desc limit 10;'
sqlquery(query)


# In[74]:

query = 'select value, count(*) from nodes_tags where key = \'amenity\' group by value order by count(*) desc limit 10;'
sqlquery(query)


# In[75]:

query = 'select value, count(*) from nodes_tags where key = \'shop\' group by value order by count(*) desc limit 10;'
sqlquery(query)


# In[76]:

query = 'select value, count(*) from nodes_tags where key = \'highway\' group by value order by count(*) desc limit 10;'
sqlquery(query)


# In[77]:

query = 'select id, count(*) from ways_nodes group by id order by count(*) desc limit 10;'
sqlquery(query)


# In[78]:

query = 'select id, count(*) from ways_tags group by id order by count(*) desc limit 10;'
sqlquery(query)


# In[79]:

query = 'select key, count(*) from ways_tags group by key order by count(*) desc limit 10;'
sqlquery(query)


# In[80]:

query = 'select value, count(*) from ways_tags where key = \'amenity\' group by value order by count(*) desc limit 10;'
sqlquery(query)


# In[81]:

query = 'select a.user, b.value, count(*) from nodes a join nodes_tags b on a.id = b.id          where b.key = \'amenity\' group by b.value order by count(*) desc limit 10;'
sqlquery(query)


# In[82]:

query = 'select key, count(*) from nodes_tags group by key order by count(*) desc limit 20;'
sqlquery(query)


# In[83]:

query = 'select a.user, b.value, count(*) from nodes a join nodes_tags b on a.id = b.id          where b.key = \'cuisine\' group by b.value order by count(*) desc limit 10;'
sqlquery(query)


# In[3]:

query = 'SELECT tags.value, COUNT(*) as count FROM (SELECT * FROM nodes_tags UNION ALL SELECT * FROM ways_tags) tags WHERE tags.key= \'postcode\' GROUP BY tags.value ORDER BY count DESC;'
sqlquery(query)


# In[4]:

query = 'SELECT COUNT(*) FROM nodes;'
sqlquery(query)


# In[5]:

query = 'SELECT COUNT(*) FROM ways;'
sqlquery(query)


# In[6]:

query = 'SELECT COUNT(DISTINCT(e.uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e'
sqlquery(query)


# In[19]:

query = 'SELECT e.user, COUNT(*) as num FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e GROUP BY e.user ORDER BY num DESC LIMIT 10;' 
sqlquery(query)


# In[8]:

query = 'SELECT COUNT(*) FROM (SELECT e.user, COUNT(*) as num FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e GROUP BY e.user HAVING num=1)  u;'
sqlquery(query)


# In[12]:

query = 'SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value=\'place_of_worship\') i ON nodes_tags.id=i.id WHERE nodes_tags.key=\'religion\' GROUP BY nodes_tags.value ORDER BY num DESC;'
sqlquery(query)
