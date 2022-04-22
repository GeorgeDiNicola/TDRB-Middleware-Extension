from subprocess import check_output, call

# the below are for Row Encryption Records
def query_blockchain(queryId):
	
	blockchain_result = ""
	try:
		blockchain_result = check_output(['node', 'query.js', queryId.encode()])
	except:
		print("ERROR: blockchain query failed")
	
	if "Failed to evaluate transaction" in blockchain_result:
		print("ERROR: key not found")

	return blockchain_result


def create_blockchain_record(item_id_hash, item_id_AES, item_hash, owned_table_AES):

	blockchain_result = ""

	#item_id_AES = str(item_id_AES)

	try:
		blockchain_result = call(['node', 'invoke.js', item_id_hash, item_id_AES, item_hash, owned_table_AES])
	except:
		print("ERROR: blockchain create failed")
		print(blockchain_result)
		return False

	return True

def update_blockchain_record(item_id_hash, new_item_hash):

	blockchain_result = ""
	try:
		blockchain_result = call(['node', 'update.js', item_id_hash, new_item_hash])
	except:
		print("ERROR: blockchain update failed")

	if "Failed to evaluate transaction" in blockchain_result:
		print("ERROR: blockchain query failed")

	return blockchain_result


def delete_blockchain_record(item_id_hash):

	blockchain_result = ""
	try:
		blockchain_result = call(['node', 'delete.js', item_id_hash])
	except:
		print("ERROR: blockchain update failed")

	return blockchain_result
