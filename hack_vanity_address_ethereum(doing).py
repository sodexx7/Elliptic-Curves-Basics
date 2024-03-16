from eth_account import Account
from eth_keys import keys
import random

# Step 1: Get a public key for a vanity address
# This is a placeholder. Replace it with the actual private key for the vanity address
vanity_private_key_hex = "edb474fa77dd6ac49b41fdae5e24691c6054dd9938b9d4bbc091a28012396f49"

# Convert the private key from hexadecimal to bytes
vanity_private_key_bytes = bytes.fromhex(vanity_private_key_hex)

# Create a PrivateKey object
vanity_private_key = keys.PrivateKey(vanity_private_key_bytes)

# Derive the public key from the private key
vanity_public_key = vanity_private_key.public_key

# Print the public key in hexadecimal format
print(vanity_public_key.to_hex())

# Convert the private key to an integer
vanity_private_key_int = int(vanity_private_key_hex, 16)

# Step 2: Expand it deterministically to 1 in 2 million possibilities
for counter in range(2000000):
    # Generate a new private key based on the counter
    new_private_key_int = (vanity_private_key_int + counter) % (2**256)
    new_private_key = keys.PrivateKey(new_private_key_int.to_bytes(32, byteorder='big'))

    # Generate a new Ethereum public key from the private key
    new_public_key = new_private_key.public_key

    # Here you can use the new_public_key for whatever you need
    print(f"Generated public key: {new_public_key}")

# Step 3: Decrement that key until it reaches the seed private key
while new_private_key != vanity_private_key:
    new_private_key_int = (new_private_key_int - 1) % (2**256)
    new_private_key = keys.PrivateKey(new_private_key_int.to_bytes(32, byteorder='big'))

    # Generate a new Ethereum public key from the private key
    new_public_key = new_private_key.public_key

    # Here you can use the new_public_key for whatever you need
    print(f"Generated public key: {new_public_key}")




# todo
#     Here is the process taken by their script:

# 1. Get a public key for a vanity address.

# 2. Expand it deterministically to 1 in 2 million possibilities.

# 3. Decrement that key until it reaches the seed public key (the 32-bit vector)

# Now you have the seed for the private key associated with the public key for the vanity address.

# The Profanity GitHub repo is still up. Please don’t use it.