"""
	Author: George DiNicola
	Description: The seed_blockchain module queries a relational table for
		all of the existing records and creates corresponding blockchain
		records for them on the Hyperledger Fabric network.
"""

import mysql.connector
from mysql.connector import Error

import config
import setup
from RowEncryptionRecord import RowEncryptionRecord
from ColumnEncryptionRecord import ColumnEncryptionRecord
from blockchain import create_blockchain_record, update_blockchain_record
import utils

import pandas as pd
from sqlalchemy import create_engine



# step 0: configure the table name
table_name = "student"

# step 1: get the relational database configuration information
settings = config.load_config()
database = settings["database"]
username = settings["username"]
host_name = settings["host_name"]
p = settings["password"]

# for the records/encryption
key = settings["aes_key"]
iv =  settings["iv"]

# step 2: get all of the rows of the database table (for seeding the blockchain)
#adapter = MysqlAdapter(host_name, database, username, p)
#adapter.connect()
connect_string = 'mysql+pymysql://{}:{}@{}/{}'.format(username, p, host_name, database)
sql_connection = create_engine(connect_string).connect()
results = pd.read_sql_table(table_name=table_name, con=sql_connection)

# for table in list_of_sql_tables:
#query_for_table_records = "select * from " + table_name  # construct the query for getting the data from the table
#results = adapter.send_query(query_for_table_records)


# step 3: convert each record to the row encryption record format
row_encryption_recs = setup.convert_table_to_row_encryption_records(results, table_name)

# step 3 b: convert the results to the column encryption record format
cer = setup.convert_table_to_column_encryption_record(results, table_name)

# step 4
result = update_blockchain_record('0', cer.column_hash)


#step 5: iterate over the row encryption records and commit each to the blockchain
i = 1
for rer in row_encryption_recs:
	# blockchain create record
	print("record :", i)
	print(rer.item_id_hash)
	print(rer.item_hash)
	result = create_blockchain_record(rer.item_id_hash, rer.item_id_AES, rer.item_hash, rer.owned_table_AES)
	i += 1