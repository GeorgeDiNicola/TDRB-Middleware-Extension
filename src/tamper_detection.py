"""
Tamper Detection Module
These algorithms are implemented with the guidance of the following study:
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


# column encryption record comparison
def cerc(col_encryption_rec, table_name, adapter, key, iv):
	""" Get all DB tables involved in the original query statement and
	query all the data in each table. Calculate the column encryption
	record according to the TDRB middleware study. """
	
	tamper_flag = 0  # zero indicates no tampering
	tamper_info = ""

	try:
		blockchain_result = check_output(['node', 'query.js', col_encryption_rec.table_name_hash])
	except:
		blockchain_result = ""  # no result for the query found above

	if col_encryption_rec.column_hash not in str(blockchain_result):
			#tamper_info = "tampering detected: ILLEGAL INSERT OR DELETE"
			tamper_flag = 1

	return tamper_flag, tamper_info


# row encryption record comparison
def rerc(results, table_name, adapter, key, iv):
	""" """

	tamper_flag = 0  # zero indicates no tampering
	tampered_records_primary_key_list = []

	#TODO: note - I already have these
	#query = "select * from " + table_name  # construct the query for getting the data from the table
	#results = adapter.send_query(query)
	
	for row in results:
		item_id = row[0]
		item_id_hash = utils.get_item_id_hash(item_id)
		item_hash = utils.get_item_hash_pk_present(row)
		item_id_aes = utils.get_encrypted_item_id(item_id, key, iv)
		owned_table_aes = utils.get_encrypted_table(table_name, key, iv)

		try:
			blockchain_result = check_output(['node', 'query.js', item_id_hash])
		except:
			#print("CAUGHT EXCEPTION")
			blockchain_result = ""  # no result for the query found above
		
		if item_hash not in str(blockchain_result):
			#print("tampering detected: ILLEGAL MODIFICATION")
			tampered_records_primary_key_list.append(item_id)
			tamper_flag = 1

	return tamper_flag, tampered_records_primary_key_list



