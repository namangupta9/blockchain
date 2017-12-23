# Naman Gupta
# mine.py
# namangupta9@gmail.com | namang@umich.edu

import time
import block


class Miner:
    """"Implementation of a Miner"""

    # Constructor
    def __init__(self):
        self.balance = 0

    # For Clean Output
    def __str__(self):
        return "Miner's Accumulated Rewards: " + str(self.balance)

    # Miners Listen for Transactions, and Then Create Block Objects
    def create_block(self, blockchain_in, transactions_in):

        # Miner Reward For Block Creation - Fixed at .01
        self.balance += 1

        # Create New Block & Add to Blockchain
        new_block = block.Block(blockchain_in, time.time(), transactions_in)

        # Output Information about Creation

        output = "New Block Created, Containing Transactions:\n"

        output += "Miner Rewarded 1 Unit of Currency\n"
        for t in transactions_in:
            output += str(t)
            output += "\n"


        print output
        blockchain_in.append(new_block)