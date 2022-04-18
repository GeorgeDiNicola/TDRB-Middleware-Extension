import hashlib
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

def get_column_hash(results):
	# assumes the primary key is the first column in the table!

	hash_string = []

	for result in results:
		str_pk = str(result[0])  # convert the PKs to string for hashing
		hash_string += str_pk

	final_hash = SHA_256_conversion(hash_string)
	return final_hash


def SHA_256_conversion(data):

	pk = data
	m = hashlib.sha256()
	pk_bytes = str(pk).encode()  # ensure PK is string before conversion
	m.update(pk_bytes)

	return m.hexdigest()


def get_encrypted_table(table_name, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	table_name_str = str(table_name)  # ensure table name is a string before conversion
	return cipher.encrypt(pad(table_name_str.encode(), 16))


def get_table_name_hash(table_name):
	str_table_name = str(table_name)  # ensure table name is string before conversion
	return SHA_256_conversion(str_table_name)


def get_item_id_hash(item_id):
	str_item_id = str(item_id)  # ensure item ID is string before conversion
	return SHA_256_conversion(str_item_id)


def get_item_hash_pk_present(row):
	# concatenate the hash for each column EXCEPT the primary key
	concatenated_items = ""
	for column in row[1:]:  # skip the primary key (1st column)
		concatenated_items += str(column)  # ensure the column is string before conversion
	return SHA_256_conversion(concatenated_items)


def get_encrypted_item_id(item_id, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	item_id_str = str(item_id)  # ensure table name is a string before conversion
	return cipher.encrypt(pad(item_id_str.encode(), 16))


def encode_items(item_list):

	m = hashlib.sha256()

	concat_items = ""
	for item in item_list:
		concat_items += str(item)

	m.update(concat_items.encode())

	return m.hexdigest()


def get_all_database_tables(adapter, database):
	#query = "SELECT table_name FROM information_schema.tables WHERE database = " + database
	query = "Show tables;"
	results = adapter.send_query(query)
	db_tables = []

	# clean the table names
	for table in results:
		db_table_name = table[0]  # remove table name from the tuple
		db_tables.append(db_table_name)
	
	return db_tables

