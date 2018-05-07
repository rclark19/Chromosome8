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
  
with cnx.cursor() as  cursor:
    query1 =  "SELECT accession, gene, product, location FROM genbank;"                 # Collate genbank table Data   
    cursor.execute(query1)
    genbank = cursor.fetchall()

with cnx.cursor() as cursor:
    query2 = "SELECT accession, sequence FROM sequence;"                              # Collate sequence table data
    cursor.execute(query2)
    sequence = cursor.fetchall()

with cnx.cursor() as cursor:
    query4 = " SELECT accession,  codon_start, positions FROM coding_regions;"       # Collate coding_regions table data
    cursor.execute(query4)
    coding_regions = cursor.fetchall()

print('export completed')                                                            # confirm data export complete 
