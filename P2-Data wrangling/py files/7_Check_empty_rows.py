
#  I faced challenges loading file into database. Initially when I tried opening the csv files in excel it showed empty alternate rows. so I wrote the below function to confirm if there are empty rows.

# In[12]:

import csv
filename = 'C:/Users/Saisandeep/Documents/Udacity Data Analyst/Data wrangling/ways.csv'

def emptyrowcounts(filename):
    count = 0
    rows = 0
    with open(filename, 'r') as f:
        for row in f:
            if row:
                rows = rows + 1
            else:
                count = count+1
    return rows, count

emptyrowcounts(filename)


# I ran the above code on all the files and found there are no empty rows in the files and continued my struggle with the loading into database. After quite a bit of struggle and search online I realized its the issue with the datatype and decoding. Then I reached out the forums to check if someone else had similar issues and found a lot of help and guidence from previous discussions. I was able to figure out my mistakes and used python connection to sqlite database and performed below queries.

