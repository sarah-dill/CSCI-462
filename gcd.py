# gcd (greatest common divisor) algorithm

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def main():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = gcd(int(num1), int(num2))
    print("The gcd of " + num1 + " and " + num2 + " is " + str(result))

main()
