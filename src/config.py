import os

config = {
	"aes_key": os.getenv("TDRB_KEY")
}

def load_config():
	return config