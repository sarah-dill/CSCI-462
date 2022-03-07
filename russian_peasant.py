"""
russian_peasant.py
Russian Peasant Algorithm
"""

def main():

    # get input
    num1 = input("First number: ")
    num2 = input("Second number: ")

    # check if input is hex digits
    try:
        num1 = int(num1, 16)
        num2 = int(num2, 16)

        # num3 = hex(int(num1) + int(num2))

    except:
        print("not valid input")
        exit(0)
    
    aes_irr = int('0x1B', 16)
    col1 = [num1]
    col2 = [num2]

    # Russian Peasant Algorithm

    # if the last element of the second column does not equal 1
    while not col2[-1] == 1:
        col1.append((int(col1[-1]) * 2))
        if int(col1[-1]) > int('0x100', 16):
            # mod by AES irreducible polynomial
            col1[-1] = (int(col1[-1]) ^ int(aes_irr)) - int('0x100', 16)
        col2.append((int(col2[-1]) // 2)) # cut off the decimal

    l = []

    # effectively cross out rows where col2's value is even
    for i in range(0, len(col1)):
        if not int(col2[i]) % 2 == 0:
            l.append(col1[i])

    # compute xor on remaining col1 values
    ans = 0
    for i in l:
        if ans == 0:
            ans += int(i)
        else:
            ans = ans ^ i

    # print answer in hex
    print(hex(ans))


main()