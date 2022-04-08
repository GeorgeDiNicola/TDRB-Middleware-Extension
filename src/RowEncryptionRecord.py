
class RowEncryptionRecord():

	def __init__(self):
		self.itemID_hash = None
		self.itemID_AES = None
		self.item_hash = None
		self.owned_table = None
	
	"""
	def __init__(self, itemID_hash, itemID_AES, item_hash, owned_table):
		self.itemID_hash = itemID_hash
		self.itemID_AES = itemID_AES
		self.item_hash = item_hash
		self.owned_table = owned_table
	"""

	def convert_to_json_kv():
		pass