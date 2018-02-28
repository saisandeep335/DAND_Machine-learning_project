# Below are the coordinates of the Sunnyvale city open street map data I will be working on. I have downloaded the data from the Overpass API link provided in the project details. 
# Minimum Latitude : 37.3499 Maximum Latitude: 37.3863 Minimum Longitude: -122.0654 Maximum Longitude: -121.9782
# 
# Below is the code to understand different tags in the data and counts against each of them.

import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    # YOUR CODE HERE
    tags = {}
    osm_file = open(filename, 'r')
    for event, elem in ET.iterparse(osm_file):
        #print elem.tag
        if elem.tag in tags:
            tags[elem.tag] = tags[elem.tag]+1
        else:
            tags[elem.tag] = 1
    return tags

data = 'C:/Users/Saisandeep/Documents/Udacity Data Analyst/Data wrangling/interpreter'
tags = count_tags(data)
pprint.pprint(tags)


# From the above code I can see that there are Nodes and Ways. I will be working on getting these into a database and analyzing further.
