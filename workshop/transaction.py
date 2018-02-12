# Naman Gupta
# transaction.py
# namangupta9@gmail.com | namang@umich.edu

import time
import heapq
import hashlib


class UTXO:
    """"Representation of an Unspent Transaction Output"""

    def __init__(self, transaction_hash_in, output_index_in, value_in):
        self.transaction_hash = transaction_hash_in     # Hash of Transaction Where This UTXO Came From
        self.output_index = output_index_in             # Which Output Was This, In the OG Transaction?
        self.value = value_in                           # "Amount" of the UTXO
        self.signature = None

    def __str__(self):
        output = "Previous Transaction Hash: " + str(self.transaction_hash.hexdigest()) + '\n'
        output += "Previous Transaction Output Index:" + str(self.output_index) + '\n'
        output += "Value: " + str(self.value) + '\n'
        return output


class Input:
    """Representation of a Transaction Input"""

    def __init__(self, utxo_in):
        self.transaction_hash = utxo_in.transaction_hash  # Hash of Transaction Containing UTXO
        self.output_index = utxo_in.output_index          # Which Of That Transaction's Outputs is the UTXO?
        self.value = utxo_in.value                        # How Much Is That UTXO Worth?


class Transaction:
    """"Representation of a Some Arbitrary Transaction"""
    # From Satoshi's White Paper: "We define an electronic coin as a chain of digital signatures"

    # Transaction Constructor
    def __init__(self, timestamp_in, value_in, size_in, sender_in, recipient_in):

        # Basic Transaction Data
        # TODO

        # Transaction's Unique ID (Double Hashed) ("TXID")
        self.hash = hashlib.sha256(str(hashlib.sha256(str(timestamp_in).encode('utf-8') + \
                                   str(value_in).encode('utf-8') + str(size_in).encode('utf-8')).hexdigest()).encode('utf-8'))

        # For Transaction Verification
        # TODO

        # Transaction Linkages
        # TODO

    def get_inputs(self):

        # Go To Sender, Greedily Select Transaction Inputs from Unspent Transaction Outputs Pool
        # TODO

            # Add UTXO to Transaction Inputs
            # TODO

            # Remove from UTXO Pool - Eliminates 'Double Spend' Problem
            # TODO

            # Check If We're Done Adding Transaction Inputs
            # TODO

        # TODO
        return None

    def create_outputs(self):

        # Initialize Container for Outputs
        # TODO

        # Deduct Inputs from Value
        # TODO

        # Send Value to Recipient
        # Sender Signs Transaction w/ Its Private Key (Ensures That Only The Private Key Owner Can Spend!)
        # TODO

        # Recipient Accepts Output
        # Recipient Uses Public Key of Sender to Verify The Sender's Signature (To Verify Chain of Ownership!)
        # TODO

        # (If Necessary) Return Change to Sender
        # TODO

        # TODO
        return None

    # For Implementation of Transaction Pool as a PQ (Max-Heap Based)
    def get_priority(self):
        return (self.value * (time.time() - self.timestamp)) / self.size


# For Clean Output
def transaction_str(transaction_in):
    output = "TimeStamp: " + str(transaction_in.timestamp) + " |"
    output += " Size: " + str(transaction_in.size) + " Bytes" + " |"
    output += " Val: " + str(transaction_in.value) + " |"
    output += " Sender: " + str(transaction_in.sender.name) + " |"
    output += " Recipient: " + str(transaction_in.recipient.name)
    return output


# For Purposes of This Simple Implementation, Finite Set of Simple Two-Party Transactions Created
def create_illustrative_transactions(transaction_pool_in, transactors_in):

    # Create A Few Transactions, All of 100-Byte Size
    # All Transactions Have Increasing Timestamps
    # Transaction Priorities Must be Negative for Proper Max-Heap Behavior

    # 50 Sent From Alpha to Bravo
    a = Transaction(time.time(), 50, 100, transactors_in[0], transactors_in[1])
    trans_priority = a.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, a))

    # 30 Sent From Bravo to Charlie
    b = Transaction(time.time() + 10, 30, 100, transactors_in[1], transactors_in[2])
    trans_priority = b.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, b))

    # 50 Sent From Bravo to Delta
    c = Transaction(time.time() + 20, 50, 100, transactors_in[1], transactors_in[3])
    trans_priority = c.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, c))

    # 10 Sent From Charlie to Bravo
    d = Transaction(time.time() + 30, 10, 100, transactors_in[2], transactors_in[1])
    trans_priority = d.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, d))

    # 60 Sent From Delta to Alpha
    e = Transaction(time.time() + 40, 60, 100, transactors_in[3], transactors_in[0])
    trans_priority = e.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, e))

    # 40 Sent From Alpha to Charlie
    f = Transaction(time.time() + 50, 40, 100, transactors_in[0], transactors_in[2])
    trans_priority = f.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, f))
