"""
sq_mul_RSA.py
Square and Multiply algorithm

Inteded for use with large numbers (ex: RSA)

The only difference between this and sq_mul.py 
is that this doesn't use the command line to obtain the
argumnents (since the numbers are so large). Instead,
the numbers are hard-coded and must be changed within
the code itself.

If using smaller numbers, use sq_mul.py, since it is 
much easier to change the values.
"""

import sys

def main():
    
    # x = base
    x = 91045328916998417442482698097341808065794629308863274299915006508648723904695483923175519319873972294295937946793571148693700025
    r = x

    # H = exponent
    H = bin(106698614368578024442868771328920154780709906633937862801226224496631063125911774470873340168597462306553968544513277109053606095)[2:]
    
    # modulus
    n = 114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541

    # algorithm
    for i in range (1, len(H)):
        r = (r*r) % n       # square
        if H[i] == '1':
            r = (r * x) % n # multiply

    # answer :)
    print(r)

main()