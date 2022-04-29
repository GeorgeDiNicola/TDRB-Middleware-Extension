"""
	Author: George DiNicola
	Reference: This data structure/object was proposed in the following study: 
		J. Lian, S. Wang and Y. Xie, "TDRB: An Efficient Tamper-Proof Detection 
		Middleware for Relational Database Based on Blockchain Technology," 
		in IEEE Access, vol. 9, pp. 66707-66722, 2021, doi: 10.1109/ACCESS.2021.3076235.
	Description: The ColumnEncryptionRecord class is an implementation of the 
		Column Encryption Record data structure proposed in TDRB. The object has
		the following attributes: 1. The hash value of the table name, 2. the name
		of the table encrypted using AES, and the hash value of all of the primary 
		keys in the table.
"""

# AES functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

class ColumnEncryptionRecord():

	def __init__(self):
		self.table_name_hash = None
		self.table_name_AES = None
		self.column_hash = None

	def get_unencrypted_table_name(self, key, iv):
		""" Get the decrypted value of the table name attribute for 
		  the column encryption record object."""
		d_cipher = AES.new(key, AES.MODE_CBC, iv)
		d_data = d_cipher.decrypt(self.table_name_AES)
		return d_data.decode()