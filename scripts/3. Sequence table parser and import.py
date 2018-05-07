# File: 3.sequence table parser and import
# Version: v1.0 
# Date: 6/5/2018 
# Copyright: (c) Rachel Julie Clark, Birkbeck, University of London, 2018
# Author: Rachel Julie Clark

# Description of Script: The following script is an parser and import script for file chrom_CDS_8, to extract data using regex (import re) for the table Sequence within the database Chromosome8 and import the data using pymysql (importpymysql) to the database. For more information please see documentation. 

import re
import pymysql

# ---------------------------------------------------------------------------------------------------------------------------------
#PHASE ONE - Parse data from Genbank file for Sequence MySQL table

with open ('test_set.txt', 'r') as f:
    chrom8 = f.read().replace('\n', '').replace(' ', '')              # removing new lines and all spaces 
    seq = chrom8.split('//')                                          # split string at // to create list 

p = re.compile(r'VERSION(\w+\d+.\d+)')                                # regex to extract the accession number - format 'XX000000.0'
accession = []
for i in seq:
        for match in p.finditer(i):
                accession.append(match.group(1))
                
p = re.compile(r'ORIGIN(.*\D)$')                                      # regex to extract sequence data 
sequence = []
for i in seq:
        for match in p.finditer(i):
                seq_1 = re.sub("[^atgcn-]", "", match.group(1))       # regex to remove digits from sequence data 
                sequence.append(seq_1)
        
sequence_data = list(zip(accession, sequence))                        # zip data together 

# -------------------------------------------------------------------------------------------------------------------------------
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

sql = "INSERT INTO sequence (accession, sequence)  VALUES(%s, %s)"

rows = cursor.executemany(sql, sequence_data)
cnx.commit()

cnx.close()

print('complete sequence table import')                               # confirm data has been imported
