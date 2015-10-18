#!/usr/bin/env python3

from collections import Counter
from itertools import zip_longest
import string


def read_cipher(filename):
    """returns a list of integers"""
    with open(filename, "r") as filestream:
        data = []
        for line in filestream:
            data += [int(s) for s in line.split(",")]
        return data


def ints_to_string(l):
    return "".join(map(chr, l))


def split_cipher(cipher):
    return cipher[0::3], cipher[1::3], cipher[2::3]


def decode(key, cipher):
    return ints_to_string([key ^ n for n in cipher])


def decode3(cipher):
    most_frequent = Counter(cipher).most_common(1)[0][0]
    key = ord(' ') ^ most_frequent

    return ints_to_string([key ^ n for n in cipher])


def main():
    cipher = read_cipher("p059_cipher.txt")

    t1 = decode3(cipher[0::3])
    t2 = decode3(cipher[1::3])
    t3 = decode3(cipher[2::3])

    s = [c for t in zip_longest(t1, t2, t3, fillvalue='') for c in t]
    ss = ''.join(s)

    print("ss", ss)
    print("ss", len(cipher), len(ss))
    print("sum", sum([ord(c) for c in ss]))


if __name__ == "__main__":
    main()
