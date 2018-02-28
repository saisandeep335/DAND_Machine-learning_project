# Phone numbers analysis
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
data = 'C:/Users/Saisandeep/Documents/Udacity Data Analyst/Data wrangling/interpreter'
OSMFILE = data

#below function would audit all types of phone numbers. I worked on the regex to build it incrementally adding all the different formats of phone numbers
def auditphone(osmfile):
    osm_file = open(osmfile, "r")
    phone_type = re.compile(r'^1\.[0-9]{3}\.[0-9]{3}\.[0-9]{4}$|^\+1\-[0-9]{3}\-[0-9]{3}\-[0-9]{4}$|^[0-9]{3}\.[0-9]{3}\.[0-9]{4}$|^[0-9]{3}\.[0-9]{3}\.[A-Z]{4}$|^[0-9]{10}$|^\+1\s[0-9]{3}\s[0-9]{3}\s[0-9]{4}$|^1\s[0-9]{3}\s[0-9]{3}\s[0-9]{4}$|^[0-9]{3}\s[0-9]{3}\s[0-9]{4}$|^[0-9]{3}\-[0-9]{3}\-[0-9]{4}$|^\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4}$|^\+1\.[0-9]{3}\.[0-9]{3}\.[0-9]{4}$', re.IGNORECASE)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k']=='phone':
                    m = phone_type.search(tag.attrib['v'])
                    if not m:
                        print tag.attrib['v']
    osm_file.close()
     
auditphone(OSMFILE)

#Below function is used to conver the alphabets in the phone numbers to the numbers based on the T9 formating. I refered to a stackoverflow code for this.
def alpha_num(input):
  
    key_alph='abcdefghijklmnopqrstuvwxyz'
    
    key_num= '22233344455566677778889999'
    
    counter = len(input)
    #print counter
    total=''    #Stores the part of string which is not going to be changed
    #print total
    while (counter>0):
        alpha = input.lower()[-counter]
        #print counter
        #print alpha
        if alpha.isalpha():   #checks if each character in the input is a valid alphabet and not a number.
            total+=key_num[key_alph.index(alpha)]  #Appending the new characters  
        else:
            total+=alpha     #This will preserve if any numeric character is encountered and keeps it same as in the input
        counter -= 1
    return total

# below function corrects all different formats of numbers into standart format +1XXXXXXXXXX
def format_phone(test):

    if re.match('^[0-9]{10}$', test):
        number = '+1'+test
    elif re.match('^1[0-9]{10}$',test):
        number = '+'+test
    elif re.match('^\+1[0-9]{10}$',test):
        number = test
    elif re.match('^\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4}$',test):
        number = '+1'+test[1:4]+test[6:9]+test[10:]
    elif re.match('^\([0-9]{3}\)\-[0-9]{3}\-[0-9]{4}$',test):
        number = '+1'+test[1:4]+test[6:9]+test[10:]
    elif re.match('^\+1\s\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4}$',test):
        number = '+1'+test[4:7]+test[9:12]+test[13:]
    elif re.match('^[0-9]{3}\s[0-9]{3}\s[0-9]{4}$',test):
        number = '+1'+test.replace(' ','')
    elif re.match('^\+1\s[0-9]{3}\s[0-9]{3}\s[0-9]{4}$',test):
        number = test.replace(' ','')
    elif re.match('^\+1\s[0-9]{3}\s[0-9]{3}\-[0-9]{4}$',test):
        number = test.replace(' ','').replace('-','')
    elif re.match('^\+1\-[0-9]{3}\-[0-9]{3}\-[0-9]{4}$',test):
        number = test.replace('-','')
    elif re.match('^\+1\s[0-9]{3}\s[0-9]{7}$',test):
        number = test.replace(' ','')
    elif re.match('^\+1\s[0-9]{3}\-[0-9]{3}\-[0-9]{4}$',test):
        number = test.replace(' ','').replace('-','')
    elif re.match('^\+1\.[0-9]{3}\.[0-9]{3}\.[0-9]{4}$',test):
        number = test.replace('.','')
    elif re.match('^1\.[0-9]{3}\.[0-9]{3}\.[0-9]{4}$',test):
        number = '+'+test.replace('.','')
    elif re.match('^1\s[0-9]{3}\s[0-9]{3}\s[0-9]{4}$',test):
        number = '+'+test.replace(' ','')
    elif re.match('^[0-9]{3}\.[0-9]{3}\.[0-9]{4}$',test):
        number = '+1'+test.replace('.','')
    elif re.match('^[0-9]{3}\-[0-9]{3}\-[0-9]{4}$',test):
        number = '+1'+test.replace('-','')
    elif re.match('^1\-[0-9]{3}\-[0-9]{3}\-[0-9]{4}$',test):
        number = test.replace('-','')
    elif re.match('^\+1\-[0-9]{3}\-[0-9]{3}\-[a-z]{4}$',test,flags=re.IGNORECASE):
        number = '+1'+test[2:5]+test[6:9]+alpha_num(test[10:])
    elif re.match('^\([0-9]{3}\)\s[0-9]{3}\-[a-z]{4}$',test,flags=re.IGNORECASE):
        number = '+1'+test[1:4]+test[6:9]+alpha_num(test[10:])
    else:
        number = 'N/A'
    test = number
    return number

#test = '1-650-938-NYNY'
#print test
#print format_phone(test)

