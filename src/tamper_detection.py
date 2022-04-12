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
from RowEncryptionRecord import RowEncryptionRecord
from ColumnEncryptionRecord import ColumnEncryptionRecord
from MysqlAdapter import MysqlAdapter


def get_column_hash(results):
	# assumes the primary key is the first column in the table!

	hash_string = []

	for result in results:
		str_pk = str(result[0])  # convert the PKs to string for hashing
		hash_string += str_pk

	final_hash = utils.SHA_256_conversion(hash_string)
	return final_hash


def get_encrypted_table(table_name, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	data = str(table_name)  # ensure table name is a string
	return cipher.encrypt(pad(data.encode(), 16))


def get_table_name_hash(table_name):
	str_table_name = str(table_name)  # ensure table name is string
	return utils.SHA_256_conversion(str_table_name)

# column encryption record comparison
def cerc(table_list, adapter, key, iv):
	""" Get all DB tables involved in the original query statement and
	query all the data in each table. Calculate the column encryption
	record according to the TDRB middleware study. """
	
	tamper_flag = 0
	
	tables = []
	# TODO: ADD SOME MECHANISM TO ACTUALLY ITERATE OVER TABLES INSTEAD OF ROWS
	for table_name in table_list:
		
		query = "select * from " + table_name  # construct the query for getting the data from the table

		results = adapter.send_query(query)

		column_hash = get_column_hash(results)

		table_name_aes = get_encrypted_table(table_name, key, iv)

		column_hash = get_column_hash(results)
		table_name_aes = get_encrypted_table(table_name, key, iv)
		table_name_hash = get_table_name_hash(table_name)

		print(column_hash)
		print(table_name_aes)
		print(table_name_hash)

		# query_column_hash, redis_flag = access_redis(table_name_hash)

	"""
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
