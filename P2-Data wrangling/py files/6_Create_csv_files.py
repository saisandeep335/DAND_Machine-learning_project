
import csv
import codecs
import pprint
import re
import xml.etree.cElementTree as ET
from 4_Street_name_cleaning import update_name
from 4_Street_name_cleaning import is_street_name
from 5_phone_num_cleaning import format_phone
import cerberus
import schema


data = 'C:/Users/Saisandeep/Documents/Udacity Data Analyst/Data wrangling/interpreter'
OSM_PATH = data

NODES_PATH = "C:/Users/Saisandeep/Documents/Udacity Data Analyst/Data wrangling/nodes.csv"
NODE_TAGS_PATH = "C:/Users/Saisandeep/Documents/Udacity Data Analyst/Data wrangling/nodes_tags.csv"
WAYS_PATH = "C:/Users/Saisandeep/Documents/Udacity Data Analyst/Data wrangling/ways.csv"
WAY_NODES_PATH = "C:/Users/Saisandeep/Documents/Udacity Data Analyst/Data wrangling/ways_nodes.csv"
WAY_TAGS_PATH = "C:/Users/Saisandeep/Documents/Udacity Data Analyst/Data wrangling/ways_tags.csv"

LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

SCHEMA = schema.schema

NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']


def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS,
                  problem_chars=PROBLEMCHARS, default_tag_type='regular'):
    """Clean and shape node or way XML element to Python dict"""

    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []  # Handle secondary tags the same way for both node and way elements

    #print element.tag
    #print element.attrib
    if element.tag == 'node':
        for field in node_attr_fields:
            #print field, element.attrib[field]
            node_attribs[field] = element.attrib[field]
    if element.tag == 'way':
        for field in way_attr_fields:
            #print field, element.attrib[field]
            way_attribs[field] = element.attrib[field]
        count = 0
        for node in element.findall('nd'):
            entry = {}
            entry['id'] = element.attrib['id']
            entry['node_id'] = node.attrib['ref']
            entry['position'] = count
            count = count +1
            way_nodes.append(entry)
        #print '-------------------------'
        #print way_nodes
                
    for tag in element.findall('tag'):
        entry = {}
        
        if is_street_name(tag):
            entry['value'] = update_name(tag.attrib['v'], mapping)
        elif tag.attrib['k'] == 'phone':
            entry['value'] = format_phone(tag.attrib['v'])
        else:
            entry['value'] = tag.attrib['v']
        
        if ':' in tag.attrib['k']:
            keys = tag.attrib['k'].split(':',1)
            entry['type'] = keys[0]
            entry['key'] = keys[1]
        else:
            entry['type'] = 'regular'
            entry['key'] = tag.attrib['k']
        entry['id'] = element.attrib['id']
        tags.append(entry)
        
        
    #print'-----------------------'
    #print tags
    
    if element.tag == 'node':
        return {'node': node_attribs, 'node_tags': tags}
    elif element.tag == 'way':
        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}


# ================================================== #
#               Helper Functions                     #
# ================================================== #
def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


def validate_element(element, validator, schema=SCHEMA):
    """Raise ValidationError if element does not match schema"""
    if validator.validate(element, schema) is not True:
        field, errors = next(validator.errors.iteritems())
        message_string = "\nElement of type '{0}' has the following errors:\n{1}"
        error_string = pprint.pformat(errors)
        
        raise Exception(message_string.format(field, error_string))


class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
            k: (v.encode('utf-8') if isinstance(v, unicode) else v) for k, v in row.iteritems()
        })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


# ================================================== #
#               Main Function                        #
# ================================================== #
def process_map(file_in, validate):
    """Iteratively process each XML element and write to csv(s)"""

    with codecs.open(NODES_PATH, 'w') as nodes_file, \
         codecs.open(NODE_TAGS_PATH, 'w') as nodes_tags_file, \
         codecs.open(WAYS_PATH, 'w') as ways_file, \
         codecs.open(WAY_NODES_PATH, 'w') as way_nodes_file, \
         codecs.open(WAY_TAGS_PATH, 'w') as way_tags_file:

        nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        validator = cerberus.Validator()

        for element in get_element(file_in, tags=('node', 'way')):
            el = shape_element(element)
            if el:
                if validate is True:
                    validate_element(el, validator)

                if element.tag == 'node':
                    nodes_writer.writerow(el['node'])
                    node_tags_writer.writerows(el['node_tags'])
                elif element.tag == 'way':
                    ways_writer.writerow(el['way'])
                    way_nodes_writer.writerows(el['way_nodes'])
                    way_tags_writer.writerows(el['way_tags'])


process_map(OSM_PATH, validate = True)
