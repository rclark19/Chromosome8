# File: 1.Chromosome8 database
# Version: v1.0 
# Date: 6/5/2018 
# Copyright: (c) Rachel Julie Clark, Birkbeck, University of London, 2018
# Author: Rachel Julie Clark

#Description of Script: The following script creates the database 'Chromosome8' for the management of required data parsed parsed from Genbank file 'chrom_CDS_8'. For detailed information on selection of tables please see documentation.

import pymysql

# Set parameters 
dbname = 'chromosome8'
dbhost = 
dbuser = 
dbpass =  
port   = 
cursortype = pymysql.cursors.DictCursor

# Connect to MySQL Database 
cnx = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, cursorclass=cursortype)
cursor = cnx.cursor()

#Create database and tables 
database = "CREATE DATABASE chromosome8"
cursor.execute(database)

cnx_database ="USE chromosome8"
cursor.execute(cnx_database)

genbank_table = "CREATE TABLE genbank (accession VARCHAR(15) NOT NULL, gene VARCHAR(100), product VARCHAR(300), location VARCHAR(50), PRIMARY KEY(accession)) ENGINE=InnoDB;"
cursor.execute(genbank_table)

sequence_table = "CREATE TABLE sequence (id MEDIUMINT NOT NULL AUTO_INCREMENT, accession VARCHAR(20) NOT NULL, sequence TEXT (100000) NOT NULL, PRIMARY KEY(id), FOREIGN KEY(accession) REFERENCES genbank(accession)) ENGINE=InnoDB;"
cursor.execute(sequence_table)

coding_table = "CREATE TABLE coding_regions (id MEDIUMINT NOT NULL AUTO_INCREMENT, accession VARCHAR(20) NOT NULL, codon_start INT(3), positions VARCHAR(100), PRIMARY KEY(id), FOREIGN KEY(accession) REFERENCES sequence(accession)) ENGINE=InnoDB;"
cursor.execute(coding_table)

cnx.close()

print('database created')   # confirm database creation 
