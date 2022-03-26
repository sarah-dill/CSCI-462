"""
fermat_primality_test.py

"""


def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

# square and multiple algorithm
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

# check if the number is prime
def check_if_prime(n):
    print("fuck")

def find_carmichael(a, s):
    # if gcd(a, C) != 1
        # return composite

    for i in range(0, s):
        print(i)
        # choose random a in {2, 3, ... p-2}
        # if a^p-1 is not 1 mod p
            # return composite
    # return p is likely prime
    return 1


def main():
    print("fuck this shit")
    for i in range(2, 10):
        car = find_carmichael(i, 4)
        if car == 1:
            print(i)


main()