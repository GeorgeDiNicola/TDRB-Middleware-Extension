"""
	Author: George DiNicola
	Description: The blockchain module serves as an API to the blockchain
		ledger. It calls Nodejs scripts that execute CRUD operations on
		the ledger and world state database (CouchDB).
"""

from subprocess import check_output, call


def query_blockchain(queryId):
	"""Query the state database using the key/ID."""
	
	blockchain_result = ""
	try:
		blockchain_result = check_output(['node', 'query.js', queryId])
	except:
		print("ERROR: blockchain query failed")
		return False

	return True


def create_blockchain_record(item_id_hash, item_id_AES, item_hash, owned_table_AES):
	""" Create a new blockchain record with the following attributes:
		1. Item ID hash value
		2. Item ID encrypted using AES
		3. The hash value of all the items in the row
		4. The name of the table encrypted using AES
	"""

	blockchain_result = ""

	try:
		blockchain_result = call(['node', 'invoke.js', item_id_hash, item_id_AES, item_hash, owned_table_AES])
	except:
		print("ERROR: blockchain create failed")
		return False

	return True

def update_blockchain_record(item_id_hash, new_item_hash):
	""" Update the item hash value of an existing record on the state database."""

	blockchain_result = ""
	try:
		blockchain_result = call(['node', 'update.js', item_id_hash, new_item_hash])
	except:
		print("ERROR: blockchain update failed")
		return False

	return True


def delete_blockchain_record(item_id_hash):
	""" Delete an existing record in the state database."""

	blockchain_result = ""
	try:
		blockchain_result = call(['node', 'delete.js', item_id_hash])
	except:
		print("ERROR: blockchain update failed")
		return False

	return True
