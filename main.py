# Naman Gupta
# main.py
# namangupta9@gmail.com | namang@umich.edu

import block
import transaction
import mine
import output


def main():

    MAX_BLOCK_SIZE = 300

    # Add Genesis Block to Empty Blockchain
    blockchain = list
    blockchain.append(block.GenesisBlock())

    # Transaction Pool is a Max-Heap (Priority Queue); Highest Value Transactions Get Mined First!
    transaction_pool = []
    transaction.create_pseudo_transactions(transaction_pool)

    # Initial Output (Before Block Mining)
    output.print_transaction_pool(transaction_pool)
    output.print_initial_blockchain(blockchain)

    # Create Miner Object & Mine Until No Transactions Left
    miner = mine.Miner()
    while len(transaction_pool) != 0:




        break



# EXECUTION
main()

