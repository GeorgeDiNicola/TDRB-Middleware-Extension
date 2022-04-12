# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

class RowEncryptionRecord():

	def __init__(self):
		self.itemID_hash = None
		self.itemID_AES = None
		self.item_hash = None
		self.owned_table_AES = None
	
	def get_unencrypted_itemID(self, key, iv):
		d_cipher = AES.new(key, AES.MODE_CBC, iv)
		d_data = d_cipher.decrypt(self.itemID_AES)
		return d_data.decode()

	def get_unencrypted_owned_table(self, key, iv):
		d_cipher = AES.new(key, AES.MODE_CBC, iv)
		# TODO: decrypt self.owned_table_AES
		d_data = d_cipher.decrypt(self.owned_table_AES)
		return d_data.decode()
	"""
	
	def __init__(self, itemID_hash, itemID_AES, item_hash, owned_table):
		self.itemID_hash = itemID_hash
		self.itemID_AES = itemID_AES
		self.item_hash = item_hash
		self.owned_table = owned_table
	"""

	def convert_to_json_kv():
		pass