import os
from eth_account import Account
from web3 import Web3
import hashlib
import hmac

# problem vanity address
def generate_vanity_address_ethereum(prefix):
    counter = 0
    
    # Generate a random private key
    seed_key = os.urandom(32)
    
    while counter < 2000000:
        # Deterministically expand this to another private key out of 2 million possibilities
        counter_bytes = counter.to_bytes(4, byteorder='big')
        h = hmac.new(seed_key, counter_bytes, hashlib.sha256)
        
        # Take the first 32 bytes as the private key
        private_key = h.digest()[:32]
        
        # Create an account with the private_key
        account = Account.from_key(private_key)
        
        # Get the address in hexadecimal format
        address_hex = account.address
        
        # Check if the address starts with the desired prefix
        if address_hex[2:].startswith(prefix):
            return private_key, address_hex
        
        counter += 1
    
vanity_prefix_ethereum = "0000"  # replace with your desired prefix
private_key_ethereum, address_ethereum = generate_vanity_address_ethereum(vanity_prefix_ethereum)

print("Private key: ", private_key_ethereum.hex())
print("Vanity address: ", address_ethereum)