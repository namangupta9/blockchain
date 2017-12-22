# Naman Gupta
# main.py
# namangupta9@gmail.com | namang@umich.edu

import time
import block

class Miner():
    """"Implementation of a Miner"""

    # Constructor
    def __init__(self, index, timestamp):
        self.balance = 0


    # For Clean Output
    def __str__(self):

    # Miners Listen for Transactions, and Then Create Block Objects
    def create_block(self, blockchain_in, transactions_in):

        new_block = block.Block(blockchain_in, time.time(), transactions_in)

        # Miner Reward: For Block Creation - Fixed at .01
        self.balance += .01

        # Miner Reward: Variable - Based on # Transactions
        # TODO
        self.balance += .01 * new_block.transaction_counter

        return new_block