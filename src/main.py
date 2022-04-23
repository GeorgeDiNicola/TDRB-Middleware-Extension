import mysql.connector
from mysql.connector import Error

import hashlib
import argparse
import base64

# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

import pandas as pd

import setup
import config
import utils
import tamper_detection as td
import sql as s
import blockchain
from MysqlAdapter import MysqlAdapter
from RowEncryptionRecord import RowEncryptionRecord
from ColumnEncryptionRecord import ColumnEncryptionRecord
import pymysql


# settings holds the AES encrypt and decrypt key
settings = config.load_config()


def handle_user_args():
	"""Handle the input given by the user."""

	parser = argparse.ArgumentParser(description='TDRB Middleware extension Argument Parser')

	parser.add_argument('--q', dest='query', required=True, type=str,
		nargs='+', help='Query for the middleware to send to the relational database')
	#parser.add_argument('--t', dest='table', required=True, type=str,
	#	nargs='+', help='Table involved in the query')
	parser.add_argument('--c', dest='command', required=True, type=str,
		nargs='+', help='Command (insert, delete, update, query')
	parser.add_argument('--r', dest='row_to_insert', required=False, type=str,
		nargs='+', help='Command (insert, delete, update, query')
	parser.add_argument('--u', dest='update_template', required=False, type=str,
		nargs='+', help='Command (insert, delete, update, query')
	parser.add_argument('--d', dest='pk_to_delete', required=False, type=str,
		nargs='+', help='Command (insert, delete, update, query')

	args = parser.parse_args()

	# check that input from user is valid
	if len(args.query) < 1:
		raise argparse.ArgumentTypeError("The query must not be empty!")

	# handles spaces in the arguments
	space = ' '
	args.query = space.join(args.query)
	args.command = space.join(args.command)
	if args.row_to_insert:
		args.row_to_insert = space.join(args.row_to_insert)
	if args.update_template:
		args.update_template = space.join(args.update_template)
	# TOOD: change the pk_to_delete var name since I am collecting more of them
	if args.pk_to_delete:
		args.pk_to_delete = space.join(args.pk_to_delete)

	return args


# do LAST. this one might be the hardest one since a second query would be needed to get
#  the plaintext records to hash with the upated record
def update(existing_item_id_hash, new_item_hash):
	
	# send the user's UPDATE sql command to the DB to see if it is valid
	result = adapter.send_query(user_query)

	# send to blockchain if the DB statement was valid and worked
	if result:
		print("Please reformulate SQL query!")
		return False
	
	blockchain_commit_success = blockchain.update_blockchain_record(existing_item_id_hash, new_item_hash)

	# TODO: FIX THIS!  the adapter.send_query(user_query) is committing to mysql before the actual commit
	if blockchain_commit_success:
		# commit the results to the MySQL DB if both user query is valid
		#	and the blockchain insert was successful
		adapter.connection.commit()
	# TODO: add else to return False

	return True



def delete(user_query, adapter, item_id, column_enc_id, updated_primary_key_list):
	
	# send the user's DELETE sql command to the DB to see if it is valid
	result = adapter.send_query(user_query)

	# send to blockchain if the DB statement was valid and worked
	if result:
		print("Please reformulate SQL query!")
		return False
	
	item_id_hash_to_delete = utils.get_item_id_hash(item_id)
	
	# delete the record on the blockchain
	blockchain_rer_commit_success = blockchain.delete_blockchain_record(item_id_hash_to_delete)

	# update the columnhash for the new pk to the blockchain
	new_column_hash = utils.get_column_hash_pks_only(updated_primary_key_list)

	blockchain_cer_commit_success = blockchain.update_blockchain_record(column_enc_id, new_column_hash)

	# TODO: FIX THIS!  the adapter.send_query(user_query) is committing to mysql before the actual commit
	if blockchain_rer_commit_success and blockchain_cer_commit_success:
		# commit the results to the MySQL DB if both user query is valid and the blockchain insert was successful
		adapter.connection.commit()
	# TODO: add else to return False

	return True




# implement second
def insert(user_query, adapter, new_row, table_name, key, iv, column_enc_id, pks_for_new_row):
	# NOTE: user MUST specify a primary key!!!!
	
	# send the user's insert sql command to the DB to see if it is valid
	result = adapter.send_query(user_query)

	# send to blockchain if the DB statement was valid and worked
	if result:
		print("Please reformulate SQL query!")
		return False
	
	
	new_row_id = new_row[0]
	new_itemID_hash = utils.get_item_id_hash(new_row_id)
	new_itemID_AES = utils.get_encrypted_item_id(new_row_id, key, iv)
	new_itemID_AES = new_row[0]
	new_item_hash = utils.get_item_hash_pk_present(new_row)
	new_item_table_AES = utils.get_encrypted_table(table_name, key, iv)
	#new_item_table_AES = table_name

	# create the new record on the blockchain
	blockchain_rer_commit_success = blockchain.create_blockchain_record(new_itemID_hash, new_itemID_AES, new_item_hash, new_item_table_AES)

	# update the columnhash for the new pk to the blockchain
	new_column_hash = utils.get_column_hash_pks_only(pks_for_new_row)

	blockchain_cer_commit_success = blockchain.update_blockchain_record(column_enc_id, new_column_hash)

	# check if successful, if so, commit to the DB
	
	# TODO: FIX THIS!  the adapter.send_query(user_query) is committing to mysql before the actual commit
	if blockchain_rer_commit_success and blockchain_cer_commit_success:
		# commit the results to the MySQL DB if both user query is valid and the blockchain insert was successful
		adapter.connection.commit()
	# TODO: add else to return False

	return True


# implement first
def query(user_query, adapter, tampered_primary_keys):

	# send the user's query to the DB and read in the results as a pandas DF

	# TODO: replace the adapter connection with pymysql
	df = pd.read_sql_query(user_query, adapter.connection)
	df["tamper_column"] = 0  # set the detect column to false

	# TODO: name all PRIMARY KEY columns to ID in mysql!
	if len(tampered_primary_keys) > 0:
		for pk in tampered_primary_keys:
			df.loc[df.student_id == pk, "tamper_column"] = 1  # 1 indicates tampered
	
	# print the results
	print(df)

	return True




if __name__ == '__main__':

	args = handle_user_args()

	user_query = args.query
	user_command = args.command
	if args.row_to_insert:
		row_to_insert = args.row_to_insert
		row_to_insert = row_to_insert.split(',')
	if args.update_template:
		update_template = args.update_template
		update_template = update_template.split(',')
	
	# TOOD: have primary keys to delete as a LIST data structure so I can delete more than 1
	if args.pk_to_delete:
		pks_to_delete = args.pk_to_delete
		pks_to_delete = pks_to_delete.split(',')

	
	table_name = "student"
	#table_list = ["student"]
	database = settings["database"]
	username = settings["username"]
	host_name = settings["host_name"]
	p = settings["password"]


	adapter = MysqlAdapter(host_name, database, username, p)
	adapter.connect()


	# for table in list_of_sql_tables:
	query_for_tamper_check = "select * from " + table_name  # construct the query for getting the data from the table
	results = adapter.send_query(query_for_tamper_check)


	key = settings["aes_key"]
	iv =  settings["iv"]
	#iv = get_random_bytes(16)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	

	# get the column encryption records and row encryption records for the database table
	col_encryption_rec = setup.convert_table_to_column_encryption_record(results, table_name)
	row_encryption_recs = setup.convert_table_to_record_encryption_records(results, table_name)

	# detect illegal modification step
	rerc_tamper_flag, rerc_tampered_primary_keys = td.rerc(results, table_name, adapter, key, iv)

	# detect illegal insert or delete step
	cerc_tamper_flag, cerc_info = td.cerc(col_encryption_rec, table_name, adapter, key, iv)

	# print the tampering info to the user before showing them the query results
	if rerc_tamper_flag == 1:
		# return tamper information
		print("RERC TAMPERING INFO: the data has been tampered with")
	if cerc_tamper_flag == 1:
		print("CERC TAMPERING INFO: the data has been tampered with")
	
	# data not tampered with

	# handle the user's query when no detection
	if user_command == "query":
		res = query(user_query, adapter, rerc_tampered_primary_keys)
	elif user_command == "insert" and rerc_tamper_flag == 0 and cerc_tamper_flag == 0:
		# NOTE: DO NOT INSERT IF THE TAMPERING FLAG IS TRUE!
		pks = [item[0] for item in results]  # get pks
		new_pk = pks[-1] + 1
		pks.append(new_pk)
		cer_id = col_encryption_rec.table_name_hash  # need this to update the column encryption record
		res = insert(user_query, adapter, row_to_insert, table_name, key, iv, cer_id, pks)
	elif user_command == "delete" and rerc_tamper_flag == 0 and cerc_tamper_flag == 0:
		pks = [item[0] for item in results]  # get pks
		pk_to_delete = pks_to_delete[0]
		pks.remove(int(pk_to_delete))
		cer_id = col_encryption_rec.table_name_hash  # need this to update the column encryption record
		res = delete(user_query, adapter, pk_to_delete, cer_id, pks)
	#elif user_command == "update":
		# NOTE: DO NOT INSERT IF THE TAMPERING FLAG IS TRUE!
	#	item_id = update_template[0]
	#	item_id = update_template[0]
	#	res = update(user_query, adapter, row_to_insert, table_name, key, iv)



	# disconnect from database
	adapter.disconnect()


	# add all of the row encryption records to the blockchain:

	#for rer in row_encryption_recs:
	#	print(rer)
	#	blockchain.create_blockchain_record(rer.item_id_hash, rer.item_id_AES, rer.item_hash, rer.owned_table_AES)




	

	# read the original records
	"""
	print("\n====Column Encryption Record====\n")
	print(col_encryption_rec.table_name_hash)
	print(col_encryption_rec.get_unencrypted_table_name(key, iv))
	print(col_encryption_rec.column_hash)
	print("==============================\n")

	print("====Row Encryption Records====\n")
	i = 1
	for rer in row_encryption_recs:
		print("record :", i)
		print(rer.item_id_hash)
		print(rer.get_unencrypted_itemID(key, iv))
		print(rer.item_hash)
		print(rer.get_unencrypted_table_name(key, iv))
		i += 1
	"""


	


	# read the ENCRYPTED records
	"""
	print("\n====Column Encryption Record====\n")
	print(col_encryption_rec.table_name_hash)
	print(col_encryption_rec.table_name_AES)
	print(col_encryption_rec.column_hash)
	print("==============================\n")

	print("====Row Encryption Records====\n")
	i = 1
	for rer in row_encryption_recs:
		print("record :", i)
		print(rer.item_id_hash)
		print(rer.item_id_AES)
		print(rer.item_hash)
		print(rer.owned_table_AES)
		i += 1
	"""


	#all_tables = utils.get_all_database_tables(adapter, database)
	#for table_name in all_tables:
	#	print(table_name)


	# read the original records
	"""
	print("\n====Column Encryption Record====\n")
	print(col_encryption_rec.table_name_hash)
	print(col_encryption_rec.get_unencrypted_table_name(key, iv))
	print(col_encryption_rec.column_hash)
	print("==============================\n")

	print("====Row Encryption Records====\n")
	i = 1
	for rer in row_encryption_recs:
		print("record :", i)
		print(rer.item_id_hash)
		print(rer.get_unencrypted_itemID(key, iv))
		print(rer.item_hash)
		print(rer.get_unencrypted_table_name(key, iv))
		i += 1
	"""

	

	# update students set age = years_old
	#insert into students(id, name, age) values (4, "james", 49)
	# create table student(student_id INT NOT NULL,name VARCHAR(25) NOT NULL,sex VARCHAR(25) NOT NULL,age INT NOT NULL,PRIMARY KEY ( student_id ));

	#td.cerc(table_list, adapter, key, iv)

	#td.rerc(table_name, adapter, key, iv)

	"""
	result = adapter.send_query(select_students_query)

	item_hash_list = []
	for row in result:
		temp_list = []
		for item in row:
			temp_list.append(item)
		item_hash_list.append(temp_list)

	print(item_hash_list)


	print(table_name)
	print(len(result))
	# convert the results into the row_encryption_records

	#m = hashlib.sha256()

	#m.update(b"hello")

	#print(m.hexdigest())

	#print(m.digest_size)
	#print(m.block_size)


	# row encryption records

	#data = b'Text to encrypt'   # 15 bytes
	key = settings["aes_key"]
	iv = get_random_bytes(16)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	#ct = cipher1.encrypt(pad(data, 16))

	# table 1
	#student_ID = [1, 2, 3]
	#name = ['Alice', 'Bob', 'Peter']
	#sex = ['Female', 'Male', 'Male']
	#age = ["20", "21", "22"]

	row_encryption_records = []
	
	# TODO: the below will go in the tampering detection module
	#  and the conversion for the actual push to the blockchain
	for row in item_hash_list:
		rer_temp = RowEncryptionRecord()
		pk = row[0]
		rer_temp.itemID_hash = utils.SHA_256_conversion(pk)
		rer_temp.itemID_AES = utils.AES_conversion(cipher, pk)

		rer_temp.item_hash = utils.encode_items(row)
		rer_temp.owned_table_AES = utils.AES_conversion(cipher, table_name)
		row_encryption_records.append(rer_temp)


	for r in row_encryption_records:
		print("===========")
		print(r.itemID_hash)
		print(r.itemID_AES)
		print(r.item_hash)
		print(r.owned_table_AES)


	cipher_d = AES.new(key, AES.MODE_CBC, iv)
	#d_data = cipher_d.decrypt(e_data)

	# decrypt the data
	for r in row_encryption_records:
		print("===========")
		print(r.itemID_hash)
		#print(r.get_unencrypted_itemID(key, iv))
		print(r.item_hash)
		# TODO: fix the below
		#print(r.get_unencrypted_owned_table(key, iv))



	# column encryption records
	pks = []
	for row in item_hash_list:
		pks.append(row[0])
	
	print("===== Column E Record=====")
	cer = ColumnEncryptionRecord()
	cer.table_name_hash = utils.SHA_256_conversion(pk)
	cer.aes_table_name = utils.AES_conversion(cipher, pk)
	cer.column_hash = utils.encode_items(pks)

	print(cer.table_name_hash)
	print(cer.aes_table_name)
	print(cer.column_hash)

	print(cer.get_unencrypted_table_name(key, iv))
	"""


	#key = get_random_bytes(32)
	
	

	
	
	#print(ct)

	#cipher2 = AES.new(key, AES.MODE_CBC, iv)
	#pt = unpad(cipher2.decrypt(ct), 16)
	#print(pt)
	#assert(data == pt)