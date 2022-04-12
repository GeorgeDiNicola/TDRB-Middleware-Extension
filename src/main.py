import hashlib
import argparse
import base64

# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

import config
import utils
import tamper_detection as td
import sql as s
from MysqlAdapter import MysqlAdapter
from RowEncryptionRecord import RowEncryptionRecord
from ColumnEncryptionRecord import ColumnEncryptionRecord

# settings holds the AES encrypt and decrypt key
settings = config.load_config()


def handle_user_args():
	"""Handle the input given by the user."""

	parser = argparse.ArgumentParser(description='TDRB Middleware extension Argument Parser')

	parser.add_argument('--q', dest='query', required=True, type=str,
		nargs='+', help='Query for the middleware to sent to the relational database')

	args = parser.parse_args()

	# check that input from user is valid
	if len(args.query) < 1:
		raise argparse.ArgumentTypeError("The query must not be empty!")

	# how to handle spaces in args: 
	# https://stackoverflow.com/questions/18157376/handle-spaces-in-argparse-input
	space = ' '
	args.query = space.join(args.query)

	return args


if __name__ == '__main__':

	# args = handle_user_args()

	# query = args.query

	
	table_name = "student"
	table_list = ["student"]
	select_students_query = s.SELECT_STUDENT_QUERY


	adapter = MysqlAdapter("localhost", "students", "root")

	adapter.connect()

	key = settings["aes_key"]
	iv =  settings["iv"]
	#iv = get_random_bytes(16)

	cipher = AES.new(key, AES.MODE_CBC, iv)

	td.cerc(table_list, adapter, key, iv)

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


	adapter.disconnect()


	#key = get_random_bytes(32)
	
	

	
	
	#print(ct)

	#cipher2 = AES.new(key, AES.MODE_CBC, iv)
	#pt = unpad(cipher2.decrypt(ct), 16)
	#print(pt)
	#assert(data == pt)