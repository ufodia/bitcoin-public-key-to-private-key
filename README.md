# Bitcoin Public Key to Private Key Converter

## Description
This Python script is a part of the `bitcoin-public-key-to-private-key` repository. It is designed to perform cryptographic operations on Bitcoin ECDSA public keys. Specifically, it subtracts the generator point `G` from a given public key multiple times. This tool finds the private key in decimal format. You can then convert this decimal private key to its hexadecimal format using any decimal-to-hex converter. This script is intended primarily for educational and research purposes in the fields of cryptography and blockchain technology.

## Installation

### Prerequisites
- Python 3
- `ecdsa` Python package

### Setup
  1. Clone the repository:
     ```bash
     git clone https://github.com/ufodia/bitcoin-public-key-to-private-key
     
  2. Navigate to the cloned repository:
  
     ```bash
     cd bitcoin-public-key-to-private-key
     
  3. Install required packages:
   
      ```bash
      pip install ecdsa



### Setup
    Run the script with the following arguments:
    
      -pb or --pubkey: Your public key in hexadecimal format.
      
      -b or --bit: The bit range for the operation.
  
   #### Example:
    
      
      
      python pubtoprivate.py -b 15 -pb 04fea58ffcf49566f6e9e9350cf5bca2861312f422966e8db16094beb14dc3df2cc71136e9f21ec86870c3a999f045d712f848c6fd6ed9582521c3f7444c8f182e


### Donate BTC: 1DDus3a5DnugwXkWdVMSYcH1tZ2jMYXfi1

### Disclaimer
This tool is provided for educational and research purposes only. The author is not responsible for any misuse or illegal activities associated with this script. Users are advised to ensure compliance with all local laws and regulations related to cryptographic operations and digital signatures.














