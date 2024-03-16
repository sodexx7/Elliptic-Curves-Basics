# import random
import random
from math import pow
from math import sqrt
Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 # The proven prime

def get_random_point():
    # x = random.randbytes(32)
    x_int = random.randint(Pcurve-1000000,Pcurve-1)
    # x_int = int.from_bytes(x, "big")
    y = pow(x_int, 3) + 7
    y_sqrt = sqrt(y)


    while (pow(y_sqrt, 2) != (pow(x_int, 3) + 7) ):
        x = random.randbytes(32)
        x_int = int.from_bytes(x, "big")
        y = pow(x_int, 3) + 7
        y_sqrt = sqrt(y)
    return (x_int, format(y_sqrt, '.0f'))

if __name__ == "__main__":
    print(get_random_point());


