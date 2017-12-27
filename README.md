# Simple Blockchain

*A basic implementation of a blockchain data structure for personal education, designed to illustrate the fundamentals of related concepts including decentralization, cryptographic hashing, transaction linking, digital signatures, and block mining.*

## Departures from Reality (Or, Room for Improvement)
Normally, a merkle root is included in the block, for purposes of saving memory space and verifying the validity of block transactions (Satoshi's White Paper)
- A merkle tree would be created recursively using the hashes of all the transactions in the block
- Not included in this implementation given the small size of the transaction set

Used the simple transaction verification protocol outlined in Chapter 2 of Satoshi's White Paper instead
- Some applications, like Bitcoin, use more complex locking & unlocking scripts

Only one miner, so there's no real need for a proof-of-work competition here

## Sample Output
See Project Wiki

## Resources:
##### Satoshi's White Paper:
https://bitcoin.org/bitcoin.pdf
##### Blockchain Fundamentals:
*https://www.youtube.com/watch?v=bBC-nXj3Ng4*
##### Asymmetric Encryption & Digital Signatures:
*https://www.youtube.com/watch?v=Us_Og3JeXiI*
##### Transaction Structure:
*http://chimera.labs.oreilly.com/books/1234000001802/ch05.html*
##### Blockchain Structure:
*http://chimera.labs.oreilly.com/books/1234000001802/ch07.html*
##### Mining & Decentralized Consensus:
*http://chimera.labs.oreilly.com/books/1234000001802/ch08.html*
##### Coding Tips:
*https://bigishdata.com/2017/10/17/write-your-own-blockchain-part-1-creating-storing-syncing-displaying-mining-and-proving-work/*
