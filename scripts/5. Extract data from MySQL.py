# File: 5.extact data from MySQL
# Version: v1.0 
# Date: 6/5/2018 
# Copyright: (c) Rachel Julie Clark, Birkbeck, University of London, 2018
# Author: Rachel Julie Clark

# Description of Script: The following script exports data from the three tables within the Chromosome8 database into python list format

import pymysql

# Set parameters 
dbname = 'chromosome8'
dbhost = '127.0.0.1'
dbuser = 'root'
dbpass = 'sasha9093'
port   = 3306

# Connect to MySQL Database 
cnx = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)
cursor = cnx.cursor(pymysql.cursors.DictCursor)

with cnx.cursor() as  cursor:
    query1 =  "SELECT accession, gene, product, location FROM genbank;"                                           # collate genbank data   
    cursor.execute(query1)
    genbank = cursor.fetchall()

with cnx.cursor() as cursor:
    query2 = "SELECT accession, sequence FROM sequence;"                                                                    # collate sequence data
    cursor.execute(query2)
    sequence = cursor.fetchall()

# Collate Coding Sequence
with cnx.cursor() as cursor:
    query3 = " SELECT accession,  codon_start, positions FROM coding_regions;"                            # collate coding region data 
    cursor.execute(query3)
    coding_regions = cursor.fetchall()

print('export completed')                                                                                                                                       # confirm data export is complete 
