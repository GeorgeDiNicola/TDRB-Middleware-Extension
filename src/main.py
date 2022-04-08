import hashlib
import argparse
import base64

# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

import config

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

	#m = hashlib.sha256()

	#m.update(b"hello")

	#print(m.hexdigest())

	#print(m.digest_size)
	#print(m.block_size)


	data = b'Text to encrypt'   # 15 bytes
	
	# TODO HAVE THIS BE A UNIFORM KEY IN THE CONFIG FILE
	key = get_random_bytes(32)
	#print(key)

	#b'\x96\xacT\xdfj\xc3\xe8C\x05\xe9\x08=m\x1d\x1c\x00u)<\xcch\xecB\x9c\xde\xda\xe5\xd6Bl\xa6\x91'
	
	iv = get_random_bytes(16)

	cipher1 = AES.new(key, AES.MODE_CBC, iv)
	ct = cipher1.encrypt(pad(data, 16))
	#print(ct)

	cipher2 = AES.new(key, AES.MODE_CBC, iv)
	pt = unpad(cipher2.decrypt(ct), 16)
	print(pt)
	assert(data == pt)