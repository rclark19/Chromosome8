# CREATE CHROMOSOME 8 DATABASE

import pymysql

# Set parameters 
dbname = 'chromosome8'
dbhost = '127.0.0.1'
dbuser = 'root'
dbpass = 'sasha9093' 
port   = 3306
cursortype = pymysql.cursors.DictCursor

# Connect to MySQL Database 
cnx = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, cursorclass=cursortype)
cursor = cnx.cursor()

#Create database and tables 
database = "CREATE DATABASE chromosome8"
cursor.execute(database)

cnx_database ="USE chromosome8"
cursor.execute(cnx_database)

genbank_table = "CREATE TABLE genbank (accession VARCHAR(15) NOT NULL, gene VARCHAR(100), product VARCHAR(300), source VARCHAR(150), PRIMARY KEY(accession), INDEX(source)) ENGINE=InnoDB;"
cursor.execute(genbank_table)

sequence_table = "CREATE TABLE sequence (id MEDIUMINT NOT NULL AUTO_INCREMENT, accession VARCHAR(20) NOT NULL, sequence TEXT (10000) NOT NULL, PRIMARY KEY(id), FOREIGN KEY(accession) REFERENCES genbank(accession)) ENGINE=InnoDB;"
cursor.execute(sequence_table)

coding_table = "CREATE TABLE coding_regions (id MEDIUMINT NOT NULL AUTO_INCREMENT, accession VARCHAR(20) NOT NULL, codon_start INT(3), positions VARCHAR(100), PRIMARY KEY(id), FOREIGN KEY(accession) REFERENCES sequence(accession)) ENGINE=InnoDB;"
cursor.execute(coding_table)

cnx.close()

print('database created')   # sanity check / confirm completion of script
