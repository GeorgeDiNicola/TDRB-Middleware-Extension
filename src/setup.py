# AES encryption/decryption functions
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

import config
import utils
from RowEncryptionRecord import RowEncryptionRecord
from ColumnEncryptionRecord import ColumnEncryptionRecord
from MysqlAdapter import MysqlAdapter

# settings holds the AES encrypt and decrypt key
settings = config.load_config()

def convert_table_to_column_encryption_record(adapter, table_name):
	
	query = "select * from " + table_name  # construct the query for getting the data from the table
	results = adapter.send_query(query)
	cer = ColumnEncryptionRecord()

	cer.column_hash = utils.get_column_hash(results)
	cer.table_name_hash = utils.get_table_name_hash(table_name)
	cer.table_name_AES = utils.get_encrypted_table(table_name, settings["aes_key"], settings["iv"])
	return cer


def convert_table_to_record_encryption_records(adapter, table_name):
	
	query = "select * from " + table_name  # construct the query for getting the data from the table
	results = adapter.send_query(query)
	rer_list = []
	
	for row in results:
		rer = RowEncryptionRecord()
		item_id = row[0]
		rer.item_id_hash = utils.get_item_id_hash(item_id)
		rer.item_hash = utils.get_item_hash(row)
		rer.item_id_AES = utils.get_encrypted_item_id(item_id, settings["aes_key"], settings["iv"])
		rer.owned_table_AES = utils.get_encrypted_table(table_name, settings["aes_key"], settings["iv"])
		rer_list.append(rer)
	
	return rer_list