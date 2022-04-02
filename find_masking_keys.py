"""
find_masking_keys.py
ElGamal: find possible masking keys (RSA)
"""
import sys

def sq_mul(x, H, n):
    # x = base
    r = x

    # H = exponent
    H = bin(H)[2:]
    
    # n = modulus

    # algorithm
    for i in range (1, len(H)):
        r = (r*r) % n       # square
        if H[i] == '1':
            r = (r * x) % n # multiply

    # answer :)
    return r

def main():

    if not (len(sys.argv) == 3):
        print("Usage: ./find_masking_keys.py <beta> <prime>")
        exit(0)
    
    b = int(sys.argv[1])
    p = int(sys.argv[2])

    K_m = []

    # find K_m values
    for i in range(2, p-1): # xetween 2 and p-2
        Km = sq_mul(b, i, p)
        K_m.append(Km)
        
    for k in K_m:
        print(str(k))


main()