"""
find_primitive.py
Identifies primitive roots (generators) for a mod n
"""

def main():
    n = input("n value: ")
    n = int(n)

    is_primitive = True
    cnt = 0

    for i in range(2, n):
        for j in range(1, n):
            ans = pow(i, j, n)
            if ans == 1 and not (j == n-1):
                is_primitive = False
                break
            if j == n-1 and not (ans == 1):
                is_primitive = False
                break
            if j == n-1 and ans == 1:
                is_primitive = True
        if is_primitive:
            cnt += 1
            print(str(i) + " is primitive")
    print("Number primitive elements: " + str(cnt))

main()