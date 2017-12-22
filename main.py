# Naman Gupta
# main.py
# namangupta9@gmail.com | namang@umich.edu

import mine
import time
import block
import transaction
import transactor
import heapq

# COMMENTS
# - Not building in blockchain forks
# - Not building in any specific type of transactions, to maintain a simple, general blockchain form

# Driver Implementation
def main():

    # Add Genesis Block to Empty Blockchain
    blockchain = []
    blockchain.append(block.create_genesis_block())
    print "Initial Blockchain:"
    print_blockchain(blockchain)

    # Transaction Pool is a Max-Heap (Priority Queue); Highest Value Transactions Get Mined First!
    transaction_pool = []

    # Create 10 Transactions, All of Size 100 Bytes; Add to Transaction Pool
    for value in range(10):
        trans = transaction.Transaction(time.time(), value * 100, 100)
        trans_priority = trans.get_priority()
        heapq.heappush(transaction_pool, (trans_priority, trans))

    # Add Transactions Here, Mine in a While Loop, Pop Transactions Accordingly


    return


# Blockchain Output Function
def print_blockchain(blockchain_in):
    print "Blockchain Height: " + blockchain_in[-1].block_height + "\n"
    print "Top 3 Blocks:\n"

    if len(blockchain_in >= 1):
        print blockchain_in[-1]

    if len(blockchain_in >= 2):
        print blockchain_in[-2]

    if len(blockchain_in >= 3):
        print blockchain_in[-3]


# EXECUTION
global MAX_BLOCK_SIZE = 300
main()


