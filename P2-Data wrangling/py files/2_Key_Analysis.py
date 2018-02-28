# I have used the code I worked on in the exercise. Looks like there are lower colons in 32580 tags. 
# I want to continue the way we have split the keys into type and the key.


import xml.etree.cElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        
        if lower.match(element.attrib['k']):
            keys['lower'] = keys['lower']+1
        elif lower_colon.match(element.attrib['k']):
            keys['lower_colon'] = keys['lower_colon'] + 1
        elif problemchars.search(element.attrib['k']):
            keys['problemchars'] =keys['problemchars'] + 1
        else:
            keys['other'] = keys['other'] +1
        #print element.attrib['k']
        #print keys
    return keys

def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)
    return keys

keys = process_map(data)
pprint.pprint(keys)
