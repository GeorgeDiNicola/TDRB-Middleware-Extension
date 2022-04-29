"""
	Author: George DiNicola
	Description: The utils module is a collection of useful functions that are
		used throughout the application.
"""

import hashlib
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

def get_column_hash(results):
	""" Get the hash value for all of the primary keys in a database table.
		NOTE:  assumes the primary key is the first column in the table!
	"""

	hash_string = []

	for result in results:
		str_pk = str(result[0])  # convert the PKs to string for hashing
		hash_string += str_pk

	final_hash = SHA_256_conversion(hash_string)
	return final_hash

def get_column_hash_pks_only(primary_keys):
	""" Get the hash value for all of the primary keys in a list."""

	hash_string = []

	for pk in primary_keys:
		str_pk = str(pk)  # convert the PKs to string for hashing
		hash_string += str_pk

	final_hash = SHA_256_conversion(hash_string)
	return final_hash


def SHA_256_conversion(data):
	""" Convert a variable of any data type to its corresponding SHA 256 hash value."""
	
	pk = data
	m = hashlib.sha256()
	pk_bytes = str(pk).encode()  # ensure PK is string before conversion
	m.update(pk_bytes)

	return m.hexdigest()


def get_encrypted_table(table_name, key, iv):
	""" Encrypt the name of a relational database table using AES encryption."""
	
	cipher = AES.new(key, AES.MODE_CBC, iv)
	table_name_str = str(table_name)  # ensure table name is a string before conversion
	return cipher.encrypt(pad(table_name_str.encode(), 16))


def get_table_name_hash(table_name):
	"""Calculate the SHA 256 hash value for a given relational table name."""
	
	str_table_name = str(table_name)  # ensure table name is string before conversion
	return SHA_256_conversion(str_table_name)


def get_item_id_hash(item_id):
	""" Calculate the SHA 256 hash value for a given item ID. """
	str_item_id = str(item_id)  # ensure item ID is string before conversion
	return SHA_256_conversion(str_item_id)


def get_item_hash_pk_present(row):
	""" Calculate the SHA 256 hash value for the contenated attribute value of the given row (EXCEPT the
	primary key). """
	concatenated_items = ""
	for column in row[1:]:  # skip the primary key (1st column)
		concatenated_items += str(column)  # ensure the column is string before conversion
	return SHA_256_conversion(concatenated_items)


def get_encrypted_item_id(item_id, key, iv):
	""" Encrypt an item ID value using AES encryption."""
	cipher = AES.new(key, AES.MODE_CBC, iv)
	item_id_str = str(item_id)  # ensure table name is a string before conversion
	return cipher.encrypt(pad(item_id_str.encode(), 16))


def encode_items(item_list):
	""" Convert a list of items to the UTF-8 encoding of their
		concatenated result."""

	m = hashlib.sha256()

	concat_items = ""
	for item in item_list:
		concat_items += str(item)

	m.update(concat_items.encode())

	return m.hexdigest()


def get_all_database_tables(adapter, database):
	""" Query the MySQL database for the names of all of the database tables
		and returns them as a list."""
	query = "Show tables;"
	results = adapter.send_query(query)
	db_tables = []

	# clean the table names
	for table in results:
		db_table_name = table[0]  # remove table name from the tuple
		db_tables.append(db_table_name)
	
	return db_tables

