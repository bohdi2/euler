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

def create_cache(text):
    cache = {}
    for k in range(128):
        cache[k] = decode(k, text)

    return cache


def key_generator(c1, c2, c3):
    print("----")
    for a in c1.items():
        print(a[0])
        for b in c2.items():
            for c in c3.items():
                yield a, b, c     # Changed to be a tuple
    return


def decode2(key, cipher):
    keys = cycle(key)
    return ints_to_string([next(keys) ^ n for n in cipher])


def main():
    cipher = read_cipher("p059_cipher.txt")

    c1 = create_cache(cipher[0::3])
    c2 = create_cache(cipher[1::3])
    c3 = create_cache(cipher[2::3])

    print("c1 %s" % c1)

    for key in key_generator(c1, c2, c3):
        #print("key")
        #print(key)

        s = [c for t in zip(key[0][1], key[1][1], key[2][1]) for c in t]
        ss = ''.join(s)

        if "the " in ss:
            print("%s: %s " % (key, ss))


if __name__ == "__main__":
    main()
