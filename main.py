# Naman Gupta
# main.py
# namangupta9@gmail.com | namang@umich.edu

import block
import transaction
import mine
import output
import heapq


def main(max_block_size):

    # Add Genesis Block to Empty Blockchain
    blockchain = []
    blockchain.append(block.GenesisBlock())

    # Transaction Pool is a Max-Heap (Priority Queue); Highest Value Transactions Get Mined First!
    transaction_pool = []
    transaction.create_pseudo_transactions(transaction_pool)

    # Initial Output (Before Block Mining)
    output.print_initial_blockchain(blockchain)
    output.print_transaction_pool(transaction_pool)

    # Create Miner Object & Mine Until No Transactions Left
    miner = mine.Miner()
    while len(transaction_pool) != 0:

        # Initialize Transactions for Block
        block_transactions = []
        block_size = 0

        # Add Transactions to Block Until Capacity Reached or No More Left
        while (len(transaction_pool) != 0) and (transaction_pool[0][-1].size + block_size <= max_block_size):
            block_transactions.append(heapq.heappop(transaction_pool)[-1])
            block_size += block_transactions[-1].size

        # Create Block, Add to Chain
        miner.create_block(blockchain, block_transactions)

    print "\nFinal Blockchain:"
    output.print_blockchain(blockchain)


# EXECUTION
main(300)

