import mysql.connector
from mysql.connector import Error

import config
import setup
from RowEncryptionRecord import RowEncryptionRecord
from ColumnEncryptionRecord import ColumnEncryptionRecord
from blockchain import create_blockchain_record
import utils

from MysqlAdapter import MysqlAdapter



# step 0: configure the table name
table_name = "student"

# step 1: get the relational database configuration information
settings = config.load_config()
table_name = "student"
database = settings["database"]
username = settings["username"]
host_name = settings["host_name"]
p = settings["password"]

# for the records/encryption
key = settings["aes_key"]
iv =  settings["iv"]

# step 2: get all of the rows of the database table (for seeding the blockchain)
adapter = MysqlAdapter(host_name, database, username, p)
adapter.connect()
# for table in list_of_sql_tables:
query_for_table_records = "select * from " + table_name  # construct the query for getting the data from the table
results = adapter.send_query(query_for_table_records)

print(results)


# step 3: convert each record to the row encryption record format
row_encryption_recs = setup.convert_table_to_record_encryption_records(results, table_name)

#TODO: add for column level encryption too!

#step 4: iterate over the row encryption records and commit each to the blockchain
i = 1
for rer in row_encryption_recs:
	# blockchain create record
	print("record :", i)
	item_id_hash = str(rer.item_id_hash)
	#item_id = rer.get_unencrypted_itemID(key, iv)
	item_id = str(rer.item_id_AES)
	item_hash = str(rer.item_hash)
	owned_table = str(table_name)
	result = create_blockchain_record(item_id_hash, item_id, item_hash, owned_table)
	i += 1