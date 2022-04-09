import hashlib
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

def convert_relational_to_row_encyption_record():
	
	# key -> value
	pass

def convert_relational_to_column_encyption_record():
	# key -> value
	pass




def encode_items(item_list):

	m = hashlib.sha256()

	concat_items = ""
	for item in item_list:
		concat_items += str(item)

	m.update(concat_items.encode())

	return m.hexdigest()


def AES_conversion(cipher, data):
	
	c = cipher

	# TODO: add data type check
	data = str(data)

	return c.encrypt(pad(data.encode(), 16))


def SHA_256_conversion(data):

	# TODO: test data type
	pk = data

	m = hashlib.sha256()

	pk_bytes = str(pk).encode()
	
	m.update(pk_bytes)

	return m.hexdigest()