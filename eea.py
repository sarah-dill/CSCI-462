# EEA (extended euclidian algorithm)


def main():
    print("a mod b")
    a = input("Enter the first number (a) (larger number): ")
    b = input("Enter the second number (b): ")
    a = int(a)
    b = int(b)

    og_a = a
    og_b = b

    q = 0
    q_arr = []
    r = 0
    x = 0
    y = 0
    xp = 1
    yp = 0
    cnt = 0
    b1 = 0

    while not(b == 0):
        cnt += 1
        q = a // b
        q_arr.append(q)
        r = a % b
        a = b
        b = r
    
    if not (a == 1):
        print("No inverse exists")
        exit(0)

    for i in range(1, cnt+1):
        x = yp
        y = xp - (yp * q_arr[cnt-i])
        xp = x
        yp = y

    if x < 0:
        b1 = y
    elif y < 0:
        b1 = og_a + y

    print("Inverse of " + str(og_a) + " mod " + str(og_b) + ": " + str(b1))

        
main()