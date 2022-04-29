# TDRB-Middleware-Extension

https://ieeexplore.ieee.org/abstract/document/9417201

https://ieeexplore-ieee-org.ezproxy.cul.columbia.edu/document/9417201

J. Lian, S. Wang and Y. Xie, "TDRB: An Efficient Tamper-Proof Detection Middleware for Relational Database Based on Blockchain Technology," in IEEE Access, vol. 9, pp. 66707-66722, 2021, doi: 10.1109/ACCESS.2021.3076235.


COMSE6156 - Topics in Software Engineering - Final Project

- Author
  - George DiNicola, gd2581


- List of files submitted:
	--   | -- 			| -- 			| Description
	--   | -- 			| -- 			| --
	` ` | `README.md` 		| -			| 
  ` ` | `` 		| -			| 
	` ` | ` 		| -			| 
	`./proj3` | `run.sh` 	| -			| Bash script to run the project with instead of Python
	`./` | `src/` 			| `.py`         	|
	`./` | `src/` 			| `.py`       	| 
  `./` | `src/` 			| `main.py`       	| Main execution of the application
  
  
PART C:

 - How to run program
  - Note: Assuming use of `python3` and Node v12.
  - Note: Both also assume you are running on a Google Cloud VM that was set up exactly following the given instructions (gc-setup.html)
  - Set up:
    - `pip3 install -r requirements.txt`  
    - `npm install`
  - Run: 
  	- `./run.sh`
  		- Example: 
  - Troubleshooting:
  	- if the run.sh script complains about permissions, please use `chmod u+x run.sh` to grant the permission and try the "Run" step again
  	- if the blockchain refuses transactions to the peer1.organization1.com node, execute the `docker stop peer1.organization1.com` and execute the steps to recreate the wallet.
  


Internal design: 


Functional overview of the internal design (function descriptions):

Python Code
- `main.py`
	- `handle_user_args()` - Handles the input given by the user. 
	- `update()` - Sends a valid update to both the relational database and blockchain.
  - `delete()` - Sends a valid delete to both the relational database and blockchain.
  - `insert()` - Sends a valid insert/create to both the relational database and blockchain.
  - `query()` - Sends a query to the relational database and marks the tampered rows by setting the tamper_column equal to 1.
- `ColumnEncryptionRecord.py` - The ColumnEncryptionRecord class is an implementation of the Column Encryption Record data structure proposed in TDRB. The object has the following attributes: 1. The hash value of the table name, 2. the name of the table encrypted using AES, and the hash value of all of the primary keys in the table.
  - Reference: This data structure/object was proposed in the following study: J. Lian, S. Wang and Y. Xie, "TDRB: An Efficient Tamper-Proof Detection Middleware for Relational Database Based on Blockchain Technology," in IEEE Access, vol. 9, pp. 66707-66722, 2021, doi: 10.1109/ACCESS.2021.3076235.
  - `get_unencrypted_table_name()` - returns the decrypted value of the table name attribute for the column encryption record object.
- `RowEncryptionRecord.py` 
- `blockchain.py` - The blockchain module serves as an API to the blockchain ledger. It calls Nodejs scripts that execute CRUD operations on the ledger and world state database (CouchDB).
  - `query_blockchain()` - Queries the state database using the key/ID.
  - `create_blockchain_record()` - Creates a new blockchain record with the following attributes: 1. Item ID hash value, 2. Item ID encrypted using AES, 3. The hash value of all the items in the row, and 4. The name of the table encrypted using AES.
  - `update_blockchain_record()` - Updates the item hash value of an existing record on the state database. This is used when any of the attribute/column values change for a given row in the relational database table.
  - `delete_blockchain_record()` - Deletes an existing record in the state database.
- `config.py` - The configuration module is meant for a user to configure the application to their relational database, their relational database credentials, and encryption (AES) key.
  - load_config() - Loads the configured environment variables for the application.
- `seed_blockchain.py` - The seed_blockchain module queries a relational table for all of the existing records and creates corresponding blockchain records for them on the Hyperledger Fabric network. 
- `setup.py` - The setup module converts relational database table records to blockchain records represented using the data structures proposed in the TDRB research.
  - `convert_table_to_column_encryption_record()` - Converts a relational table to the column encryption record proposed in TDRB.
  - `convert_table_to_column_encryption_record()` - Converts a relational table to the record encryption records proposed in TDRB.
- `sql.py` 
- `tamper_detection.py` - The tamper_detection module checks for the existence of row encryption record and column encryption record representations
  of the relational database on the blockchain. If the records do not match, the tampering to the relational database (as well as any
  tampering to the blockchain) will be detected.
    - `cerc()` - Algorithm proposed in the TDRB middleware study. Query the blockchain for the column encryption records for the relational table. If the column hash does not match the blockchain column hash, an illegal insert or delete will be detected.
    - `rerc()` - Algorithm proposed in the TDRB middleware study. Query the blockchain for the row encryption records for the relational table. If the column hash does not match the blockchain column hash, an illegal modification is detected.
    - `rerc_new()` - My own updated version of the row encryption record detection algorithm proposed in the TDRB study. This function calls the queryByRange blockchain API (a one-time bulk query) call to use its records to check for the existence of row encryption records.
    - Reference: This data structure/object was proposed in the following study: J. Lian, S. Wang and Y. Xie, "TDRB: An Efficient Tamper-Proof Detection Middleware for Relational Database Based on Blockchain Technology," in IEEE Access, vol. 9, pp. 66707-66722, 2021, doi: 10.1109/ACCESS.2021.3076235.
- `utils.py` - The utils module is a collection of useful functions that are used throughout the application.
	- `get_column_hash()` - Gets the hash value for all of the primary keys in a database table. NOTE: assumes the primary key is the first column in the table!
	- `get_column_hash_pks_only()` - Gets the hash value for all of the primary keys in a list.
  - `SHA_256_conversion()` - Converts a variable of any data type to its corresponding SHA 256 hash value.
  - `get_encrypted_table()` - Encrypts the name of a relational database table using AES encryption.
  - `get_table_name_hash()` - Calculates the SHA 256 hash value for a given relational table name.
  - `get_item_id_hash()` - Calculates the SHA 256 hash value for a given item ID.
  - `get_item_hash_pk_present()` - Calculates the SHA 256 hash value for the contenated attribute value of the given row (EXCEPT the primary key). 
  - `get_encrypted_item_id()` - Encrypts an item ID value using AES encryption.
  - `encode_items()` - Convert a list of items to the UTF-8 encoding of their concatenated result.
  - `get_all_database_tables()` - Queries the MySQL database for the names of all of the database tables and returns them as a list.

Node code:
- `delete.js`
- `enrollAdmin.js`
- `invoke.js`
- `query.js`
- `queryRange.js`
- `registerUser.js`
- `update.js`


Other Details:
- Libraries I used (all of them are built into python and do not have to be installed with `pip`): 
  - `argparse`: A library that makes it easy for processing input from a user to a Python program. I used the argparse library to parse input from the user and have a much cleaner way for specifying parameters by name for the bash script (`run.sh`) executed by the user.
  - `Cryptodome` - A library for AES encryption/decryption functions. Some attributes of the column encryption records and row encryption records are encrypted using AES.
  - `hashlib` - A library for hashing values. Some attributes of the column encryption records and row encryption records are hashed.
  
  
   


