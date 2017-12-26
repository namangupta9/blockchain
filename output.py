# Naman Gupta
# output.py
# namangupta9@gmail.com | namang@umich.edu

import transaction


def print_initial_blockchain(blockchain_in):

    print "\nInitial Blockchain"
    print "-----------------------------------------"
    print blockchain_in[-1]
    print "\n"


def print_blockchain(blockchain_in):

    print "Blockchain Height: " + str(blockchain_in[-1].block_height)
    print "-----------------------------------------"

    if len(blockchain_in) > 0:
        print blockchain_in[-1]

        if len(blockchain_in) > 1:
            print blockchain_in[-2]

            if len(blockchain_in) > 2:
                print blockchain_in[-3]


def print_transaction_pool(transactions_in, transactors_in):

    print "Transaction Pool: "
    print "-----------------"

    index = 0
    for t in transactions_in:
        print "Priority " + str(index) + ": " + transaction.transaction_str(t[-1], transactors_in)
        index += 1

    print "\n"


def print_final(transactors_in):

    # Final Outputs
    print "\nAlpha's Final Blockchain:"
    print_blockchain(transactors_in[0].blockchain)

    print "\nAlpha's Final Unspent Transaction Outputs (UTXO's):"
    print_utxo_pool(transactors_in[0].utxo_pool)

    print "\nBravo's Final Blockchain:"
    print_blockchain(transactors_in[1].blockchain)

    print "\nBravo's Final Unspent Transaction Outputs (UTXO's):"
    print_utxo_pool(transactors_in[1].utxo_pool)

    print "\nCharlie's Final Blockchain:"
    print_blockchain(transactors_in[2].blockchain)

    print "\nCharlie's Final Unspent Transaction Outputs (UTXO's):"
    print_utxo_pool(transactors_in[2].utxo_pool)

    print "\nDelta's Final Blockchain:"
    print_blockchain(transactors_in[3].blockchain)

    print "\nDelta's Final Unspent Transaction Outputs (UTXO's):"
    print_utxo_pool(transactors_in[3].utxo_pool)

#todo
def print_utxo_pool(utxo_pool_in):
    return None