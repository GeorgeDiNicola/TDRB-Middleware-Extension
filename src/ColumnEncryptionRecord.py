# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

class ColumnEncryptionRecord():

	def __init__(self):
		self.table_name_hash = None
		self.aes_table_name = None
		self.column_hash = None

	def get_unencrypted_table_name(self, key, iv):
		d_cipher = AES.new(key, AES.MODE_CBC, iv)
		d_data = d_cipher.decrypt(self.aes_table_name)
		# TODO: decrypt self.owned_table_AES
		return d_data
	
	"""
	def __init__(self, table_name_hash, aes_table_name, column_hash):
		self.table_name_hash = table_name_hash
		self.aes_table_name = aes_table_name
		self.column_hash = column_hash
	"""
	def convert_to_json_kv():
		pass