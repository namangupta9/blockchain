# Naman Gupta
# transaction.py
# namangupta9@gmail.com | namang@umich.edu

import time
import main

class Transaction():
    """"Representation of a Some Arbitrary Transaction"""

    # Constructor
    def __init__(self, timestamp_in, value_in, size_in):
        self.timestamp = timestamp_in
        self.value = value_in
        self.size = size_in

    # For Clean Output
    def __str__(self):
        print "Transaction Timestamp: " + self.timestamp + "\n"
        print "Transaction Value: " + self.value + "\n"
        print "Transaction Size: " + self.size + "\n"

    def get_priority(self):
        return (self.value * (time.time() - self.timestamp)) / self.size

    # Transactions Must Be Verified By Respective Nodes Before Addition to Transaction Pool
    # Simple Verification Function Here
    def validate(self):

        # Verify Size
        if (self.size > main.MAX_BLOCK_SIZE):
            return False

        return True