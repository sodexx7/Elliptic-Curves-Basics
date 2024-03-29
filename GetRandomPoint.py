# import random
import random
from math import pow
from math import sqrt
Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 # The proven prime


# y^2 = x^3 + 7
# below just statisfy above math formula, not the condsider the prime number
def get_random_point():
    x_int = random.randint(0,Pcurve-1)
    y_int = int(sqrt(pow(x_int, 3) + 7))

    while pow(y_int,2) != pow(x_int, 3) + 7:
        x_int = random.randint(0,Pcurve-1)
        y_int = int(sqrt(pow(x_int, 3) + 7))

    return (x_int,y_int)

if __name__ == "__main__":
    print(get_random_point());



