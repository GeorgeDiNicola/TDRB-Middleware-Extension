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
	- `()` - 
	- `()` -
- `ColumnEncryptionRecord.py` 
- `RowEncryptionRecord.py` 
- `blockchain.py` 
  - `query_blockchain()` -
  - `create_blockchain_record()` -
  - `update_blockchain_record()` -
  - `update_blockchain_record()` -
- `config.py` 
  - `update_blockchain_record()` -
- `seed_blockchain.py` 
- `setup.py` 
  - `convert_table_to_column_encryption_record()` - 
  - `convert_table_to_column_encryption_record()` -
- `sql.py` 
- `tamper_detection.py` 
  - `cerc()` - 
  - `rerc()` - 
  - `rerc_new()` - 
- `utils.py`
	- `get_column_hash()` -
	- `get_column_hash_pks_only()` - 
  - `SHA_256_conversion()` - 
  - `get_encrypted_table()` - 
  - `get_table_name_hash()` - 
  - `get_item_id_hash()` -
  - `get_item_hash_pk_present()` - 
  - `get_encrypted_item_id()` -  
  - `encode_items()` -
  - `get_all_database_tables()` -

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
  
  
   


