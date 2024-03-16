import os
from tinyec import registry
import hashlib
import hmac

# Step 1: Get a public key for a vanity address.
seed_key = os.urandom(32)
private_key = int.from_bytes(seed_key, byteorder='big') 
curve = registry.get_curve('secp256k1')

public_key = private_key * curve.g

# Step 2: Expand it deterministically to 1 in 2 million possibilities.
counter = 0
public_keys = []
while counter < 2000000:
    # create a deterministic key from seed_key and counter
    counter_bytes = counter.to_bytes(4, byteorder='big')
    h = hmac.new(seed_key, counter_bytes, hashlib.sha256)
    new_private_key = h.digest()[:32]
    public_keys.append(new_private_key * curve.g)
    counter += 1

# Step 3: Decrement that key until it reaches the seed public key (the 32-bit vector)
for decrement_value in range(len(public_keys)-1, -1, -1):
    if public_keys[decrement_value] == public_key:  # checks if the generated public key equals the initial public key
        print("Success! The index is:", decrement_value)
        break
