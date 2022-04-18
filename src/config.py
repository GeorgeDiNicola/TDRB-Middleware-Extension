import os

config = {
	#"aes_key": os.getenv("TDRB_KEY")
	"host_name": "localhost",
	"username": "root",
	"database": "students",
	"password": "root",
	"aes_key": b'\xa8\n\xa4\x17\xef\xef\x9a\x8a\xe3\xca\x08\xd0\xb0\xc9\x90Y`\xd9B\x9b\xc9\xe0\x89\xddD \x84y0@\xbe\xcd',
	"iv": b'\x94\x92\xa3u\x183(\xe75\x19\xc1K\x06\x95\xba\x88'
}

def load_config():
	return config