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
        """Construct a Transactor instance."""
        self.name = name_in

        # Generate Key Pair (Public, Private)
        # TODO

        # All Start w/ Empty Local Copy of Blockchain
        # TODO

        # Unspent Transaction Outputs (UXTO's); Starts w/ Initial Value In
        # Will make sense when after we implement transactions.py
        self.utxo_pool = [transaction.UTXO(None, None, initial_value_in)]

    # Transaction Verification Methods
    def sign_utxo(self, recipient_in, utxo_in):

        # From Satoshi's White Paper:
        # - Each owner transfers the coin to the next by digitally signing
        #   a hash of the previous transaction and the public key of the next owner

        to_sign = hashlib.sha256(str(utxo_in.transaction_hash.hexdigest()) + str(recipient_in.public_key))
        utxo_in.signature = self.key.sign(str(to_sign.hexdigest()), '')

    def verify_utxo(self, sender_in, utxo_in):

        # From Satoshi's White Paper:
        # - A payee can verify the signatures to verify the chain of ownership.

        to_verify = hashlib.sha256(str(utxo_in.transaction_hash.hexdigest()) + str(self.public_key))
        return sender_in.public_key.verify(str(to_verify.hexdigest()), utxo_in.signature)
