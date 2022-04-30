"""
	Author: George DiNicola
	Reference: This data structure/object was proposed in the following study: 
		J. Lian, S. Wang and Y. Xie, "TDRB: An Efficient Tamper-Proof Detection 
		Middleware for Relational Database Based on Blockchain Technology," 
		in IEEE Access, vol. 9, pp. 66707-66722, 2021, doi: 10.1109/ACCESS.2021.3076235.
	Description: The setup module converts relational database table records to blockchain
		records represented using the data structures proposed in the TDRB research.
"""

# AES encryption/decryption functions
import hashlib
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

import config
import utils
from RowEncryptionRecord import RowEncryptionRecord
from ColumnEncryptionRecord import ColumnEncryptionRecord

# settings holds the AES encrypt and decrypt key
settings = config.load_config()


def convert_table_to_column_encryption_record(table, table_name):
	""" Convert a relational table to the column encryption record proposed in
	  TDRB."""
	
	cer = ColumnEncryptionRecord()

	primary_keys = set(table['id'])  # get the primary keys

	concatentated_primary_keys = "".join(map(str,primary_keys))  # concatenate the primary keys (for hash)
	cer.column_hash = utils.SHA_256_conversion(concatentated_primary_keys)  # hash the concatenated primary keys

	cer.table_name_hash = utils.get_table_name_hash(table_name)
	cer.table_name_AES = utils.get_encrypted_table(table_name, settings["aes_key"], settings["iv"])
	
	return cer


def convert_table_to_row_encryption_records(table, table_name):
	""" Convert a relational table to the record encryption records proposed in
	  TDRB."""
	
	row_encryption_records = []

	for index, row in table.iterrows():
		rer = RowEncryptionRecord()
		item_id = str(row["id"])
		rer.item_id_hash = item_id  #utils.get_item_id_hash(item_id)
		#rer.item_hash = utils.get_item_hash_pk_present(row)
		concatentated_items = "".join(map(str,row[1:]))  # concatenate the primary keys (for hash)
		rer.item_hash = utils.SHA_256_conversion(concatentated_items)  # hash the items in the row
		rer.item_id_AES = item_id
		rer.owned_table_AES = utils.get_encrypted_table(table_name, settings["aes_key"], settings["iv"])
		row_encryption_records.append(rer)
	
	return row_encryption_records