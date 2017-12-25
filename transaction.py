# Naman Gupta
# transaction.py
# namangupta9@gmail.com | namang@umich.edu

import time
import heapq


class UTXO:
    """"Representation of an Unspent Transaction Output"""

    def __init__(self, value_in):
        self.value = None
        self.locking_script = None


class Transaction:
    """"Representation of a Some Arbitrary Transaction"""

    class Input:
        """Representation of a Transaction Input"""

        def __init__(self, utxo_in):
            self.associated_utxo = utxo_in
            self.unlocking_script = None

    # Transaction Constructor
    def __init__(self, timestamp_in, value_in, size_in, sender_in, recipient_in):
        self.timestamp = timestamp_in
        self.value = value_in
        self.size = size_in

        # For Transaction Verification
        self.sender = sender_in
        self.recipient = recipient_in

        # Transaction Structure
        self.inputs = self.get_inputs()
        self.value_output, self.remainder_output = self.create_outputs()

    def get_inputs(self):

        # Go To Sender, Greedily Select Transaction Inputs from Unspent Transaction Outputs Pool
        inputs = []
        inputs_sum = 0
        for u in self.sender.utxo_pool:

            # Add UTXO to Transaction Inputs
            # Unlock w/ Signature of Current UTXO Owner (To Confirm They're Okay w/ This) todo
            i = self.Input(u)
            inputs.append(i)
            inputs_sum += u.value

            # Remove from UTXO Pool - Eliminates 'Double Spend' Problem
            self.sender.utxo_pool.remove(i)

            # Check If We're Done Adding Transaction Inputs
            if inputs_sum >= self.value:
                break

        return inputs

    def create_outputs(self):

        # Deduct Inputs from Value
        input_sum = 0
        for i in self.inputs:
            input_sum += i.value

        # Send Value to Recipient
        # Lock Value's UXTO to New Owner todo
        value_out = UTXO(self.value)

        # Return Change to Sender
        remainder_out = UTXO(self.value - float(input_sum))

        return value_out, remainder_out

    def get_priority(self):
        return (self.value * (time.time() - self.timestamp)) / self.size


# For Clean Output
def transaction_str(transaction_in, transactors_in):
    output = "TS: " + str(transaction_in.timestamp) + " |"
    output += " Size: " + str(transaction_in.size) + " Bytes" + " |"
    output += " Val: " + str(transaction_in.value) + " |"
    output += " Sender: " + str(transactors_in[transaction_in.sender].name) + " |"
    output += " Recipient: " + str(transactors_in[transaction_in.recipient].name)
    return output


def create_illustrative_transactions(transaction_pool_in, transactors_in):

    # Create A Few Transactions, All of 100-Byte Size
    # All Transactions Have Increasing Timestamps
    # Transaction Priorities Must be Negative for Proper Max-Heap Behavior

    # 50 Sent From Alpha to Bravo
    a = Transaction(time.time(), 50, 100, transactors_in[0], transactors_in[1])
    trans_priority = a.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, a))

    # 30 Sent From Bravo to Charlie
    b = Transaction(time.time() + 10000, 30, 100, transactors_in[1], transactors_in[2])
    trans_priority = b.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, b))

    # 50 Sent From Bravo to Delta
    c = Transaction(time.time() + 20000, 50, 100, transactors_in[1], transactors_in[3])
    trans_priority = c.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, c))

    # 10 Sent From Charlie to Bravo
    d = Transaction(time.time() + 10000, 10, 100, transactors_in[2], transactors_in[1])
    trans_priority = d.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, d))

    # 60 Sent From Delta to Alpha
    e = Transaction(time.time() + 10000, 60, 100, transactors_in[3], transactors_in[0])
    trans_priority = e.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, e))

    # 40 Sent From Alpha to Charlie
    f = Transaction(time.time() + 10000, 40, 100, transactors_in[0], transactors_in[2])
    trans_priority = f.get_priority() * -1
    heapq.heappush(transaction_pool_in, (trans_priority, f))