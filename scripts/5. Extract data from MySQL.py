# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:24:23 2018

@author: Rachel
"""

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

# Collate Genbank Data   
with cnx.cursor() as  cursor:
    query1 =  "SELECT accession, gene, product, source FROM genbank;"
    cursor.execute(query1)
    genbank = cursor.fetchall()

# Collate Sequence Data

with cnx.cursor() as cursor:
    query2 = "SELECT accession, sequence FROM sequence;"
    cursor.execute(query2)
    sequence = cursor.fetchall()

# Collate Coding Sequence
with cnx.cursor() as cursor:
    query4 = " SELECT accession,  codon_start, positions FROM coding_regions;"
    cursor.execute(query4)
    coding_regions = cursor.fetchall()

print('export completed')
