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
  `src/` | `requirements.txt` 		| -			| The required modules and module version numbers the Python application depends on.
	`src/` | `main.py` 			| ``         	| Main execution of the application 
	`src/` | `blockchain.py` 			| ``       	| The blockchain module serves as an API to the blockchain ledger. It calls Nodejs scripts that execute CRUD operations on the ledger and world state database (CouchDB).
  `src/` | `ColumnEncrypionRecord.py`       | ``        | The ColumnEncryptionRecord class is an implementation of the Column Encryption Record data structure proposed in TDRB. The object has the following attributes: 1. The hash value of the table name, 2. the name of the table encrypted using AES, and the hash value of all of the primary keys in the table.
  `src/` | `config.py`      | ``        | The configuration module is meant for a user to configure the application to their relational database, their relational database credentials, and encryption (AES) key.
  `src/` | `RowEncryptionRecord.py`      | ``        | The RowEncryptionRecord class is an implementation of the Row Encryption Record data structure proposed in TDRB. The object has the following attributes: 1. The hash value of the item (row) ID, 2. the item ID (primary key) encrypted using AES, 3. the hash value of all of the row's attribute (column) values, and 4. the name of the table encrypted using AES.
  `src/` | `seed_blockchain.py`      | ``        | The seed_blockchain module queries a relational table for all of the existing records and creates corresponding blockchain records for them on the Hyperledger Fabric network.
  `src/` | `setup.py`      | ``        | The setup module converts relational database table records to blockchain records represented using the data structures proposed in the TDRB research.
  `src/` | `tamper_detection.py`      | ``        | The tamper_detection module checks for the existence of row encryption record and column encryption record representations of the relational database on the blockchain. If the records do not match, the tampering to the relational database (as well as any tampering to the blockchain) will be detected.
  `src/` | `test_delete.sh`      | ``        | Test script for committing a valid delete operation to the blockchain and relational database through the middleware app using the method I proposed queryByRange.
  `src/` | `test_delete_original_method.sh`      | ``        | Test script for committing a valid delete operation to the blockchain and relational database through the middleware app using the method proposed in the TDRB study.
  `src/` | `test_insert.sh`      | ``        | Test script for committing a valid insert operation to the blockchain and relational database through the middleware app using the method I proposed with queryByRange.
  `src/` | `test_insert_original_method.sh`      | ``        | Test script for committing a valid insert operation to the blockchain and relational database through the middleware app using the method proposed in the TDRB study.
  `src/` | `test_query.sh`      | ``        | Test script for querying the blockchain and relational database through the middleware app using the method I proposed queryByRange.
  `src/` | `test_query_original_method.sh`      | ``        | Test script for querying blockchain and relational database through the middleware app using the method proposed in the TDRB study.
  `src/` | `test_update.sh`      | ``        | Test script for committing a valid update operation to the blockchain and relational database through the middleware app using the method I proposed queryByRange.
  `src/` | `test_update_original_method.sh`      | ``        | Test script for committing a valid update operation to the blockchain and relational database through the middleware app using the method proposed in the TDRB study.
  `src/` | `utils.py`      | ``        | The utils module is a collection of useful functions that are used throughout the application.
  `src/` | `delete.js`      | ``        | deletes a record on the blockchain using the ID of its key value (the application uses its item ID hash value).
  `src/` | `enrollAdmin.js`      | ``        | (from the FabCar tutorial referenced in this README) creates an admin priviledged user.
  `src/` | `invoke.js`      | ``        | creates/inserts a record on the blockchain using the ID of its key value (the application uses its item ID hash value).
  `src/` | `query.js`      | ``        | queries a record on the blockchain using the ID of its key value (the application uses its item ID hash value).
  `src/` | `queryByRange.js`      | ``        | The utils module is a collection of useful functions that are used throughout the application.
  `src/` | `registerUser.js`      | ``        | (from the FabCar tutorial referenced in this README) creates a new user called "user1" that can interact with the user. The crypto wallet for the user is added to the current working directory.s
  `src/` | `update.js`      | ``        | updates a record on the blockchain using the ID of its key value (the application uses its item ID hash value)
  `src/` | `sql/`      | `create_student.sql`        | Database creation, table creation, and seeding script for the example data shown in the TDRB study.
  `src/` | `sql/`      | `moon_comparison.sql`        | Database creation, table creation, and seeding script for the test data used in the MOON study.
  `src/` | `fabric/chaincode/record`      | `record.js`      | The javascript and javascript low-level chaincode deployed onto the peer nodes for the blockchain network. These scripts contain the business logic for the middleware application that each peer node should adhere to (i.e. handing of query, insert/create, update, delete operations). These scripts are modified from the originals found in the Hyperledger "Fabcar" tutorial referenced by the README.
  `src/` | `fabric/config/`      | `configtx.yaml`, `core.yaml`, `orderer.yaml`     | Configuration files (.yaml format) for the blockchain network to run over Docker. These scripts are from the Hyperledger "Fabcar" tutorial referenced by the README.
  `src/` | `fabric/first-network/`      | ``     | Scripts for the commands to start the blockchain network and install the necessary chaincode on the network peers for the "fist network" configuration from Hyperledger Fabric. These scripts are from the Hyperledger "Fabcar" tutorial referenced by the README.
  `src/` | `fabric/basic-network/`      | ``     | Scripts for the commands to start the blockchain network and install the necessary chaincode on the network peers for the "basic network" configuration from Hyperledger Fabric. These scripts are from the Hyperledger "Fabcar" tutorial referenced by the README.
  `src/` | `milestone_assignments/`      | ``     | Directory containing the milestone assignments for COMSE6156 outlining the proposal and progress for this project.
   `src/` | `test_logs/`      | ``     | Directory containing the logs from the evaluation described in the final report.



 - How to run program
  - Note: Assuming use of `python3` and Node v12.
  - Set up:
    - Install the required Python libraries/modules: `pip3 install -r requirements.txt`  
    - Install the required Node.js libraries/modules: `npm install`
    - Start the blockchain network (this step will take about two minutes to execute): `./startFabric javascript`
    - Enroll yourself as the admin user: `node enrollAdmin.js`
    - Create a user called 'user1' `node registerUser.js`
    - (if necessary) seed the blockchain using the configured relational database using the following command (specify the table from within the script): `python3 seed_blockchain.py"
  - Run: 
  	- Query records using the middleware: `python3 main.py --q "<SQL Query>" --c "query"`
  		- Example: `python3 main.py --q "select * from student" --c "query"`
	- Insert a record using the middleware: `python3 main.py --q "<SQL Insert statement>" --c "insert" --r "<row to insert separated by commas>"`
  		- Example: `python3 main.py --q "insert into student (id, name, sex, age) values (1, 'John', 'Male', 20);" --c "insert" --r "1,John,Male,20"`
  	- Update a record using the middleware: `python3 main.py --q "<SQL Update statement>" --c "update" --u "<primary key to update>, <new update value>"`
  		- Example: `python3 main.py --q "update student set name='Alice' where id=1" --c "update" --u "1,Alice"`
  	- Delete a record using the middleware: `python3 main.py --q "<SQL Delete statement>" --c "delete" --d <primary key of the record to delete>`
  		- Example: `python3 main.py --q "delete from student where id=1" --c "delete" --d 1`
  - Troubleshooting:
  	- if the run.sh script complains about permissions, please use `chmod u+x run.sh` to grant the permission and try the "Run" step again
  	- if the blockchain refuses transactions to the peer1.organization1.com node, execute the `docker stop peer1.organization1.com` and execute the steps to recreate the wallet.
  	- if the following error occurs "ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running?", change the permissions for the Docker network communication socket using the following command: `sudo chmod 666 /var/run/docker.sock`
  


Functional overview of the internal design (function descriptions):

Python Code
- `main.py` - Main execution of the application
	- `handle_user_args()` - Handles the input given by the user. 
	- `update()` - Sends a valid update to both the relational database and blockchain.
  - `delete()` - Sends a valid delete to both the relational database and blockchain.
  - `insert()` - Sends a valid insert/create to both the relational database and blockchain.
  - `query()` - Sends a query to the relational database and marks the tampered rows by setting the tamper_column equal to 1.
- `ColumnEncryptionRecord.py` - The ColumnEncryptionRecord class is an implementation of the Column Encryption Record data structure proposed in TDRB. The object has the following attributes: 1. The hash value of the table name, 2. the name of the table encrypted using AES, and the hash value of all of the primary keys in the table.
  - Reference: This data structure/object was proposed in the following study: J. Lian, S. Wang and Y. Xie, "TDRB: An Efficient Tamper-Proof Detection Middleware for Relational Database Based on Blockchain Technology," in IEEE Access, vol. 9, pp. 66707-66722, 2021, doi: 10.1109/ACCESS.2021.3076235.
  - `get_unencrypted_table_name()` - returns the decrypted value of the table name attribute for the column encryption record object.
- `RowEncryptionRecord.py` - The RowEncryptionRecord class is an implementation of the Row Encryption Record data structure proposed in TDRB. The object has the following attributes: 1. The hash value of the item (row) ID, 2. the item ID (primary key) encrypted using AES, 3. the hash value of all of the row's attribute (column) values, and 4. the name of the table encrypted using AES.
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


The below node code came from the following example, which I modified for the purposes of the middleware app: https://hyperledger-fabric.readthedocs.io/en/release-1.4/write_first_app.html
Node code:
- `delete.js` - deletes a record on the blockchain using the ID of its key value (the application uses its item ID hash value)
- `enrollAdmin.js` - (from the tutorial referenced above) creates an admin priviledged user.
- `invoke.js` - creates/inserts a record on the blockchain using the ID of its key value (the application uses its item ID hash value)
- `query.js` - queries a record on the blockchain using the ID of its key value (the application uses its item ID hash value)
- `queryRange.js`- queries a range of records on the blockchain
- `registerUser.js` - (from the tutorial referenced above) creates a new user called "user1" that can interact with the user. The crypto wallet for the user is added to the current working directory.s
- `update.js` - updates a record on the blockchain using the ID of its key value (the application uses its item ID hash value)


Instructions for reproducing the tests I've conducted:

Research Question 1:
	Step 1: Follow the setup instructions listed at the beginning of the README.
	Step 2: Seed the MySQL database using the create_student.sql seeding script (this script has the database creation, table creation, and table seeding scripted out already).
	Step 3: Seed the blockchain database (assuming step 1 is complete and the network is running) using the `python3 seed_blockchain.py` command. The script does not need to be altered since it is already configured for the "students" test database and "student" test table.
	Step 4: (testing the new queryByRange implementation) Execute the test scripts (note: between each of the numbered tests, steps 1-3 need to be re-executed to re-create a clean test environment):
		1) Execute the query test `./test_query.sh`
		2) Execute the insert test `./test_insert.sh`
		3) Execute the update test `./test_update.sh`
		4) Execute the update test `./test_update.sh`
	Step 5: (testing the original TDRB implementation) modify main.py by commenting out line 275 and uncommenting line 264. Specifically, line 275 should change from `rerc_tamper_flag, rerc_tampered_primary_keys = td.rerc_new(row_encryption_recs, table_name, key, iv)` to `rerc_tamper_flag, rerc_tampered_primary_keys` and execute the test scripts (note: between each of the numbered tests, steps 1-3 need to be re-executed to re-create a clean test environment):
		1) Execute the query test `./test_query_original_method.sh`
		2) Execute the insert test `./test_insert_original_method.sh`
		3) Execute the update test `./test_update_original_method.sh`
		4) Execute the update test `./test_update_original_method.sh`

Research Question 2:


Other Details:
- Libraries I used (all of them are built into python and do not have to be installed with `pip`): 
  - `argparse`: A library that makes it easy for processing input from a user to a Python program. I used the argparse library to parse input from the user and have a much cleaner way for specifying parameters by name for the bash script (`run.sh`) executed by the user.
  - `Cryptodome` - A library for AES encryption/decryption functions. Some attributes of the column encryption records and row encryption records are encrypted using AES.
  - `hashlib` - A library for hashing values. Some attributes of the column encryption records and row encryption records are hashed.
  - `base64` - a module for encoding ASCII characters into base 64 format.
  - `os` - a default Python library for interacting with the operating system
  - `pandas` - A library for converting a data source such as a SQL database, CSV file, Excel file, etc. to a table that can be operated on in Python.
  - `subprocess` - A library for calling other processing in the operating system such as scripts in other programming languages and parallel tasks. 
 
