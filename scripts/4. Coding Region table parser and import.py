# File: 4. coding regions table parser and import
# Version: v1.0 
# Date: 6/5/2018 
# Copyright: (c) Rachel Julie Clark, Birkbeck, University of London, 2018
# Author: Rachel Julie Clark

# Description of Script: The following script is an parser and import script for file chrom_CDS_8, to extract data using regex (import re) for the table Coding_regions within the database Chromosome8 and import the data using pymysql (importpymysql) to the database. For more information please see documentation. 

import re
import pymysql

# --------------------------------------------------------------------------------------------------------------------------------
#PHASE ONE - Parse data from Genbank file for Coding Sequence MySQL table

with open ('test_set.txt', 'r') as f:
    chrom8 = f.read().replace('\n', '').replace('(', '').replace('<', '')  # removing new lines, ( and <
    seq = chrom8.split('//')                                               # split string at // to create list 

p = re.compile(r'VERSION\s+(\w+\d+.\d+)')                                  # regex to extract the accession number - format 'XX000000.0'
accession = []
for i in seq:
        for match in p.finditer(i):
                accession.append(match.group(1))

p = re.compile(r'codon_start=(\d+)')                                       # regex to extact codon_start number 
codon_start = []
for i in seq:
        for match in p.finditer(i):
                codon_start.append(match.group(1))
            
p = re.compile(r'CDS\s+([^ ,]+)')                                          # regex to extact coding regions
positions = []
for i in seq:
        for match in p.finditer(i):
                pos_1 = re.sub(r'join', '', match.group(1))                # regex to remove splice varants 
                positions.append(pos_1)    

coding_sequence = list(zip(accession, codon_start, positions))        # zip data togther 

# ---------------------------------------------------------------------------------------------------------------------------
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

sql = "INSERT INTO coding_regions (accession, codon_start, positions) VALUES(%s, %s, %s)"

rows = cursor.executemany(sql, coding_sequence)
cnx.commit()

cnx.close()

print('complete coding regions import')         # confirm data has finished importing
