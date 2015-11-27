#!/usr/bin/env python3


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def diagonals(d):
    m = 0
    count = 0

    if d % 3 == 0:
        m = d//3 + 1
        for n in range(0, d, 3):
            if gcd(n, d) == 1:
                count += 1
    elif d % 3 == 1:
        m = d // 3
        for n in range(2, d, 3):
            if gcd(n, d) == 1:
                count += 1
    else:
        m = d // 3 + 1
        for n in range(1, d, 3):
            if gcd(n, d) == 1:
                count += 1

    return d, count, m, m - count


def bounces(b):
    d = (b + 1) // 2 + 1
    print(d)
    return diagonals(d)


if __name__ == '__main__':

    b = 12017639147
    #b = 1000001

    print(1000001, 1000001 % 3)
    print(12017639147, 12017639147 % 3)
    n = 100

    #for d in range(0, n, 3):
    #    print(diagonals(d))

    #print()

    f = "{:5}: {:18} {:18} {:18}"
    print(f.format("index",
                    "L, max, diff",
                    "L, max, diff",
                    "L, max, diff"))
    for e in enumerate(range(0, n, 3)):
        print(f.format(e[0],
                       str(diagonals(e[1]+0)),
                       str(diagonals(e[1]+1)),
                       str(diagonals(e[1]+2))))

    print()

    print(b, bounces(b))



