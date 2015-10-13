#!/usr/bin/env python3

from itertools import cycle
import string

def read_cipher(filename):
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


def validate(text):
    return all(c in string.printable for c in text)

def find_potential_keys(text):
    cache = {}
    for k in range(128):
        decoded = decode(k, text)
        if validate(decoded):
            cache[k] = decoded

    return cache


def key_generator():
    for a in range(128):
        print(a)
        for b in range(128):
            for c in range(128):
                yield [a, b, c]
    return


def decode2(key, cipher):
    keys = cycle(key)
    return ints_to_string([next(keys) ^ n for n in cipher])


def main():
    cipher = read_cipher("p059_cipher.txt")
    c1, c2, c3 = map(find_potential_keys, split_cipher(cipher))

    #cache1 = find_potential_keys(c1)
    for c in c1, c2, c3:
        print(c.keys())

    #for k in range(128):
    #    decoded = decode(k, c1)
    #    if validate(decoded):
    #        print("%d: %s" % (k, decoded))

    for key in key_generator():
        s = decode2(key, cipher)
        if "the " in s:
            print("%s: %s " % (key, s))


if __name__ == "__main__":
    main()
