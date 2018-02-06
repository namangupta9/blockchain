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
        # TODO
        self.hash = hashlib.sha256(str(hashlib.sha256(header_string).hexdigest()))

    # For Clean Output
    def __str__(self):
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
        self.hash = hashlib.sha256(str(hashlib.sha256("Genesis Block").hexdigest()))

    # For Clean Output
    def __str__(self):
        """Print properly."""
        output = ""
        output += "Block Timestamp: Genesis\n"
        output += "Block Hash: " + str(self.hash.hexdigest()) + "\n"
        output += "Block Previous Hash: N/A\n"
        return output
