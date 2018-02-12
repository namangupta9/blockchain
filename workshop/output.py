# Naman Gupta
# output.py
# namangupta9@gmail.com | namang@umich.edu

import transaction
import heapq


def print_transactors():
    print("Transactors: Alpha, Bravo, Charlie, & Delta")
    print("All Transactors Begin with 100 Units of Currency\n")


def print_blockchain(blockchain_in):
    print("Blockchain Height: " + str(blockchain_in[-1].block_height))
    print("-----------------------------------------")

    if len(blockchain_in) > 0:
        print(blockchain_in[-1])

        if len(blockchain_in) > 1:
            print(blockchain_in[-2])

            if len(blockchain_in) > 2:
                print(blockchain_in[-3])


def print_transaction_pool(transactions_in, transactors_in):
    print("Transaction Pool: ")
    print("-----------------")

    index = 0
    for t in heapq.nsmallest(6, transactions_in):
        print("Priority " + str(index) + ": " + transaction.transaction_str(t[-1]))
        index += 1

    print("\n")


def print_final(transactors_in):
    # Final Outputs
    print("\nTransactors' Final Blockchain:")
    print_blockchain(transactors_in[0].blockchain)

    print("\nAlpha's Final Unspent Transaction Output (UTXO's) Pool")
    print_utxo_pool(transactors_in[0].utxo_pool)

    print("\nBravo's Final Unspent Transaction Outputs (UTXO's) Pool")
    print_utxo_pool(transactors_in[1].utxo_pool)

    print("\nCharlie's Final Unspent Transaction Outputs (UTXO's) Pool")
    print_utxo_pool(transactors_in[2].utxo_pool)

    print("\nDelta's Final Unspent Transaction Outputs (UTXO's) Pool")
    print_utxo_pool(transactors_in[3].utxo_pool)


def print_utxo_pool(utxo_pool_in):
    print("---------------------------------------------------------")

    sum = 0
    for u in utxo_pool_in:
        print(str(u))
        sum += u.value

    print("UTXO Balance: " + str(sum) + '\n')
