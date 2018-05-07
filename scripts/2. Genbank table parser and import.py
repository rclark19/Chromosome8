# GenBank files (trial using sub set of Chromosome8 data) 
# Data parser for Sequence information only

import re
import csv
import pymysql

# PHASE ONE - Parse data from Genbank file for Genbank MySQL table 

with open ('test_set.txt', 'r') as f:
        chrom8 = f.read().replace('\n', '')     # removing new lines and spaces 
        seq = re.sub(' +', ' ', chrom8)
        data = seq.split('//')                                                                     # spilit string at // to create list 

p = re.compile(r'VERSION\s+(\w{2}\d{6}.\d)')
accession = []
for i in data:
        for match in p.finditer(i):
                accession.append(match.group(1))   

p = re.compile(r'/gene="([^"]+)')
gene = []
for i in data:
        for match in p.finditer(i):
                gene.append(match.group(1))

# Extract Product data 
p = re.compile(r'product="([^"]+)')
product = []
for i in data:
        for match in p.finditer(i):
                product.append(match.group(1))

p = re.compile(r'SOURCE([^ORGANISM]+)')
source = []
for i in data:
        for match in p.finditer(i):
                source.append(match.group(1))

genbank = list(zip(accession, gene, product, source))  # zip information together to create a tuple 

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

sql = "INSERT INTO genbank (accession, gene, product, source)  VALUES(%s, %s, %s, %s)"

rows = cursor.executemany(sql, genbank)
cnx.commit()

cnx.close()

print('complete genbank table import')         # sanity check 
