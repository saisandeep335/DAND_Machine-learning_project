import xml.etree.cElementTree as ET
import pprint
import re

def get_user(element):
    return


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if element.tag in ['node', 'way', 'relation']:
            #print element.tag
            users.add(element.attrib['user'])
    return users

users = process_map(data)
pprint.pprint(users)


# From the above code I have got the list of all the users who have contributed in creating this data from nodes, ways and relations.
