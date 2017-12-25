# Naman Gupta
# transactor.py
# namangupta9@gmail.com | namang@umich.edu

from Crypto.PublicKey import RSA
from Crypto import Random
import transaction


class Transactor:
    """"Implementation of a Block Chain Transactor"""

    def __init__(self, name_in, initial_value_in):
        self.name = None

        # Generate Key Pair (Public, Private)
        random_generator = Random.new().read
        self.key = RSA.generate(1024, random_generator)     # Generates Both Public & Private
        self.public_key = self.key.publickey()              # For External Access

        # All Start w/ Empty Local Copy of Blockchain
        self.blockchain = []

        # Unspent Transaction Outputs (UXTO's); Starts w/ Initial Value In
        self.utxo_pool = [transaction.UTXO(initial_value_in)]