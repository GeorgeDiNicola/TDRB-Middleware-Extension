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
from sqlalchemy import create_engine

import setup
import config
import utils
import tamper_detection as td
import sql as s
import blockchain
from RowEncryptionRecord import RowEncryptionRecord
from ColumnEncryptionRecord import ColumnEncryptionRecord
#import pymysql


# settings holds the AES encrypt and decrypt key
settings = config.load_config()


def handle_user_args():
	"""Handle the input given by the user."""

	parser = argparse.ArgumentParser(description='TDRB Middleware extension Argument Parser')

	parser.add_argument('--q', dest='query', required=True, type=str,
		nargs='+', help='Query for the middleware to send to the relational database')
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
	if args.pk_to_delete:
		args.pk_to_delete = space.join(args.pk_to_delete)

	return args


def update(user_query, sql_connection, sql_table, existing_item_id_hash, updated_item_value):
	""" Make a valid update to both the relational database and blockchain."""
	
	# send the user's UPDATE sql command to the DB to see if it is valid
	result = sql_connection.execute(user_query)

	# get the new item hash
	update_col_name = 'name'
	
	# update the pandas dataframe

	# row #, col #
	#sql_table.iat[0, 1]=updated_item_value
	row = sql_table.loc[sql_table['student_id'] == int(existing_item_id_hash)]
	print("Row being updated: ", row)
	row[update_col_name] = updated_item_value
	items = row.values.tolist()

	#sql_table[update_col_name][str(existing_item_id_hash)] = updated_item_value
	#print(sql_table)

	#row = sql_table.iat[0,0:7]
	#items = list(row)

	# get the new row
	#items = sql_table[sql_table.loc[sql_table.student_id == str(existing_item_id_hash)]]
	#items = list(sql_table.iloc[])
	#items = sql_table.loc[sql_table['student_id'] == existing_item_id_hash]
	items = items[0]
	print("New row values: ", items)
	concatentated_items = "".join(map(str,items[1:]))  # concatenate the primary keys (for hash)

	new_item_hash = utils.SHA_256_conversion(concatentated_items)

	# send to blockchain if the DB statement was valid and worked
	#if result:
	#	print("Please reformulate SQL query!")
	#	return False
	
	blockchain_commit_success = blockchain.update_blockchain_record(existing_item_id_hash, new_item_hash)

	# TODO: FIX THIS!  the adapter.send_query(user_query) is committing to mysql before the actual commit
	if blockchain_commit_success:
		# commit the results to the MySQL DB if both user query is valid
		#	and the blockchain insert was successful
		print("Update statement successfully executed")
	# TODO: add else to return False

	return True



def delete(user_query, sql_connection, item_id, updated_primary_key_list):
	""" Send a valid delete to both the relational database and blockchain."""
	
	# send the user's DELETE sql command to the DB
	result = sql_connection.execute(user_query)

	# send to blockchain if the DB statement was valid and worked
	if not result:
		print("ERROR: Invalid SQL syntax")
		return False
	
	item_id_hash_to_delete = item_id  # utils.get_item_id_hash(item_id)
	
	# delete the record on the blockchain
	blockchain_rer_commit_success = blockchain.delete_blockchain_record('RECORD' + item_id_hash_to_delete)

	# update the columnhash for the new pk to the blockchain
	concatentated_primary_keys = "".join(map(str,primary_keys))  # concatenate the primary keys (for hash) #utils.get_column_hash_pks_only(updated_primary_key_list)
	new_column_hash = utils.SHA_256_conversion(concatentated_primary_keys)

	blockchain_cer_commit_success = blockchain.update_blockchain_record('0', new_column_hash)

	if blockchain_rer_commit_success and blockchain_cer_commit_success:
		print("Delete statement successfully executed")
	else:
		return False

	return True


def insert(user_query, sql_connection, new_row, table_name, key, iv, pks_for_new_row):
	""" Send a valid insert/create to both the relational database and blockchain."""
	# NOTE: user MUST specify a primary key!!!!
	
	# send the user's insert sql command to the DB
	result = sql_connection.execute(user_query)

	# send to blockchain if the DB statement was valid and worked
	if not result:
		print("ERROR: Invalid SQL syntax")
		return False
	
	new_row_id = new_row[0]
	new_itemID_hash = new_row_id  #utils.get_item_id_hash(new_row_id)
	

	# must do since encryption causes failure on id 128
	new_itemID_AES = new_row_id
	# new_itemID_AES = utils.get_encrypted_item_id(new_row_id, key, iv)

	concatentated_items = "".join(map(str,new_row[1:]))  # concatenate the primary keys (for hash)
	new_item_hash = utils.SHA_256_conversion(concatentated_items)
	new_item_table_AES = utils.get_encrypted_table(table_name, key, iv)

	# create the new record on the blockchain
	blockchain_rer_commit_success = blockchain.create_blockchain_record(new_itemID_hash, new_itemID_AES, new_item_hash, new_item_table_AES)

	# update the columnhash for the new pk to the blockchain
	concatentated_primary_keys = "".join(map(str,pks_for_new_row))  # concatenate the primary keys (for hash)
	new_column_hash = utils.SHA_256_conversion(concatentated_primary_keys)  # hash the concatenated primary keys

	blockchain_cer_commit_success = blockchain.update_blockchain_record('0', new_column_hash)

	if blockchain_rer_commit_success and blockchain_cer_commit_success:
		print("Insert statement successfully executed")
	else:
		return False

	return True


def query(user_query, sql_connection, tampered_primary_keys, rerc_tamper_flag, cerc_tamper_flag):
	""" Send a query to the relational database and mark the tampered rows by
		setting the tamper_column equal to 1."""

	# send the user's query to the DB and read in the results as a pandas DF
	try:
		df = pd.read_sql_query(user_query, sql_connection)
	except:
		print("ERROR: Invalid SQL syntax")
		return False
	
	df["tamper_column"] = 0  # set the detect column to false		
	if len(tampered_primary_keys) > 0:
		for pk in tampered_primary_keys:
			df.loc[df.id == int(pk), "tamper_column"] = 1  # 1 indicates tampered

	if cerc_tamper_flag == 1 and rerc_tamper_flag == 1:
		if len(df.loc[df.tamper_column == 1]) > 0:
			print("The records below contain an illegal modification and/or insert and are marked in the tamper_column\n")
		else:
			print("The records below are missing one or more valid rows (illegal deletion)\n")
	elif cerc_tamper_flag == 1:
		if len(df.loc[df.tamper_column == 1]) > 0:
			print("The records below contain an illegal insertion and are marked in the tamper_column\n")
		else:
			print("The records below are missing one or more valid rows (illegal deletion)\n")
	elif rerc_tamper_flag == 1:
		print("The records below contain an illegal modification and are marked in the tamper_column\n")

	print(df)  # display the results to the user

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

	
	# TODO: how should I specify the name of the table????
	table_name = "student"
	

	database = settings["database"]
	username = settings["username"]
	host_name = settings["host_name"]
	p = settings["password"]

	# query SQL for the table to check for tampering (SQLAlchemy connection)
	connect_string = 'mysql+pymysql://{}:{}@{}/{}'.format(username, p, host_name, database)
	sql_connection = create_engine(connect_string).connect()

	sql_data = pd.read_sql_table(table_name=table_name, con=sql_connection)

	# cryptography settings
	key = settings["aes_key"]
	iv =  settings["iv"]  # iv = get_random_bytes(16)
	cipher = AES.new(key, AES.MODE_CBC, iv)

	# get the column encryption records and row encryption records for the database table
	col_encryption_rec = setup.convert_table_to_column_encryption_record(sql_data, table_name)
	row_encryption_recs = setup.convert_table_to_row_encryption_records(sql_data, table_name)

	# detect illegal insert or delete step
	cerc_tamper_flag, cerc_info = td.cerc(col_encryption_rec, table_name, key, iv)

	# detect illegal modification step
	rerc_tamper_flag, rerc_tampered_primary_keys = td.rerc_new(row_encryption_recs, table_name, key, iv)

	# print the tampering info to the user before showing them the query results
	if rerc_tamper_flag == 1:
		# return tamper information
		print("TAMPERING DETECTED - ILLEGAL MODIFICATION: the data has been tampered with")
	if cerc_tamper_flag == 1:
		print("TAMPERING DETECTED - ILLEGAL INSERT/DELETE: the data has been tampered with")

	# move forward with the user's chosen operation
	if user_command == "query":
		res = query(user_query, sql_connection, rerc_tampered_primary_keys, rerc_tamper_flag, cerc_tamper_flag)
	elif user_command == "insert" and rerc_tamper_flag == 0 and cerc_tamper_flag == 0:
		primary_keys = list(sql_data['id'])  # get the primary keys
		new_pk = row_to_insert[0]
		primary_keys.append(new_pk)
		cer_id = col_encryption_rec.table_name_hash  # need this to update the column encryption record
		res = insert(user_query, sql_connection, row_to_insert, table_name, key, iv, primary_keys)
	elif user_command == "delete" and rerc_tamper_flag == 0 and cerc_tamper_flag == 0:
		primary_keys = list(sql_data['id'])  # get the primary keys
		pk_to_delete = pks_to_delete[0]
		primary_keys.remove(int(pk_to_delete))
		#cer_id = col_encryption_rec.table_name_hash  # need this to update the column encryption record
		res = delete(user_query, sql_connection, pk_to_delete, primary_keys)
	elif user_command == "update" and rerc_tamper_flag == 0 and cerc_tamper_flag == 0:
		item_id = update_template[0]
		update_value = update_template[1]
		res = update(user_query, sql_connection, sql_data, item_id, update_value)
	else:
		print("Cannot insert, update, or delete records. The underlying table has been modified")

