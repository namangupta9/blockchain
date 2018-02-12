# Naman Gupta
# block.py
# namangupta9@gmail.com | namang@umich.edu

import hashlib


class Block:
    """"Implementation of a Block Object"""

    # Constructor
    def __init__(self, blockchain_in, timestamp_in, transactions_in):
        """Constructing base block instance."""
        # Block Height & Transactions
        # TODO

        # Block Header
        # TODO

        # Block's Hash: Made by Hashing Block Header 2x Through Cryptographic Hash Function
        header_string = str(self.previous_hash).encode('utf-8') + str(self.timestamp).encode('utf-8')
        self.hash = hashlib.sha256(str(hashlib.sha256(header_string).hexdigest()).encode('utf-8'))

    # For Clean Output
    def __str__(self):
        """Print properly."""
        output = "Block Height: " + str(self.block_height) + "\n"
        output += "Block Timestamp: " + str(self.timestamp) + "\n"
        output += "Block Hash: " + str(self.hash.hexdigest()) + "\n"
        output += "Block Previous Hash: " + str(self.previous_hash.hexdigest()) + "\n"
        return output


class GenesisBlock():
    """"Implementation of a Genesis Block"""

    def __init__(self):
        """Constructing base genesis block instance."""
        # Block Height & Transactions
        # TODO

        # Block Header
        # TODO

        # Block's Hash: Made by Hashing Block Header 2x Through Cryptographic Hash Function
        hash_text = "Genesis Block".encode('utf-8')
        self.hash = hashlib.sha256(str(hashlib.sha256(hash_text).hexdigest()).encode('utf-8'))

    # For Clean Output
    def __str__(self):
        """Print properly."""
        output = ""
        output += "Block Timestamp: Genesis\n"
        output += "Block Hash: " + str(self.hash.hexdigest()) + "\n"
        output += "Block Previous Hash: N/A\n"
        return output
