# File: 5.extact data from MySQL
# Version: v1.0 
# Date: 6/5/2018 
# Copyright: (c) Rachel Julie Clark, Birkbeck, University of London, 2018
# Author: Rachel Julie Clark

# Description of Script: The following script exports data from the three tables within the Chromosome8 database into python list format

import pymysql

# Set parameters 
dbname = 'chromosome8'
dbhost = 
dbuser = 
dbpass = 
port   = 

# Connect to MySQL Database 
cnx = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)
cursor = cnx.cursor(pymysql.cursors.DictCursor)

# Collate genbank table Data   
with cnx.cursor() as  cursor:
    query1 =  "SELECT accession, gene, product, source FROM genbank;"
    cursor.execute(query1)
    genbank = cursor.fetchall()

# Collate sequence table data

with cnx.cursor() as cursor:
    query2 = "SELECT accession, sequence FROM sequence;"
    cursor.execute(query2)
    sequence = cursor.fetchall()

# Collate coding_regions table data
with cnx.cursor() as cursor:
    query4 = " SELECT accession,  codon_start, positions FROM coding_regions;"
    cursor.execute(query4)
    coding_regions = cursor.fetchall()

print('export completed')                          # confirm data export complete 
