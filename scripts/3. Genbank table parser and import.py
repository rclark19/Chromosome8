# File: 2.genbank table parser and import
# Version: v1.0 
# Date: 6/5/2018 
# Copyright: (c) Rachel Julie Clark, Birkbeck, University of London, 2018
# Author: Rachel Julie Clark

# Description of Script: The following script is an parser and import script for file chrom_CDS_8, to extract data using regex (import re) for the table Genbank within the database Chromosome8 and import the data using pymysql (importpymysql) to the database. For more information please see documentation. 

import re
import pymysql

# ----------------------------------------------------------------------------------------------------------------------------------
# PHASE ONE - Parse data from Genbank file for Genbank MySQL table

with open ('test_set.txt', 'r') as f:
        chrom8 = f.read().replace('\n', '')                                        # removing new lines and spaces 
        seq = re.sub(' +', ' ', chrom8)                                                  # remove all trailing whitespaces 
        data = seq.split('//')                                                                     # spilit string at // to create list 

p = re.compile(r'VERSION\s+(\w+\d+.\d+)')                             # regex to extract the accession number - format 'XX000000.0'
accession = []
for i in data:
        for match in p.finditer(i):
                accession.append(match.group(1))   

p = re.compile(r'/gene="([^"]+)')                                               # regex to extract gene name
gene = []
for i in data:
        for match in p.finditer(i):
                gene.append(match.group(1))

# Extract Product data 
p = re.compile(r'product="([^"]+)')                                         # regex to extact product name 
product = []
for i in data:
        for match in p.finditer(i):
                product.append(match.group(1))

p = re.compile(r'/map="([^"]+)')                                                # regex to extact chromosome location
location = []
for i in data:
        for match in p.finditer(i):
                location.append(match.group(1))

genbank = list(zip(accession, gene, product, location))    # zip idata together  

# ---------------------------------------------------------------------------------------------------------------------------------
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

sql = "INSERT INTO genbank (accession, gene, product, location)  VALUES(%s, %s, %s, %s)"

rows = cursor.executemany(sql, genbank)
cnx.commit()

cnx.close()

print('complete genbank table import')         # confirm data has finshed importing
