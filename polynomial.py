"""
polynomial.py
Finds whether a polynomial of degree m is primitive or irreducible
Primitive: always produces maximum length
Irreducible: produces x length (not maximum - same every time)
"""

import random

def polynomial(m, max):
    m = int(m)

    # assign p_values
    p_values = [0] * m
    if m == 5:
        p_values[0] = 1
        p_values[2] = 1
    elif m == 6:
        p_values[0] = 1
        p_values[1] = 1
    elif m == 7:
        p_values[0] = 1
        p_values[1] = 1
    elif m == 8:
        p_values[0] = 1
        p_values[1] = 1
        p_values[3] = 1
        p_values[4] = 1
    elif m == 9:
        p_values[0] = 1
        p_values[1] = 1
    else:
        print("not valid")
        exit(0)

    og_s_values = [0] * m
    old_s_values = [0] * m
    num_ones = 0
    for i in range(0, m-1): # assign s_values
        og_s_values[i] = random.randrange(0, 2)
        if og_s_values[i] == 1:
            num_ones += 1
    if num_ones == 0:   # if all s_values are 0, make the last s_value 1
        og_s_values[m-1] = 1
    s_values = og_s_values.copy()
    
    num_rounds = 0
    is_primitive = False
    cont = True

    while cont:
        # get old s values
        for i in range(0, m):
            old_s_values[i] = s_values[i]

        # shift over all registers
        for i in range(0, m-1):
            s_values[i] = s_values[i+1]

        # calculate s_max-1
        x = 0
        for i in range(0, m):
            if p_values[i] == 1:                # if data can flow through
                x = x + old_s_values[i]         # assign x
        x = x % 2                               # perform mod operation
        s_values[m-1] = x                       # assign x to left-most s_value

        num_rounds += 1

        # check if all values are the same as the original
        for i in range(0, m):
            if not (s_values[i] == og_s_values[i]):
                break
            if (s_values[i] == og_s_values[i] and i == m-1):    # if last s_values are the same as the original, break from while loop
                if (num_rounds == max):
                    is_primitive = True
                cont = False
    
    print("Number of rounds: " + str(num_rounds))
    if is_primitive:
        print("Polynomial size " + str(m) + " is primitive")
    else:
        print("Polynomial size " + str(m) + " is irreducible")


def main():
    m = input("Enter degree of polynomial: ")
    max = 2 ** (int(m)) - 1
    polynomial(m, max)


main()
