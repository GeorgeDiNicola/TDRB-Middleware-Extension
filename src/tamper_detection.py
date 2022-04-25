"""
Tamper Detection Module
These algorithms are have been modified with the guidance of the following study:
https://ieeexplore-ieee-org.ezproxy.cul.columbia.edu/document/9417201

J. Lian, S. Wang and Y. Xie, "TDRB: An Efficient Tamper-Proof Detection Middleware for Relational Database Based on Blockchain Technology," 
in IEEE Access, vol. 9, pp. 66707-66722, 2021, doi: 10.1109/ACCESS.2021.3076235.
"""

# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

import utils
import hashlib
from RowEncryptionRecord import RowEncryptionRecord
from ColumnEncryptionRecord import ColumnEncryptionRecord
from MysqlAdapter import MysqlAdapter
from subprocess import check_output
import config


# settings holds the AES encrypt and decrypt key
settings = config.load_config()


def rerc_new(row_encryption_recs, table_name, key, iv):

	tamper_flag = 0  # zero indicates no tampering
	tampered_records_primary_key_list = []


	# query by range instead of records

	# TODO: call the actual blockchain functions!!!
	try:
		blockchain_result = check_output(['node', 'queryRange.js'])
	except:
		blockchain_result = ""  # no result for the query found above

	for rec in row_encryption_recs:
		item_id = rec.item_id_hash
		hashed_items = rec.item_hash
		if hashed_items not in str(blockchain_result):
			#print("tampering detected: ILLEGAL MODIFICATION")
			tampered_records_primary_key_list.append(item_id)
			tamper_flag = 1

	return tamper_flag, tampered_records_primary_key_list


# column encryption record comparison
def cerc(col_encryption_rec, table_name, key, iv):
	""" Get all DB tables involved in the original query statement and
	query all the data in each table. Calculate the column encryption
	record according to the TDRB middleware study. """
	
	tamper_flag = 0  # zero indicates no tampering
	tamper_info = ""


	try:
		blockchain_result = check_output(['node', 'query.js', 'RECORD0'])  # CERC always record 0
	except:
		blockchain_result = ""  # no result for the query found above

	if col_encryption_rec.column_hash not in str(blockchain_result):
			#tamper_info = "tampering detected: ILLEGAL INSERT OR DELETE"
			tamper_flag = 1

	return tamper_flag, tamper_info


# row encryption record comparison
def rerc(table, table_name, key, iv):
	""" """

	tamper_flag = 0  # zero indicates no tampering
	tampered_records_primary_key_list = []

	for index, row in table.iterrows():
		#rer = RowEncryptionRecord()
		item_id = str(row["student_id"])
		item_id_hash = item_id  #utils.get_item_id_hash(item_id)
		#rer.item_hash = utils.get_item_hash_pk_present(row)
		concatentated_items = "".join(map(str,row[1:]))  # concatenate the primary keys (for hash)
		item_hash = utils.SHA_256_conversion(concatentated_items)  # hash the items in the row
		item_id_AES = item_id
		owned_table_AES = utils.get_encrypted_table(table_name, settings["aes_key"], settings["iv"])

		try:
			blockchain_result = check_output(['node', 'query.js', 'RECORD' + item_id_hash])
		except:
			#print("CAUGHT EXCEPTION")
			blockchain_result = ""  # no result for the query found above
		
		if item_hash not in str(blockchain_result):
			#print("tampering detected: ILLEGAL MODIFICATION")
			tampered_records_primary_key_list.append(item_id)
			tamper_flag = 1

	return tamper_flag, tampered_records_primary_key_list



