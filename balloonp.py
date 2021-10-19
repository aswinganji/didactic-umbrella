import hashlib
import json 
from time import time

chain = []

def block(proof,previous_hash=None):
	transaction = {
	'sender' : 'Santoshi',
	'recepient' : 'Mike',
	'amount' : '500000 ETH'
	}

	data = {
	'index' : 1,
	'timestamps' : time(),
	'gas/fee' : 0.1,
	'proof' : proof,
	'previous_hash' : previous_hash,
	'uncle rewards' : '10000 ETH', 
	'block rewards' : '41000 ETH',
	'difficulty' : '9,999,999,999',
	'total difficulty' : '9,999,999,999,999,999,999,999'

	}

	chain.append(block)
	print("block information",data)
	string_object = json.dumps(data)
	block_string = string_object.encode()

	raw_hash = hashlib.sha512(block_string)
	hex_hash = raw_hash.hexdigest()

	print("CODING HASH ERROR CODING HASH ERROR")

block(previous_hash = "BLAHBLAHBLAHBLAHBLAH FIRST HASH BLAHBLAHBLAHBLAHBLAH",proof=000)
