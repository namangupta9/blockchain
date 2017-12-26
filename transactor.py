# Naman Gupta
# transactor.py
# namangupta9@gmail.com | namang@umich.edu

from Crypto.PublicKey import RSA
from Crypto import Random
import transaction
import hashlib


class Transactor:
    """"Implementation of a Block Chain Transactor"""

    def __init__(self, name_in, initial_value_in):
        self.name = name_in

        # Generate Key Pair (Public, Private)
        random_generator = Random.new().read
        self.key = RSA.generate(1024, random_generator)     # Both Public & Private Keys
        self.public_key = self.key.publickey()              # For External Access

        # All Start w/ Empty Local Copy of Blockchain
        self.blockchain = []

        # Unspent Transaction Outputs (UXTO's); Starts w/ Initial Value In
        self.utxo_pool = [transaction.UTXO(initial_value_in)]

    # Transaction Verification Methods
    def sign_utxo(self, recipient_in, utxo_in):

        # From Satoshi's White Paper:
        # - Each owner transfers the coin to the next by digitally signing
        #   a hash of the previous transaction and the public key of the next owner

        to_sign = hashlib.sha256(str(utxo_in.transaction_hash.hexdigest()) + str(recipient_in.public_key))
        utxo_in.signature = self.key.sign(to_sign, '')

    def verify_utxo(self, sender_in, utxo_in):

        # From Satoshi's White Paper:
        # - A payee can verify the signatures to verify the chain of ownership.

        to_verify = hashlib.sha256(str(utxo_in.transaction_hash.hexdigest()) + str(self.public_key))
        return sender_in.public_key.verify(to_verify, utxo_in.signature)