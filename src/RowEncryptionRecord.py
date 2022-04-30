"""
	Author: George DiNicola
	Reference: This data structure/object was proposed in the following study: 
		J. Lian, S. Wang and Y. Xie, "TDRB: An Efficient Tamper-Proof Detection 
		Middleware for Relational Database Based on Blockchain Technology," 
		in IEEE Access, vol. 9, pp. 66707-66722, 2021, doi: 10.1109/ACCESS.2021.3076235.
	Description: The RowEncryptionRecord class is an implementation of the 
		Row Encryption Record data structure proposed in TDRB. The object has
		the following attributes: 1. The hash value of the item (row) ID, 2. the item ID
		 (primary key) encrypted using AES, 3. the hash value of all of the row's attribute
		 (column) values, and 4. the name of the table encrypted using AES.
"""

# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

class RowEncryptionRecord():

	def __init__(self):
		self.item_id_hash = None
		self.item_id_AES = None
		self.item_hash = None
		self.owned_table_AES = None
	
	def get_unencrypted_itemID(self, key, iv):
		d_cipher = AES.new(key, AES.MODE_CBC, iv)
		d_data = d_cipher.decrypt(self.item_id_AES)
		return d_data.decode()

	def get_unencrypted_table_name(self, key, iv):
		d_cipher = AES.new(key, AES.MODE_CBC, iv)
		d_data = d_cipher.decrypt(self.owned_table_AES)
		return d_data.decode()