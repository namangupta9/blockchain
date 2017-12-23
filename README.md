# Simple Blockchain

*Didn't understand blockchain, so I decided to build a simple one.*

## Departures from Reality
Transactions normally have parties, who must verify transactions before they're added to the transaction pool
- In this case, pseudo-transactions are generated randomly, without any associated parties
- Hence, this simple implementation isn't truly "decentralized"; there are no nodes to keep local copies

Normally, a merkle root is included in the block, for purposes of verifying the validity of block transactions
- A merkle tree would be created using the hashes of all the transactions in the block

Only one miner, so there's no real need for a proof-of-work competition here
- Simple, illustrative proof-of-work competition here is based on a random number generator that's just looking to get the number "7" to create the block

## Sample Output

## Resources:
##### https://www.youtube.com/watch?v=bBC-nXj3Ng4
##### http://chimera.labs.oreilly.com/books/1234000001802/ch07.html#_introduction_2
##### https://bigishdata.com/2017/10/17/write-your-own-blockchain-part-1-creating-storing-syncing-displaying-mining-and-proving-work/
