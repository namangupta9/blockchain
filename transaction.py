# Naman Gupta
# transaction.py
# namangupta9@gmail.com | namang@umich.edu

import time
import random
import heapq


class Transaction:
    """"Representation of a Some Arbitrary Transaction"""

    # Constructor
    def __init__(self, timestamp_in, value_in, size_in):
        self.timestamp = timestamp_in
        self.value = value_in
        self.size = size_in

    # For Clean Output
    def __str__(self):
        output = "TS: " + str(self.timestamp) + " |"
        output += " Size: " + str(self.size) + " Bytes" + " |"
        output += " Val: " + str(self.value)
        return output

    def get_priority(self):
        return (self.value * (time.time() - self.timestamp)) / self.size



def create_pseudo_transactions(transaction_pool_in):

    # Create 10 Transactions, All of Size 100 Bytes
    # Transactions Have Pseudo-Random Value & Timestamp (< Current Time)
    for value in range(10):
        random_timestamp = time.time() - random.randrange(20000, 50000)
        random_value = (value + 1) * random.randrange(50, 90)
        trans = Transaction(random_timestamp, random_value, 100)

        # Priority Must be Negative for Proper Max-Heap Behavior
        trans_priority = trans.get_priority() * -1
        heapq.heappush(transaction_pool_in, (trans_priority, trans))
