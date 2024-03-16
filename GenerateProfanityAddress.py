

from ecpy.curves import Curve
from ecpy.keys import ECPublicKey, ECPrivateKey
from sha3 import keccak_256
from datetime import datetime
import random

def generateEthereumAddress(private_key):
    cv = Curve.get_curve('secp256k1')
    pv_key = ECPrivateKey(int(private_key, 16), cv)
    pu_key = pv_key.get_public_key()

    concat_x_y = pu_key.W.x.to_bytes(32, byteorder='big') + pu_key.W.y.to_bytes(32, byteorder='big')
    eth_addr = '0x' + keccak_256(concat_x_y).digest()[-20:].hex()
    return eth_addr
   


if __name__ == "__main__":
    #  get current time  
    beforeTime =  datetime.now();       
    private_key = '0x' + random.randbytes(32).hex()
    # print("private_key", private_key)
    # private_key = 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
    eth_addr = generateEthereumAddress(private_key)
    while eth_addr[2:6] != "0000":
        private_key = '0x' + random.randbytes(32).hex()
        # print("private_key", private_key)
        eth_addr = generateEthereumAddress(private_key)

    endTime =  datetime.now();
    total_seconds = (endTime - beforeTime).total_seconds()
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    endTime =  datetime.now();
    print(f"Consume {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds.")
    print("private_key", private_key, "eth_addr", eth_addr)
