# Naman Gupta
# main.py
# namangupta9@gmail.com | namang@umich.edu

import transactor
import block
import transaction
import mine
import output
import heapq


def main(max_block_size):

    # Define Transactors ("Nodes")
    # Let's Say Each Transactor Buys In w/ 100 Units of Currency ("Coinbase Transaction")
    alpha = transactor.Transactor("alpha", 100)
    bravo = transactor.Transactor("bravo", 100)
    charlie = transactor.Transactor("charlie", 100)
    delta = transactor.Transactor("delta", 100)
    transactors = [alpha, bravo, charlie, delta]

    # Add Genesis Block
    for t in transactors:
        t.blockchain.append(block.GenesisBlock())

    # Transaction Pool is a Max-Heap (Priority Queue); Highest Value Transactions Get Mined First!
    transaction_pool = []

    # Executes A Few Transactions; All Pushed to Un-Mined Transaction Pool
    transaction.create_illustrative_transactions(transaction_pool, transactors)
    output.print_transaction_pool(transaction_pool, transactors)

    # Create Miner Object & Mine Blocks Until No Transactions Left
    miner = mine.Miner()
    while len(transaction_pool) != 0:

        # Initialize Container for Block Transactions
        block_transactions = []
        block_size = 0

        # Add Transactions to Block Until Arbitrary Capacity Reached or No More Left
        while (len(transaction_pool) != 0) and (transaction_pool[0][-1].size + block_size <= max_block_size):
            block_transactions.append(heapq.heappop(transaction_pool)[-1])
            block_size += block_transactions[-1].size

        # Create Block, Add to Chain
        for t in transactors:
            miner.create_block(t.blockchain, block_transactions)

    # ...And We're Done
    output.print_final(transactors)


# EXECUTION
main(300)