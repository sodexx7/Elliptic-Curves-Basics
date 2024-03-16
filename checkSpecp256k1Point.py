
# Given a random point n, is n a valid point on the sepc265k1 curve.

# elliptic curves
# y^2 = x^3 + ax + b (4a3 + 27b2 != 0)
    
# The secp256k1 curve is defined by the equation y^2 = x^3 + 7. where a=0, b=7.
# 1. The curve define
#   1. The field prime is 2^256 - 2^32 - 977(2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1). (115792089237316195423570985008687907853269984665640564039457584007908834671663)
#   2. The generator point G is 
#      (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
#   3. order(Number of points in the field) : 115792089237316195423570985008687907852837564279074904382605163141518161494337(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)

Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 # The proven prime
N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # Number of points in the field
Acurve = 0; Bcurve = 7 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424

import sys
from math import pow

def check_point(x, y):
    # x,y must in the field [1,p-1]? todo check
    # if(x==0 or x>Pcurve-1 and y==0 or y>Pcurve-1):
    #     return False
    return (pow(y, 2)% Pcurve == (pow(x, 3) + 7) % Pcurve)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 checkSpecp256k1Point.py [x] [y]")
        sys.exit(1)

    x = int(sys.argv[1])
    y = int(sys.argv[2])

    print(check_point(x, y))

