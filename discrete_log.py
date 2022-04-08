"""
discrete_log.py
Solves discrete log problems
"""

import sys

def sq_mul(base, exp, modulus):
    # x = base
    x = int(base)
    r = int(x)

    # H = exponent
    H = bin(int(exp))[2:]
    
    # modulus
    n = int(modulus)

    # algorithm
    for i in range (1, len(H)):
        r = (r*r) % n       # square
        if H[i] == '1':
            r = (r * x) % n # multiply

    # answer :)
    return r

def main():
    # check arguments
    if not (len(sys.argv) == 4):
        print("Usage: ./sq_mul.py <base> <r> <n>")
        exit(0)

    base = int(sys.argv[1])
    r = int(sys.argv[2])
    n = int(sys.argv[3])

    for i in range(1, n-1):
        x = sq_mul(base, i, n)
        if x == r:
            print("x = " + str(i))
            exit(0)
            
    # print if there is no value of x that satisfies the equation
    print("Not defined")


main()