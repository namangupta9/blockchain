# Naman Gupta
# block.py
# namangupta9@gmail.com | namang@umich.edu

import hashlib


class Block:
    """"Implementation of a Block Object"""

    # Constructor
    def __init__(self, blockchain_in, timestamp_in, transactions_in):

        # Block Height & Transactions
        self.block_height = blockchain_in[-1].block_height + 1    #Basically, The Index in Our Blockchain
        self.transactions = transactions_in
        self.transaction_counter = len(transactions_in)

        # Block Header
        self.previous_hash = blockchain_in[-1].hash
        self.timestamp = timestamp_in
        self.difficulty_target = 7
        self.nonce = None

        # Block's Hash: Made by Hashing Block Header 2x Through Cryptographic Hash Function
        self.hash = hashlib.sha256(str(hashlib.sha256(None).hexdigest()))

    # For Clean Output
    def __str__(self):
        print "Block Height: " + str(self.block_height) + "\n"
        print "Block Timestamp: " + str(self.timestamp) + "\n"
        print "Block Hash: " + str(self.hash) + "\n"
        print "Block Previous Hash: " + str(self.previous_hash) + "\n"



# Inherited Subclass for Genesis Block
class GenesisBlock(Block):

    def __init__(self):
        # Block Height & Transactions
        self.block_height = 0
        self.transactions = []
        self.transaction_counter = 0

        # Block Header
        self.previous_hash = None
        self.merkle_root = None
        self.timestamp = None
        self.difficulty_target = None
        self.nonce = None

        # Block's Hash: Made by Hashing Block Header 2x Through Cryptographic Hash Function
        self.hash = hashlib.sha256(str(hashlib.sha256("Genesis Block").hexdigest()))

    # For Clean Output
    def __str__(self):
        output = ""
        output += "Block Height: " + str(self.block_height) + "\n"
        output += "Block Timestamp: Genesis\n"
        output += "Block Hash: " + str(self.hash.hexdigest()) + "\n"
        output += "Block Previous Hash: N/A\n"
        return output
