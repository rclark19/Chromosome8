# GenBank files (trial using sub set of Chromosome8 data) 
# Data parser for Sequence information only

import re
import json
import pymysql

#PHASE ONE - Parse data from Genbank file for Sequence MySQL table

with open ('test_set.txt', 'r') as f:
    chrom8 = f.read().replace('\n', '').replace(' ', '')                   # removing new lines and spaces 
    seq = chrom8.split('//')                                                                     # spilit string at // to create list 

p = re.compile(r'VERSION(\w+\d+.\d+)') 
accession = []
for i in seq:
        for match in p.finditer(i):
                accession.append(match.group(1))
                
p = re.compile(r'ORIGIN(.*\D)$')
sequence = []
sequence_1 = []
for i in seq:
        for match in p.finditer(i):
                seq_1 = re.sub("[^atgcn-]", "", match.group(1))
                sequence.append(seq_1)
        
sequence_data = list(zip(accession, sequence))  # zip information together to create a tuple

# PHASE TWO - import data in to MySQL

# Set parameters 
dbname = 'chromosome8'
dbhost = '127.0.0.1'
dbuser = 'root'
dbpass = 'sasha9093' 
port   = 3306

# Connect to MySQL Database 
cnx = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)
cursor = cnx.cursor(pymysql.cursors.DictCursor)

sql = "INSERT INTO sequence (accession, sequence)  VALUES(%s, %s)"

rows = cursor.executemany(sql, sequence_data)
cnx.commit()

cnx.close()

print('complete sequence table import')         # sanity check 
