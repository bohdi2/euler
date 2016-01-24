#!/usr/bin/env python3


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def isquareroot(n):
    return int(n ** 0.5) + 1


# Check if n is divisible by a square .
def is_divisible_by_square(n):
    i = 2
    while i ** 2 <= n:
        if n % (i ** 2) == 0:
            return 1
        i += 1
    return 0


# Count the number of prime factors of n.
def number_of_factors(n):
    counter = 0
    while n > 1:
        i = 2
        while i <= n:
            if n % i == 0:
                n /= i
                counter += 1
                break
            i += 1
    return counter


# The Mobius function .
def mu(n):
    if n == 1:
        return 1
    # Important to check this first .
    elif is_divisible_by_square(n):
        return 0
    else:
        # As n is not divisible by a square ,
        # every power of a prime is equal to one.
        # Hence , the number of factors is correct .
        return (-1) ** number_of_factors(n)


def find_divisors(n):
    factors = set()
    i = 1
    limit = isquareroot(n)

    while i <= limit:
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)

        i += 1
    return factors


def phi(n):
    sum = 0
    for d in find_divisors(n):
        sum += d * mu(n//d)
    return sum


def phi3(n):
    remainder = n % 3

    total = 0
    for divisor in find_divisors(n):
        count = (divisor + remainder) // 3
        print(divisor, remainder, count)
        total += count * mu(n // divisor)
    return total


def terminal(bounces):
    return (bounces+3)//2


def laser(bounces):
    terminal_line = terminal(bounces)
    return phi3(terminal_line)


def main():
    phi_format = "{0:<12} {1:<12} {2:<12}"
    print(phi_format.format("n", "phi(n)", "phi3(n)"))

    for n in [2,3,7]: #3, 4, 5, 11, 25, 64, 100, 1000001]:
    #    print(phi_format.format(n, phi(n), phi3(n)))
        c = phi3(n)
        print(c)

    print()

    laser_format = "{0:<12} {1:<12} {2:<12}"
    #print(laser_format.format("bounces", "terminal", "laser(n)"))

    # for n in range(1, 200):
    #    print(laser_format.format(n, terminal(n), laser(n)))

    #for n in [11]: #1000001, 12017639147, 715225739*2-3]:
        # print(laser_format.format(n, terminal(n), laser(n)))
    #    laser(n)


if __name__ == "__main__":
    main()
