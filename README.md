# Simple Blockchain

*A simple implementation, for personal educational purposes.*

## Departures from Reality (Or, Room for Improvement)
Normally, a merkle root is included in the block, for purposes of verifying the validity of block transactions
- A merkle tree would be created using the hashes of all the transactions in the block

Only one miner, so there's no real need for a proof-of-work competition here
- Simple, illustrative proof-of-work competition here is based on a random number generator that's just looking to get the number "7" to create the block

## Sample Output
See Project Wiki

## Resources:
##### Blockchain Fundamentals: https://www.youtube.com/watch?v=bBC-nXj3Ng4
##### Asymmetric Encryption & Digital Signatures: https://www.youtube.com/watch?v=Us_Og3JeXiI
##### Transaction Structure: http://chimera.labs.oreilly.com/books/1234000001802/ch05.html
##### Blockchain Structure: http://chimera.labs.oreilly.com/books/1234000001802/ch07.html
##### Mining & Decentralized Consensus: http://chimera.labs.oreilly.com/books/1234000001802/ch08.html
##### Coding Tips: https://bigishdata.com/2017/10/17/write-your-own-blockchain-part-1-creating-storing-syncing-displaying-mining-and-proving-work/
