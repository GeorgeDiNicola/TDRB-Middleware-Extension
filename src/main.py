import hashlib
import argparse
import base64

# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

import config
import utils
from MysqlAdapter import MysqlAdapter
from RowEncryptionRecord import RowEncryptionRecord

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

	select_students_query = "SELECT * FROM student"
	table_name = "student"


	adapter = MysqlAdapter("localhost", "students", "root")

	adapter.connect()

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

	#data = b'Text to encrypt'   # 15 bytes
	key = settings["aes_key"]
	iv = get_random_bytes(16)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	#ct = cipher1.encrypt(pad(data, 16))

	# table 1
	table_name = 'Student'
	student_ID = [1, 2, 3]
	name = ['Alice', 'Bob', 'Peter']
	sex = ['Female', 'Male', 'Male']
	age = ["20", "21", "22"]

	r1_test = RowEncryptionRecord()
	
	pk = student_ID[0]

	r1_test.itemID_hash = utils.SHA_256_conversion(pk)

	# TODO: a later func should check data types
	r1_test.itemID_AES = utils.AES_conversion(cipher, pk)
	
	items = [student_ID[0], sex[0], age[0]]
	r1_test.item_hash = utils.encode_items(items)
	
	r1_test.owned_table = utils.AES_conversion(cipher, table_name)
	

	print(r1_test.itemID_hash)
	print(r1_test.itemID_AES)
	print(r1_test.item_hash)
	print(r1_test.owned_table)


	adapter.disconnect()


	#key = get_random_bytes(32)
	
	

	
	
	#print(ct)

	#cipher2 = AES.new(key, AES.MODE_CBC, iv)
	#pt = unpad(cipher2.decrypt(ct), 16)
	#print(pt)
	#assert(data == pt)