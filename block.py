# Naman Gupta
# main.py
# namangupta9@gmail.com | namang@umich.edu

import hashlib

class Block():
    """"Implementation of a Block Object"""

    # Constructor
    def __init__(self, blockchain_in, timestamp_in, transactions_in):

        # Block Height & Transactions
        self.block_height = blockchain_in[-1].block_height + 1    #Basically, The Index in Our Blockchain
        self.transactions = transactions_in
        self.transaction_counter = len(transactions_in)

        # Block Header
        self.previous_hash = blockchain_in[-1].hash
        self.merkle_root = None                                   #Merkle Root: Root of Merkle Tree of All Transactions' Hashes
        self.timestamp = timestamp_in
        self.difficulty_target = 7
        self.nonce = None

        # Block's Hash: Made by Hashing Block Header 2x Through Cryptographic Hash Function
        # TODO
        self.hash = hashlib.sha256(self.previous_hash).hexdigest()

    # For Clean Output
    def __str__(self):
        print "Block Height: " + self.index + "\n"
        print "Block Timestamp: " + self.timestamp + "\n"
        print "Block Hash: " + self.hash + "\n"
        print "Block Previous Hash: " + self.previous_hash + "\n"
        print "Block Data: " + self.data + "\n"

    # Recursively Calculate Merkle Root of Transactions_in
    # TODO
    def get_merkle_root(self, transactions_in):
        return None

# Genesis Block: Initial Block in Chain
def create_genesis_block():
    genesis_block = Block(0, 0, [])
    return genesis_block