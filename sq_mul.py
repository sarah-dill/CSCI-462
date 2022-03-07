"""
sq_mul.py
Square and Multiply algorithm
"""

import sys

def main():

    # check arguments
    if not (len(sys.argv) == 4):
        print("Usage: ./sq_mul.py <base> <exponent> <n>")
        print(len(sys.argv))
        exit(0)
    
    # x = base
    x = int(sys.argv[1])
    r = int(x)

    # H = exponent
    H = bin(int(sys.argv[2]))[2:]
    
    # modulus
    n = int(sys.argv[3])

    # algorithm
    for i in range (1, len(H)):
        r = (r*r) % n       # square
        if H[i] == '1':
            r = (r * x) % n # multiply

    # answer :)
    print(r)

main()