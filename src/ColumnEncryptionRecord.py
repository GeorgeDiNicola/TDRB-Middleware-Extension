# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

class ColumnEncryptionRecord():

	def __init__(self):
		self.table_name_hash = None
		self.table_name_AES = None
		self.column_hash = None

	def get_unencrypted_table_name(self, key, iv):
		d_cipher = AES.new(key, AES.MODE_CBC, iv)
		d_data = d_cipher.decrypt(self.table_name_AES)
		return d_data.decode()
	
	"""
	def __init__(self, table_name_hash, table_name_AES, column_hash):
		self.table_name_hash = table_name_hash
		self.table_name_AES = table_name_AES
		self.column_hash = column_hash
	"""
	def convert_to_json_kv():
		pass