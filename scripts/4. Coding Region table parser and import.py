# GenBank files (trial using sub set of Chromosome8 data) 
# Data parser for Sequence information only

import re
import pymysql

#PHASE ONE - Parse data from Genbank file for Coding Sequence MySQL table

with open ('test_set.txt', 'r') as f:
    chrom8 = f.read().replace('\n', '')                   # removing new lines and spaces 
    seq = chrom8.split('//')                                                                     # spilit string at // to create list 

# Extract Accession data
p = re.compile(r'VERSION\s+(\w+\d+.\d+)')
accession = []
for i in seq:
        for match in p.finditer(i):
                accession.append(match.group(1))

# Extract Codon Start data 
p = re.compile(r'codon_start=(\d+)')
codon_start = []
for i in seq:
        for match in p.finditer(i):
                codon_start.append(match.group(1))

# Extract Postion data 
p = re.compile(r'CDS\s+([^ ]+)')
positions = []
for i in seq:
        for match in p.finditer(i):
                positions.append(match.group(1))

coding_sequence = list(zip(accession, codon_start, positions))

# PHASE TWO - import data in to MySQL

# Set parameters 
dbname = 'chromosome8'
dbhost = 
dbuser = 
dbpass = 
port   = 

# Connect to MySQL Database 
cnx = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)
cursor = cnx.cursor(pymysql.cursors.DictCursor)

sql = "INSERT INTO coding_regions (accession, codon_start, positions) VALUES(%s, %s, %s)"

rows = cursor.executemany(sql, coding_sequence)
cnx.commit()

cnx.close()

print('complete coding regions import')         # sanity check 
