# Naman Gupta
# main.py
# namangupta9@gmail.com | namang@umich.edu

import transactor
import block
import transaction
import mine
import output


def main():
    """Execute all components of program."""
    # Define Transactors ("Nodes")
    # Let's Say Each Transactor Buys In w/ 100 Units of Currency
    alpha = transactor.Transactor("alpha", 100)
    bravo = transactor.Transactor("bravo", 100)
    charlie = transactor.Transactor("charlie", 100)
    delta = transactor.Transactor("delta", 100)
    transactors = [alpha, bravo, charlie, delta]
    output.print_transactors()

    # Add Genesis Block
    for t in transactors:
        t.blockchain.append(block.GenesisBlock())

    # Transaction Pool is a Max-Heap (Priority Queue); Highest Value Transactions Get Mined First!
    transaction_pool = []

    # Executes A Few Transactions; All Pushed to Un-Mined Transaction Pool
    transaction.create_illustrative_transactions(transaction_pool, transactors)
    output.print_transaction_pool(transaction_pool, transactors)

    # Create Miner Object & Mine Blocks Until No Transactions Left
    # Arbitarily Saying That Max. Size of a Block is 300 Bytes Worth of Transactions
    miner = mine.Miner()
    while len(transaction_pool) != 0:
        miner.mine_blocks(transactors, transaction_pool, max_block_size=300)

    # ...And We're Done
    output.print_final(transactors)


# EXECUTION
main()
