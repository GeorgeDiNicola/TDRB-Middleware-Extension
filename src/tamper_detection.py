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

	print("\n====Column Encryption Record====\n")
	print(col_encryption_rec.table_name_hash)
	print(col_encryption_rec.table_name_AES)
	print(col_encryption_rec.column_hash)
	print("==============================\n")

	try:
		blockchain_result = check_output(['node', 'query.js', col_encryption_rec.table_name_hash])
	except:
		blockchain_result = ""  # no result for the query found above

	print("CER column hash: ", col_encryption_rec.column_hash)
	print(str(blockchain_result))
	if col_encryption_rec.column_hash not in str(blockchain_result):
			print("tampering detected: ILLEGAL INSERT OR DELETE")
			tamper_info = "tampering detected: ILLEGAL INSERT OR DELETE"
			tamper_flag = 1

	#table_name_hash = utils.get_table_name_hash(table_name)
	#column_hash = utils.get_column_hash(results)
	#table_name_aes = utils.get_encrypted_table(table_name, key, iv)

	return tamper_flag, tamper_info

	
	
	
	# TODO: ADD SOME MECHANISM TO ACTUALLY ITERATE OVER TABLES INSTEAD OF ROWS
	"""
	tables = []
	for table_name in table_list:
		
		query = "select * from " + table_name  # construct the query for getting the data from the table

		results = adapter.send_query(query)

		column_hash = utils.get_column_hash(results)

		table_name_aes = utils.get_encrypted_table(table_name, key, iv)

		column_hash = utils.get_column_hash(results)
		table_name_aes = utils.get_encrypted_table(table_name, key, iv)
		table_name_hash = utils.get_table_name_hash(table_name)

		#print(column_hash)
		#print(table_name_aes)
		#print(table_name_hash)

		# query_column_hash, redis_flag = access_redis(table_name_hash)

	# redis_flag represents cache hit (1) or cache miss (0)

		if column_hash != query_column_hash:
			if redis_flag == 0:
				tamper_flag = 1
				#b_tabes = rich_query_blockchain_(table)   send query to get blockchain records
				r_tables = get_all_row_encryption_records(table)
				illegal_insert, illegal_delete, illegal_modify = check_tamper(b_tables, r_tables)
			else:
				clear Redis
				get query_column_hash from Blockchain
				if column_hash != query_column_hash:
					tamper_flag = 1
					#b_tables = rich_query_blockchain_(table)  # send query to get blockchain records
					r_tables = get_all_row_encryption_records(table)
					illegal_insert, illegal_delete, illegal_modify = check_tamper(b_tables, r_tables)
				else:
					tamper_flag = check_tamper(b_tables, r_tables)
	if tamper_flag == 0:
		return table  # return the query results from the relational DB
	else:
		tamper_information = show_tamper_information(illegal_insert, illegal_delete, illegal_modify)
		print(tamper_information)

	return tamper_information, table  # table = query results
	"""

# row encryption record comparison
def rerc(table_name, adapter, key, iv):
	""" """

	tamper_flag = 0  # zero indicates no tampering
	tampered_records_primary_key_list = []

	#TODO: note - I already have these
	query = "select * from " + table_name  # construct the query for getting the data from the table
	results = adapter.send_query(query)
	
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
			print("tampering detected: ILLEGAL MODIFICATION")
			tampered_records_primary_key_list.append(item_id)
			tamper_flag = 1

	return tamper_flag, tampered_records_primary_key_list



