#!/usr/bin/env python3

import fractions


# check that n is in N \{0}.
def is_valid(n):
    if n <= 0:
        return 0
    elif n - int(n) != 0:
        return 0
    return 1


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def isqrt(n):
    return int(n ** 0.5) + 1


# The Mobius function .
def mu(n):
    if not is_valid(n):
        return 0
    elif n == 1:
        return 1
    # Important to check this first .
    elif is_divisible_by_square(n):
        return 0
    else:
        # As n is not divisible by a square ,
        # every power of a prime is equal to one.
        # Hence , the number of factors is correct .
        return (-1) ** number_of_factors(n)


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


def find_factors(n):
    factors = [1]
    while n > 1:
        i = 2
        while i <= n:
            if n % i == 0:
                factors.append(i)
                n //= i
                break
            i += 1
    return factors


def find_divisors(n):
    factors = set()
    i = 1
    limit = isqrt(n)
    while i <= limit:
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)

        i += 1
    return factors


# The number of numbers smaller than or
# equal to n which is relatively prime to n
def phi(n):
    if not is_valid(n):
        return 0
    if n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            if (int(n) % i) == 0 and is_prime(i):
                n *= (1 - (1.0 / i))
        return int(n)


# Check if a numer is prime or not
def is_prime(n):
    return not (n < 2 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)))


def brute_force_phi(n):
    amount = 0

    for k in range(1, n+1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount


def sum_mod3(n, r):
    return (n + r) // 3


def brute_force_sum_mod3(n, r):
    count = 0
    for k in range(1, n + 1):
        if k % 3 == r:
            count += 1
    return count


if __name__ == "__main__":
    for ii in range(25, 30):
        print("mod3", 0, ii, brute_force_sum_mod3(ii, 0), sum_mod3(ii, 0))
        print("mod3", 1, ii, brute_force_sum_mod3(ii, 1), sum_mod3(ii, 1))
        print("mod3", 2, ii, brute_force_sum_mod3(ii, 2), sum_mod3(ii, 2))

    def ff(n):
        def f(i):
            return i*mu(n//i)
        return f

    def ff3(n):
        def f(i):
            return sum_mod3(i, n % 3)*mu(n//i)
        return f


    #for nn in range(20, 40):
    #    ds = find_divisors(nn)
    #    xs = list(map(ff(nn), ds))
    #    print(nn, ds, xs, sum(xs), phi(nn))

    nn = (11 + 3) // 2
    ds = find_divisors(nn)
    xs = list(map(ff3(nn), ds))
    print(nn, sum(xs))

    nn = (1000001 + 3) // 2
    ds = find_divisors(nn)
    xs = list(map(ff(nn), ds))
    print(nn, sum(xs))

    nn = (1000001 + 3) // 2
    ds = find_divisors(nn)
    xs = list(map(ff3(nn), ds))
    print(nn, sum(xs),  80840)

    nn = (12017639147 + 3) // 2
    ds = find_divisors(nn)
    xs = list(map(ff3(nn), ds))
    print(nn, sum(xs), 1209002624)
