import hashlib

if __name__ == '__main__':

	m = hashlib.sha256()

	m.update(b"hello")

	print(m.hexdigest())

	print(m.digest_size)
	print(m.block_size)