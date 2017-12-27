# Naman Gupta
# mine.py
# namangupta9@gmail.com | namang@umich.edu

import time
import block
import heapq
import transaction


class Miner:
    """"Implementation of a Miner"""

    # Constructor
    def __init__(self):
        self.balance = 0

    # For Clean Output
    def __str__(self):
        return "Miner's Accumulated Rewards: " + str(self.balance)

    # Package Final Set of Transactions Into Block Object
    def create_block(self, blockchain_in, transactions_in):

        # Miner Reward For Block Creation - Fixed at .01
        self.balance += 1

        # Create New Block & Add to Blockchain
        new_block = block.Block(blockchain_in, time.time(), transactions_in)
        blockchain_in.append(new_block)

    # Process of Taking Transactions From Pool into A Block
    def mine_blocks(self, transactors_in, transaction_pool_in, max_block_size):

        # Initialize Container for Block Transactions
        block_transactions = []
        block_size = 0

        # Add Transactions to Block Until Arbitrary Capacity Reached or No More Left
        while (len(transaction_pool_in) != 0) and (transaction_pool_in[0][-1].size + block_size <= max_block_size):
            block_transactions.append(heapq.heappop(transaction_pool_in)[-1])
            block_size += block_transactions[-1].size

        # Create Block, Add to Chain
        for t in transactors_in:
            self.create_block(t.blockchain, block_transactions)

        # Output Information about Creation
        out = "New Block Created, Containing Transactions:\n"
        out += "- Coinbase Transaction: Miner Rewarded 1 Unit of Currency\n"
        for t in block_transactions:
            out += "- "
            out += transaction.transaction_str(t)
            out += "\n"

        print out