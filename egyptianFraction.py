import math
def egyptianFraction(nr, dr):
    if dr % nr == 0:
        print(int(dr // nr))
        return
    x = math.ceil(float(dr)/ nr)
    print (int(x))
    egyptianFraction(nr * x - dr, dr * x)


egyptianFraction(6, 14)


