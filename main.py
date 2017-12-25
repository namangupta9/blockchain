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
    transaction.create_illustrative_transactions(transaction_pool, transactors)
    output.print_transaction_pool(transaction_pool, transactors) #todo

    # Create Miner Object & Mine Blocks Until No Transactions Left
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
        for t in transactors:
            miner.create_block(t.blockchain, block_transactions)


    # Final Outputs
    print "\nAlpha's Final Blockchain:"
    output.print_blockchain(transactors[0].blockchain)

    print "\nAlpha's Final Unspent Transaction Outputs (UTXO's):"
    output.print_utxo_pool(transactors[0].utxo_pool)

    print "\nBravo's Final Blockchain:"
    output.print_blockchain(transactors[1].blockchain)

    print "\nBravo's Final Unspent Transaction Outputs (UTXO's):"
    output.print_utxo_pool(transactors[1].utxo_pool)

    print "\nCharlie's Final Blockchain:"
    output.print_blockchain(transactors[2].blockchain)

    print "\nCharlie's Final Unspent Transaction Outputs (UTXO's):"
    output.print_utxo_pool(transactors[2].utxo_pool)

    print "\nDelta's Final Blockchain:"
    output.print_blockchain(transactors[3].blockchain)

    print "\nDelta's Final Unspent Transaction Outputs (UTXO's):"
    output.print_utxo_pool(transactors[3].utxo_pool)

# EXECUTION
main(300)