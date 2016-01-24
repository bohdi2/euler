#!/usr/bin/env python3


def mod3(n, r):
    count = 0
    for k in range(1, n + 1):
        if k % 3 == r:
            count += 1
    return count


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def bf_phi(n):
    count = 0
    for ii in range(n):
        if gcd(n, ii) == 1:
            count += 1

    return count


def diagonals(bounces):
    return 1 + (bounces + 1) // 2


def cycles(d):
    return -d % 3


def count_c(d, c):
    count = 0
    for ii in range(c, d, 3):
        if gcd(d, ii) == 1:
            count += 1

    return count


def bf_laser(bounces):
    d = diagonals(bounces)
    c = cycles(d)
    return count_c(d, c)


if __name__ == '__main__':

    b = 12017639147
    # b = 1000001

    print(1000001, bf_laser(1000001))
    # print(12017639147, laser(12017639147))

    # for d in range(0, n, 3):
    #    print(diagonals(d))

    # print()

    f = "{:>7}: {:>14} {:>14} {:>14} {:>5}"

    print(f.format("index",
                   "|0 (mod 3)|",
                   "|1 (mod 3)|",
                   "|2 (mod 3)|",
                   "laser"))

    for n in [1, 5, 7, 35]:
        print(f.format(n,
                       mod3(n, 0),
                       mod3(n, 1),
                       mod3(n, 2),
                       count_c(n, 2)))

    print(f.format("index",
                   "|0 (mod 3)|",
                   "|1 (mod 3)|",
                   "|2 (mod 3)|",
                   "laser"))

    for n in [1, 5, 11, 55]:
        print(f.format(n,
                       mod3(n, 0),
                       mod3(n, 1),
                       mod3(n, 2),
                       count_c(n, 2)))
